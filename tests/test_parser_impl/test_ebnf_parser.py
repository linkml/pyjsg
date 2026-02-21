from dataclasses import dataclass
from typing import cast, Optional

import pytest

from pyjsg.parser_impl.jsg_ebnf_parser import JSGEbnf
from pyjsg.parser_impl.jsg_valuetype_parser import JSGValueType

from tests.test_basics.parser import parse


@dataclass
class testentry:
    text: str
    min: int
    max: Optional[int]
    ptype: str
    oneopt: bool
    mult: bool
    stype: str


tests = [testentry('*', 0, None, "list[k]", False, True, "jsg.ArrayFactory('{name}', _CONTEXT, k, 0, None)"),
         testentry('?', 0, 1, "typing.Optional[k]", True, False, "typing.Optional[k]"),
         testentry('+', 1, None, "list[k]", False, True, "jsg.ArrayFactory('{name}', _CONTEXT, k, 1, None)"),
         testentry('{0}', 0, 0, "type(None)", False, False, "type(None)"),
         testentry('{0, 1}', 0, 1, "typing.Optional[k]", True, False, "typing.Optional[k]"),
         testentry('{1}', 1, 1, "k", False, False, "k"),
         testentry('{1, }', 1, None, "list[k]", False, True, "jsg.ArrayFactory('{name}', _CONTEXT, k, 1, None)"),
         testentry('{2}', 2, 2, "list[k]", False, True, "jsg.ArrayFactory('{name}', _CONTEXT, k, 2, 2)"),
         testentry('{2 ,}', 2, None, "list[k]", False, True, "jsg.ArrayFactory('{name}', _CONTEXT, k, 2, None)"),
         testentry('{ 3 , * }', 3, None, "list[k]", False, True, "jsg.ArrayFactory('{name}', _CONTEXT, k, 3, None)"),
         testentry('{3,7}', 3, 7, "list[k]", False, True, "jsg.ArrayFactory('{name}', _CONTEXT, k, 3, 7)")]


@pytest.mark.parametrize("te", tests, ids=[te.text for te in tests])
def test_basics(te):
    t = cast(JSGEbnf, parse(te.text, "ebnfSuffix", JSGEbnf))
    assert str(t) == te.text.replace(' ', ''), te.text
    assert t.min == te.min, te.text
    assert t.max == te.max, te.text
    assert t.python_cardinality("k") == te.ptype, te.text
    assert t.signature_cardinality("k") == te.stype, te.text
    assert t.one_optional_element == te.oneopt, te.text
    assert t.multiple_elements == te.mult, te.text


def test_double_optional():
    t = cast(JSGEbnf, parse('?', 'ebnfSuffix', JSGEbnf))
    assert 'typing.Optional[k]' == t.python_cardinality('typing.Optional[k]')
    assert 'typing.Optional[k]' == t.signature_cardinality('typing.Optional[k]')


def test_all_optional():
    t = cast(JSGEbnf, parse('?', 'ebnfSuffix', JSGEbnf))
    assert 'typing.Optional[k]' == t.python_cardinality('k', True)
    assert "typing.Optional[k]" == t.signature_cardinality('k', True)
    t = cast(JSGEbnf, parse('+', 'ebnfSuffix', JSGEbnf))
    assert 'typing.Optional[list[k]]' == t.python_cardinality('k', True)
    assert "typing.Optional[jsg.ArrayFactory('{name}', _CONTEXT, k, 1, None)]" == t.signature_cardinality('k', True)
