import pytest
from typing import cast

from pyjsg.parser_impl.jsg_objectexpr_parser import JSGObjectExpr
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

ref_tests = [("A", "ID"),
             ("a", "ID"),
             ("ABCt", "ID"),
             ("aNID", "ID"),
             ("AA", "LEXER_ID_REF"),
             ("HEX_NUM", "LEXER_ID_REF")]


@pytest.mark.parametrize("text,sig,typ_,mt_typ", builtin_tests, ids=[t[0] for t in builtin_tests])
def test_builtins(text, sig, typ_, mt_typ):
    t = cast(JSGValueType, parse(text, "valueType", JSGValueType))
    assert t.signature_type() == sig, text
    assert t.python_type() == typ_, text
    assert str(t) == f"valueType: builtinValueType: {'jsg.AnyType' if text == '.' else text}", text
    assert t.mt_value() == mt_typ, text
    assert t.members_entries() == [], text
    assert t.dependency_list() == [], text


@pytest.mark.parametrize("text,typ", ref_tests, ids=[t[0] for t in ref_tests])
def test_refs(text, typ):
    t = cast(JSGValueType, parse(text, "valueType", JSGValueType))
    assert t.signature_type() == (f'Undefined({text})' if typ != 'LEXER_ID_REF' else text)
    assert t.python_type() == (f'Undefined({text})' if typ != 'LEXER_ID_REF' else 'str')
    assert str(t) == f"valueType: {typ}: {text}"
    assert t.dependency_list() == [text]
    assert t.members_entries() == []
    assert t.mt_value() == "None"


def test_ref_escapes():
    assert cast(JSGValueType, parse("Class", "valueType", JSGValueType)).signature_type() == "Undefined(Class)"
    t = cast(JSGValueType, parse("class", "valueType", JSGValueType))
    assert t.signature_type() == "Undefined(class_)"
    assert t.python_type() == "Undefined(class_)"
    assert t.members_entries() == []


def test_literals():
    t = cast(JSGValueType, parse("'literal'", "valueType", JSGValueType))
    assert t.signature_type() == "_Anon1"
    assert t.python_type() == "str"
    assert str(t) == "valueType: STRING: pattern: r'literal'"


def test_any():
    t = cast(JSGValueType, parse("id = .;", "valueTypeMacro", JSGValueType))
    assert t.python_type() == "object"
    assert t.signature_type() == "jsg.AnyTypeFactory('{name}', _CONTEXT)"
    assert t.mt_value() == "jsg.Empty"
    assert t.members_entries() == []
    assert t.dependency_list() == []
    assert str(t) == "valueType: builtinValueType: jsg.AnyType"


def test_alternatives():
    t = cast(JSGValueType, parse("id = ('x'|'y') ;", "valueTypeMacro", JSGValueType))
    assert t.signature_type() == "_Anon1"
    assert t.python_type() == "str"
    assert str(t) == "valueType: STRING: pattern: r'(x)|(y)'"

    t = cast(JSGValueType, parse("id = (Aa | Bb | (Cc | Dd)) ;", "valueTypeMacro", JSGValueType))
    assert t.signature_type() == "typing.Union[Undefined(Aa), Undefined(Bb), typing.Union[Undefined(Cc), Undefined(Dd)]]"
    assert t.python_type() == "typing.Union[Undefined(Aa), Undefined(Bb), typing.Union[Undefined(Cc), Undefined(Dd)]]"
    assert t.dependency_list() == ['Aa', 'Bb', 'Cc', 'Dd']
    assert str(t) == "valueType: (Undefined(Aa) | Undefined(Bb) | typing.Union[Undefined(Cc), Undefined(Dd)])"
    assert t.members_entries() == []

    t = cast(JSGValueType, parse("id = (Aa | Bb | 'foo' | (Cc | Dd) | 'bar') ;", "valueTypeMacro", JSGValueType))
    assert t.signature_type() == ("typing.Union[_Anon1, Undefined(Aa), Undefined(Bb), "
                                   "typing.Union[Undefined(Cc), Undefined(Dd)]]")
    assert t.python_type() == ("typing.Union[str, Undefined(Aa), Undefined(Bb), "
                                "typing.Union[Undefined(Cc), Undefined(Dd)]]")
    assert t.dependency_list() == ['_Anon1', 'Aa', 'Bb', 'Cc', 'Dd']
    assert str(t) == ("valueType: ((STRING: pattern: r'(foo)|(bar)') | Undefined(Aa) | Undefined(Bb) | "
                      "typing.Union[Undefined(Cc), Undefined(Dd)])")


def test_array():
    t = cast(JSGValueType, parse('id = [.] ;', "valueTypeMacro", JSGValueType))
    assert str(t) == 'valueType: arrayExpr: [valueType: builtinValueType: jsg.AnyType]'
    assert t.dependency_list() == []
    assert t.members_entries() == []
    assert t.python_type() == 'list[object]'
    assert t.signature_type() == "jsg.ArrayFactory('{name}', _CONTEXT, jsg.AnyTypeFactory('{name}', _CONTEXT), 0, None)"
    assert t.mt_value() == 'None'

    t = cast(JSGValueType, parse('id = [@int | "AB*" +] ;', "valueTypeMacro", JSGValueType))
    assert str(t) == ("valueType: arrayExpr: [(valueType: builtinValueType: "
                      "@int | valueType: STRING: pattern: r'AB\\*')+]")
    assert t.dependency_list() == ['_Anon1']
    assert t.members_entries() == []
    assert t.python_type() == 'list[typing.Union[int, str]]'
    assert t.signature_type() == "jsg.ArrayFactory('{name}', _CONTEXT, typing.Union[jsg.Integer, _Anon1], 1, None)"
    assert t.mt_value() == 'None'


