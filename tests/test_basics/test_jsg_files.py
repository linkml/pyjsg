import os
import pytest
from contextlib import redirect_stdout
from io import StringIO


def get_jsg_files(base):
    jsg_files = []
    for dirpath, _, filenames in os.walk(os.path.join(base, "jsg")):
        for fn in filenames:
            if fn.endswith(".jsg"):
                infile = os.path.relpath(os.path.join(dirpath, fn))
                outfile = os.path.relpath(
                    os.path.join(base, "py", fn.rsplit('.', 1)[0] + '.py')
                )
                jsg_files.append((infile, outfile))
    return jsg_files


base = os.path.abspath(os.path.dirname(__file__))
jsg_params = get_jsg_files(base)


@pytest.mark.parametrize("infile,outfile", jsg_params)
def test_jsg_file(infile, outfile):
    from pyjsg.parser_impl.generate_python import generate
    outf = StringIO()
    with redirect_stdout(outf):
        assert generate([infile, "-o", outfile, "-e", "-nh"]) == 0


def test_file_count():
    assert len(jsg_params) == 24
