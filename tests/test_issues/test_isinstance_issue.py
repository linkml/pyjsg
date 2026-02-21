import os
from typing import Union

from pyjsg.jsglib import isinstance_


def test_isinstance_issue():
    from pyjsg.jsglib.loader import isinstance_
    x = Union[int, str]
    assert isinstance(17, x)
    assert isinstance_(17, x)


def test_issue_with_shexj():
    from pyjsg.parser_impl.generate_python import generate
    data_root = os.path.join(os.path.split(os.path.abspath(__file__))[0], '..', 'test_basics')
    jsg_path = os.path.relpath(os.path.join(data_root, 'jsg', 'ShExJ.jsg'))
    py_path = os.path.abspath(os.path.join(data_root, 'py', 'ShExJ.py'))
    assert generate([jsg_path, "-o", py_path, "-e", "-nh"]) == 0
    from tests.test_basics.py import ShExJ
    assert isinstance_(ShExJ.IRIREF("http://foo.bar"), ShExJ.shapeExprLabel)