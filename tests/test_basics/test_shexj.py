import os
import unittest
from contextlib import redirect_stdout
from io import StringIO
from typing import TextIO, cast

import requests
from dict_compare import compare_dicts
from jsonasobj import loads as jao_loads
from jsonasobj.jsonobj import as_dict, as_json

from pyjsg.validate_json import JSGPython

CWD = os.path.abspath(os.path.dirname(__file__))

# Test configuration variables
#     If you are going to be doing a lot of testing, it would be in your best interest to clone a copy of
#     https://github.com/shexSpec/shexTest into a local directory.  The configuration below is intended to
#     work with:
#     <path> +---  hsolbrig/pyjsg/tests/test_basics/test_shexj.py
#            |
#            +---- shexSpec/shexTest/schemas/*.jsg
#            |
#            +---- hsolbrig/ShExJSG/ShExJSG/ShExJ.jsg
#
# If you set LOCAL_TEST_FILES to True, shexTestRepository will be set as above.  You can obviously point it somewhere
# else if needed, but please don't check it in that way.
#
# USE_REL_TEST_PATHS = True attempts to hide absolute paths from logs and various things, but, as it makes debugging
# difficult, you can set it to False whilst debugging.
#
# If you set LOCAL_TEST_FILES to False, the following locations will be used:
#
#  - - - - -
#
# SHEXJ_JSG should point at the image of ShExJ.jsg to be used in the testing process.  We keep a local copy in
#    pyjsg/tests/test_basics/jsg/ShExJ.jsg to minimize the dependencies between ShExJSG and pyjsg.  One should
#    try to keep this up to date with the master, which can be found in:
#               https://github.com/hsolbrig/ShExJSG/ShExJSG/ShExJ.jsg
#
# ===== CHECKING IN =======
# LOCAL_TEST_FILES = False
# USE_REL_TEST_PATHS = True
# ONLY_TEST_THIS = ""
# STOP_ON_ERROR = False

LOCAL_TEST_FILES = False              # True means use files that have been checked out from repository, False repository
USE_REL_TEST_PATHS = True             # True means relative paths, false absolute
ONLY_TEST_THIS = ""                   # If not empty, path to a single file you want to do a test on
STOP_ON_ERROR = False                 # True means stop on first error.  False means test all jsg

if LOCAL_TEST_FILES:
    # Files are local and stored relative to this directory
    organization_root = os.path.join(CWD, '../../../')            # test_basic/tests/pyjsg/  HERE
    shexJSGSource = os.path.relpath(os.path.join(organization_root, 'ShExJSG/ShExJSG/ShExJ.jsg'), CWD)
    shexTestRepository = os.path.relpath(os.path.join(organization_root, '../shexSpec/shexTest/schemas'), CWD)
    if not USE_REL_TEST_PATHS:
        shexJSGSource = os.path.abspath(shexJSGSource)
        shexTestRepository = os.path.abspath(shexTestRepository)
    assert os.path.exists(shexJSGSource)
    assert os.path.exists(shexTestRepository)
else:
    shexTestRepository = "https://api.github.com/repos/shexSpec/shexTest/contents/schemas?ref=main"
    shexJSGSource = "https://raw.githubusercontent.com/hsolbrig/ShExJSG/master/ShExJSG/ShExJ.jsg"
print(f"TESTING *.json from: {shexTestRepository} against {shexJSGSource}")


# Files to skip until we reintroduce a manifest reader
skip = ['coverage.json', 'manifest.json', 'representationTests.json']


def compare_json(j1: str, j2: str, log: TextIO) -> bool:
    """ Compare two JSON strings """
    d1 = jao_loads(j1)
    d2 = jao_loads(j2)
    return compare_dicts(as_dict(d1), as_dict(d2), file=log)


def validate_shexj_json(json_str: str, input_fname: str, parser: JSGPython) -> bool:
    """Validate json_str against ShEx Schema

    :param json_str: String to validate
    :param input_fname: Name of source file for error reporting
    :param parser: JSGPython parser
    :return: True if pass
    """
    rslt = parser.conforms(json_str, input_fname)
    if not rslt.success:
        print("File: {} - ".format(input_fname))
        print(str(rslt.fail_reason))
        return False
    else:
        log = StringIO()
        if not compare_json(json_str, as_json(parser.json_obj), cast(TextIO, log)):
            print("File: {} - ".format(input_fname))
            print(log.getvalue())
            print(as_json(parser.json_obj))
            return False
    return True


class FileValidator:
    def __init__(self):
        self.nvalidated = 0
        self.nskipped = 0

    def validate_file(self, download_file: str, parser: JSGPython) -> bool:
        fname = download_file.rsplit('/', 1)[1]
        if fname not in skip and 'futureWork' not in download_file:
            if '://' in download_file:
                resp = requests.get(download_file)
                if resp.ok:
                    text = resp.text
                else:
                    print("Error {}: {}".format(resp.status_code, resp.reason))
                    return False
            else:
                with open(download_file) as f:
                    text = f.read()
            self.nvalidated += 1
            return validate_shexj_json(text, download_file, parser)
        print("Skipping {}".format(download_file))
        self.nskipped += 1
        return True


def download_github_file(github_url: str) -> str | None:
    """
    Download the file in github_url
    :param github_url: github url to download
    :return: file contents if success, None otherwise
    """
    print("Downloading {}".format(github_url))
    resp = requests.get(github_url)
    if resp.ok:
        resp = requests.get(resp.json()['download_url'])
        if resp.ok:
            return resp.text
    print("Error {}: {}".format(resp.status_code, resp.reason))
    return None


def validate_shex_schemas(parser: JSGPython, validator: FileValidator) -> bool:
    if not ONLY_TEST_THIS:
        filelist = []
        if '://' in shexTestRepository:
            resp = requests.get(shexTestRepository)
            if resp.ok:
                filelist = [f['download_url'] for f in resp.json() if f['name'].endswith('.json')]
            else:
                print("Error {}: {}".format(resp.status_code, resp.reason))
                return False
        else:
            for dirpath, _, filenames in os.walk(shexTestRepository):
                filelist += [os.path.join(dirpath, f) for f in filenames if f.endswith('.json')]
        if STOP_ON_ERROR:
            return all(validator.validate_file(f, parser) for f in filelist)
        else:
            return all([validator.validate_file(f, parser) for f in filelist])
    else:
        return validator.validate_file(ONLY_TEST_THIS, parser)


class ShExJValidationTestCase(unittest.TestCase):

    @unittest.skipIf(False, "Schema tests disabled -- do not commit in this state")
    def test_shex_schema(self):
        parser = JSGPython(shexJSGSource)
        log_path = os.path.join(os.path.abspath(os.path.dirname(__file__)), 'logs', 'test_shex_schema.log')
        validator = FileValidator()
        with open(log_path, 'w') as logf:
            with redirect_stdout(logf):
                self.assertTrue(validate_shex_schemas(parser, validator), f"See {log_path} for reasons")
        print(f"{validator.nvalidated} files validated - {validator.nskipped} skipped")


if __name__ == '__main__':
    unittest.main()
