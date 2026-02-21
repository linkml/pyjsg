import os
import re

import pytest
from io import StringIO
from types import ModuleType
from typing import cast, TextIO, Any

from pyjsg.validate_json import JSGPython
from pyjsg.jsglib.loader import loads, Logger, is_valid
from pyjsg.parser_impl.generate_python import parse

CWD = os.path.abspath(os.path.dirname(__file__))

LOCAL_TEST_FILES = False
USE_REL_TEST_PATHS = True
ONLY_TEST_THIS = ""
STOP_ON_ERROR = False

if LOCAL_TEST_FILES:
    organization_root = os.path.join(CWD, '../../../')
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


cwd = os.path.abspath(os.path.join(os.path.dirname(__file__)))

save_output_files = False
save_all_output_files = False


def strip_details(txt: str) -> str:
    txt = re.sub(r'(# Auto generated from JSGPython by PyJSG version ).*', r'\1', txt)
    return re.sub(r'(# Generation date:).*', r'\1', txt).strip()


@pytest.fixture(autouse=True)
def check_save_flags():
    yield
    assert not save_output_files, "save_output_files is True"
    if save_all_output_files:
        print("Warning: save_all_output_files is True")


@pytest.fixture
def do_python_generator_test():
    def _do_test(jsg: str, test_file: str, module, passing_json: list[str], failing_vars: dict[str, Any],
                 failing_json: list[str] = None, print_python: bool = False) -> None:
        x = JSGPython(jsg, print_python=print_python)
        py_file = os.path.join(cwd, "test_python_generator", "py", test_file + '.py')
        with open(py_file) as f:
            expected = strip_details(f.read())
        actual = strip_details(x.python)
        if expected != actual:
            if save_output_files or save_all_output_files:
                with open(py_file, 'w') as f:
                    f.write(x.python)
                    print(f"***** {py_file} updated *****")
            assert expected == actual

        for p in passing_json:
            json_doc = loads(p, module)
            log = StringIO()
            assert is_valid(json_doc, log), log.getvalue()

        for f in (failing_json or []):
            doc_is_valid = True
            json_doc = None
            try:
                json_doc = loads(f, module)
            except ValueError:
                doc_is_valid = False
            if doc_is_valid:
                log = StringIO()
                doc_is_valid = is_valid(json_doc, log)
            assert not doc_is_valid, f

        for k, v in failing_vars.items():
            with pytest.raises(ValueError):
                vv = f'"{v}"' if isinstance(v, str) else str(v)
                loads(f'{{"{k}": {vv}}}', module)

    return _do_test


@pytest.fixture(scope="session")
def shex_parser():
    return JSGPython(shexJSGSource)


@pytest.fixture
def do_test_harness(request):
    def _do_test(jsg: str, json: str, should_pass: bool = True, _: bool = True,
                 fails_validation: bool = False, expected: str = None) -> None:
        test_name = request.node.name
        python = parse(jsg, test_name)
        spec = compile(python, test_name, 'exec')
        module = ModuleType(test_name)
        exec(spec, module.__dict__)

        if should_pass:
            assert is_valid(loads(json, module))
        elif fails_validation:
            logf = StringIO()
            logger = Logger(cast(TextIO, logf))
            assert not is_valid(loads(json, module), logger)
            if expected:
                assert expected == logf.getvalue().strip('\n')
            else:
                print(logf.getvalue())
            assert logger.nerrors > 0
        else:
            with pytest.raises(ValueError):
                is_valid(loads(json, module))

    return _do_test


@pytest.fixture
def do_builtin_test():
    def _do_builtin_test(cls, val, rslt=None, fail=False):
        if fail:
            with pytest.raises(ValueError):
                cls(val)
        else:
            t = cls(val)
            assert t == (rslt if rslt is not None else val)
            if not isinstance(t, bool):
                assert t.val == (rslt if rslt is not None else val)
            return t

    return _do_builtin_test


@pytest.fixture
def do_string_test():
    def _do_string_test(jsgstr, val, is_valid=True):
        if not is_valid:
            with pytest.raises(ValueError):
                jsgstr(val)
        else:
            v = jsgstr(val)
            assert v == str(val)

    return _do_string_test


@pytest.fixture
def jsg1():
    return '''
    .TYPE t - id val ;
    doc {a:.,}
    id {b: @int}
    val {c: @string}
    '''
