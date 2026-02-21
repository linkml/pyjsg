import os
import requests
import pytest
from contextlib import redirect_stdout
from io import StringIO
from typing import TextIO, cast

from dict_compare import compare_dicts
from jsonasobj import loads as jao_loads
from jsonasobj.jsonobj import as_dict, as_json

from tests.conftest import (
    CWD, ONLY_TEST_THIS, shexTestRepository
)

skip = ['coverage.json', 'manifest.json', 'representationTests.json']


def compare_json(j1: str, j2: str, log: TextIO) -> bool:
    d1 = jao_loads(j1)
    d2 = jao_loads(j2)
    return compare_dicts(as_dict(d1), as_dict(d2), file=log)


def validate_shexj_json(json_str: str, input_fname: str, parser) -> bool:
    rslt = parser.conforms(json_str, input_fname)
    if not rslt.success:
        print(f"File: {input_fname} - ")
        print(str(rslt.fail_reason))
        return False
    log = StringIO()
    if not compare_json(json_str, as_json(parser.json_obj), cast(TextIO, log)):
        print(f"File: {input_fname} - ")
        print(log.getvalue())
        print(as_json(parser.json_obj))
        return False
    return True


def get_file_list() -> list[str]:
    if ONLY_TEST_THIS:
        return [ONLY_TEST_THIS]
    if '://' in shexTestRepository:
        resp = requests.get(shexTestRepository)
        if resp.ok:
            return [f['download_url'] for f in resp.json() if f['name'].endswith('.json')]
        raise RuntimeError(f"Error {resp.status_code}: {resp.reason}")
    filelist = []
    for dirpath, _, filenames in os.walk(shexTestRepository):
        filelist += [os.path.join(dirpath, f) for f in filenames if f.endswith('.json')]
    return filelist


def fetch_file(url: str) -> str:
    if '://' in url:
        resp = requests.get(url)
        if resp.ok:
            return resp.text
        raise RuntimeError(f"Error {resp.status_code}: {resp.reason}")
    with open(url) as f:
        return f.read()


def should_skip(download_file: str) -> bool:
    fname = download_file.rsplit('/', 1)[1]
    return fname in skip or 'futureWork' in download_file


@pytest.mark.parametrize("download_file", get_file_list())
def test_shex_schema(download_file, shex_parser):
    if should_skip(download_file):
        pytest.skip(f"Skipping {download_file}")
    text = fetch_file(download_file)
    log_path = os.path.join(CWD, 'test_basics', 'logs', 'test_shex_schema.log')
    with open(log_path, 'a') as logf:
        with redirect_stdout(logf):
            assert validate_shexj_json(text, download_file, shex_parser), f"See {log_path} for reasons"