def test_lexeridref():
    t = cast(JSGValueType, parse('("[a-z]*" | "0-9*")', "valueType", JSGValueType))
    assert str(t) == "valueType: STRING: pattern: r'(\\[a\\-z\\]\\*)|(0\\-9\\*)'"
    assert t.signature_type() == "_Anon1"
    assert t.python_type() == "str"
    assert t.mt_value() == "None"
    assert t.members_entries() == []

    t = cast(JSGValueType, parse('("[a-z]*" | "0-9*" | ID)', "valueType", JSGValueType))
    assert str(t) == "valueType: ((STRING: pattern: r'(\\[a\\-z\\]\\*)|(0\\-9\\*)') | ID)"
    assert t.signature_type() == "typing.Union[_Anon1, ID]"
    assert t.python_type() == "typing.Union[str, str]"
    assert t.mt_value() == "None"
    assert t.members_entries() == []


def test_anon_typeid():
    t = cast(JSGValueType, parse("{a: @int b: @string+}", "valueType", JSGValueType))
    assert str(t) == 'valueType: (anonymous: _Anon1): objectExpr: simple object'
    assert t.signature_type() == '_Anon1'
    assert t.python_type() == '_Anon1'
    assert t.mt_value() == 'None'
    assert t.members_entries() == []


def test_objectmacro_opts():
    t = cast(JSGValueType, parse("a = @string | KT | {} ;", "valueTypeMacro", JSGValueType))
    assert str(t) == 'valueType: (jsg.String | KT | _Anon1)'
    assert t.signature_type() == 'typing.Union[jsg.String, KT, _Anon1]'
    assert t.python_type() == 'typing.Union[str, str, _Anon1]'
    assert t.mt_value() == 'None'
    assert t.members_entries() == []


def test_objectmacro():
    t = cast(JSGObjectExpr, parse("stringFacet = (length minlength maxlength):"
                                  "INTEGER pattern:STRING flags:STRING? ;", "objectMacro", JSGObjectExpr))
    assert t.as_python('stringFacet').strip() == """class stringFacet(jsg.JSGObject):
    _reference_types = []
    _members = {'length': INTEGER,
                'minlength': INTEGER,
                'maxlength': INTEGER,
                'pattern': STRING,
                'flags': typing.Optional[STRING]}
    _strict = True

    def __init__(self,
                 length: str = None,
                 minlength: str = None,
                 maxlength: str = None,
                 pattern: str = None,
                 flags: typing.Optional[str] = None,
                 **_kwargs: dict[str, object]):
        super().__init__(_CONTEXT, **_kwargs)
        self.length = length
        self.minlength = minlength
        self.maxlength = maxlength
        self.pattern = pattern
        self.flags = flags"""
    assert t.dependency_list() == ['INTEGER', 'STRING']

    t = cast(JSGObjectExpr, parse("stringFacet = (length minlength maxlength):INTEGER "
                                  "pattern:STRING | flags:STRING? ;", "objectMacro", JSGObjectExpr))
    assert t.as_python('stringFacet').strip() == """class stringFacet(jsg.JSGObject):
    _reference_types = [_Anon1_1_, _Anon1_2_]
    _members = {'length': typing.Optional[INTEGER],
                'minlength': typing.Optional[INTEGER],
                'maxlength': typing.Optional[INTEGER],
                'pattern': typing.Optional[STRING],
                'flags': typing.Optional[STRING]}
    _strict = True

    def __init__(self,
                 opts_: typing.Union[_Anon1_1_, _Anon1_2_] = None,
                 **_kwargs: dict[str, object]):
        super().__init__(_CONTEXT, **_kwargs)
        if opts_ is not None:
            if isinstance(opts_, _Anon1_1_):
                self.length = opts_.length
                self.minlength = opts_.minlength
                self.maxlength = opts_.maxlength
                self.pattern = opts_.pattern
            elif isinstance(opts_, _Anon1_2_):
                self.flags = opts_.flags
            else:
                raise ValueError(f"Unrecognized value type: {opts_}")"""
    assert t.dependency_list() == ['INTEGER', 'STRING', '_Anon1_1_', '_Anon1_2_']

    t = cast(JSGObjectExpr, parse("x = a:@number | b:@null | ;", "objectMacro", JSGObjectExpr))
    assert t.as_python('stringFacet').strip() == """class stringFacet(jsg.JSGObject):
    _reference_types = [_Anon1_1_, _Anon1_2_, _Anon1_3_]
    _members = {'a': typing.Optional[jsg.Number],
                'b': typing.Optional[jsg.JSGNull]}
    _strict = True

    def __init__(self,
                 opts_: typing.Union[_Anon1_1_, _Anon1_2_, _Anon1_3_] = None,
                 **_kwargs: dict[str, object]):
        super().__init__(_CONTEXT, **_kwargs)
        if opts_ is not None:
            if isinstance(opts_, _Anon1_1_):
                self.a = opts_.a
            elif isinstance(opts_, _Anon1_2_):
                self.b = opts_.b
            elif isinstance(opts_, _Anon1_3_):
                pass
            else:
                raise ValueError(f"Unrecognized value type: {opts_}")"""
    assert t.dependency_list() == ['_Anon1_1_', '_Anon1_2_', '_Anon1_3_']