from typing import cast

import pytest

from pyjsg.parser_impl.jsg_builtinvaluetype_parser import JSGBuiltinValueType
from pyjsg.parser_impl.jsg_valuetype_parser import JSGValueType
from tests.test_basics.parser import parse

builtin_tests = [("@string", "jsg.String", "str", "None"),
                 ("@number", "jsg.Number", "float", "None"),
                 ("@int", "jsg.Integer", "int", "None"),
                 ("@bool", "jsg.Boolean", "bool", "None"),
                 ("@null", "jsg.JSGNull", "type(None)", "jsg.Empty"),
                 ("@array", "jsg.ArrayFactory('{name}', _CONTEXT, jsg.AnyType, 0, None)", "list", "None"),
                 ("@object", "jsg.ObjectFactory('{name}', _CONTEXT, jsg.Object)", "object", "None"),
                 (".", "jsg.AnyTypeFactory('{name}', _CONTEXT)", "object", "jsg.Empty")]


@pytest.mark.parametrize("text,sig,typ_,mt_typ", builtin_tests)
def test_builtins(text, sig, typ_, mt_typ):
    t = cast(JSGValueType, parse(text, "builtinValueType", JSGBuiltinValueType))
    assert t.signature_type() == sig, text
    assert t.python_type() == typ_, text
    assert str(t) == f"builtinValueType: {text if text != '.' else 'jsg.AnyType'}", text
    assert t.mt_value() == mt_typ, text
    assert t.members_entries() == [], text
    assert t.dependency_list() == [], text