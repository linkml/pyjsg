import os
import pytest


def test_execute_item(tmp_path):
    from pyjsg.parser_impl.generate_python import generate, evaluate

    basedir = os.path.abspath(os.path.dirname(__file__))
    goodfile = tmp_path / "goodjsg.py"
    badfile = tmp_path / "badjsg.py"

    # Make sure that a simple generate works
    assert generate([os.path.join(basedir, "jsg", "complexfacet.jsg"), "-o", str(goodfile), "-e", "-nh"]) == 0

    # Make sure that we can detect exceptions and errors
    with open(badfile, 'w') as bf:
        bf.write("i=1/0\n")
        with open(goodfile) as gf:
            bf.write(gf.read())

    with pytest.raises(ZeroDivisionError):
        evaluate("bar", str(badfile), False)

    # Make sure that our namespace hasn't been messed up
    assert 'bar' not in globals()