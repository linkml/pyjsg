import pytest
from typing import cast

from pyjsg.parser_impl.jsg_doc_parser import JSGDocParser
from pyjsg.parser_impl.jsg_pairdef_parser import JSGPairDef
from tests.test_basics.parser import parse

tests = [("x1 : INT", "INT", "str", ["INT"], ['x1: str = None'], [('x1', 'INT')],
          "pairDef: x1 : valueType: LEXER_ID_REF: INT"),
         ("x2 : INT?", "typing.Optional[INT]", "typing.Optional[str]", ["INT"], ['x2: typing.Optional[str] = None'], [
             ('x2', 'typing.Optional[INT]')], "pairDef: x2 : valueType: LEXER_ID_REF: INT?"),
         ("x3 : INT+", "jsg.ArrayFactory('{name}', _CONTEXT, INT, 1, None)", "typing.List[str]", ["INT"],
          ['x3: typing.List[str] = None'], [('x3', "jsg.ArrayFactory('x3', _CONTEXT, INT, 1, None)")],
          "pairDef: x3 : valueType: LEXER_ID_REF: INT+"),
         ("x4 : INT*", "jsg.ArrayFactory('{name}', _CONTEXT, INT, 0, None)", "typing.List[str]",
          ["INT"], ['x4: typing.List[str] = None'], [("x4", "jsg.ArrayFactory('x4', _CONTEXT, INT, 0, None)")],
          "pairDef: x4 : valueType: LEXER_ID_REF: INT*"),
         ("x5 : INT{1}", "INT", "str", ["INT"], ['x5: str = None'], [("x5", "INT")],
          "pairDef: x5 : valueType: LEXER_ID_REF: INT{1}"),
         ("x6 : INT{1, 1}", "INT", "str", ["INT"], ['x6: str = None'], [("x6", "INT")],
          "pairDef: x6 : valueType: LEXER_ID_REF: INT{1,1}"),
         ("x7 : INT{1,}", "jsg.ArrayFactory('{name}', _CONTEXT, INT, 1, None)",
          "typing.List[str]", ["INT"], ['x7: typing.List[str] = None'],
          [("x7", "jsg.ArrayFactory('x7', _CONTEXT, INT, 1, None)")],
          "pairDef: x7 : valueType: LEXER_ID_REF: INT{1,}")]

initializers = {
    "x1 : INT": ['self.x1 = x1'],
    "x2 : INT?": ['self.x2 = x2'],
    "x3 : INT+": ["self.x3 = x3"],
    "x4 : INT*": ["self.x4 = x4"],
    "x5 : INT{1}": ['self.x5 = x5'],
    "x6 : INT{1, 1}": ['self.x6 = x6'],
    "x7 : INT{1,}": ["self.x7 = x7"]
}

builtins = [("k : @string", ["k: str = None"], ['self.k = k'],
             'pairDef: k : valueType: builtinValueType: @string')]


@pytest.mark.parametrize("text,sig,py,deps,sigs,memins,v", tests, ids=[t[0] for t in tests])
def test_simple_pairdef(text, sig, py, deps, sigs, memins, v):
    t = cast(JSGPairDef, parse(text, "pairDef", JSGPairDef))
    assert str(t) == v
    assert t.signature_type() == sig, text
    assert t.python_type() == py, text
    assert t.dependency_list() == deps, text
    assert t.signatures() == sigs, text
    assert t.members_entries() == memins, text
    assert t.initializers() == initializers[text]


def test_odd_identifiers():
    t = cast(JSGPairDef, parse("'String' : INT", "pairDef", JSGPairDef))
    assert str(t) == 'pairDef: String : valueType: LEXER_ID_REF: INT'
    assert t.members_entries() == [('String', 'INT')]
    assert t.members_entries(True) == [('String', 'typing.Optional[INT]')]
    assert t.signatures() == ['String: str = None']
    assert t.initializers() == ['self.String = String']

    t = cast(JSGPairDef, parse("'def' : INT", "pairDef", JSGPairDef))
    assert str(t) == 'pairDef: def : valueType: LEXER_ID_REF: INT'
    assert t.members_entries() == [('def', 'INT')]
    assert t.signatures() == ['def_: str = None']
    assert t.initializers() == ["setattr(self, 'def', def_ if def_ is not None else _kwargs.get('def', None))"]

    t = cast(JSGPairDef, parse("'a var' : @number", "pairDef", JSGPairDef))
    assert str(t) == "pairDef: a var : valueType: builtinValueType: @number"
    assert t.members_entries() == [('a var', 'jsg.Number')]
    assert t.signatures() == []
    assert t.initializers() == ["setattr(self, 'a var', _kwargs.get('a var', None))"]


def test_pairdef_shorthand():
    text = "(x1 'v 2' 'class') : @number {3,17}"
    t = cast(JSGPairDef, parse(text, "pairDef", JSGPairDef))
    assert t.signatures() == ['x1: typing.List[float] = None', 'class_: typing.List[float] = None']
    assert t.initializers() == [
        'self.x1 = x1',
        "setattr(self, 'v 2', _kwargs.get('v 2', None))",
        "setattr(self, 'class', class_ if class_ is not None else _kwargs.get('class', None))"]
    assert str(t) == "pairDef: (x1 | v 2 | class) : valueType: builtinValueType: @number{3,17}"
    assert t.dependency_list() == []

    text = "(x1 'v 2' 'class') : @bool ?"
    t = cast(JSGPairDef, parse(text, "pairDef", JSGPairDef))
    assert t.signatures() == ['x1: typing.Optional[bool] = None', 'class_: typing.Optional[bool] = None']
    assert t.initializers() == [
        'self.x1 = x1',
        "setattr(self, 'v 2', _kwargs.get('v 2', None))",
        "setattr(self, 'class', class_ if class_ is not None else _kwargs.get('class', None))"]
    assert str(t) == "pairDef: (x1 | v 2 | class) : valueType: builtinValueType: @bool?"
    assert t.dependency_list() == []
    assert t.members_entries() == [('x1', 'typing.Optional[jsg.Boolean]'),
                                    ('v 2', 'typing.Optional[jsg.Boolean]'),
                                    ('class', 'typing.Optional[jsg.Boolean]')]

    text = "(x1 'v 2' 'class') : @null"
    t = cast(JSGPairDef, parse(text, "pairDef", JSGPairDef))
    assert t.signatures() == ['x1: type(None) = jsg.Empty', 'class_: type(None) = jsg.Empty']
    assert t.initializers() == [
        'self.x1 = x1',
        "setattr(self, 'v 2', _kwargs.get('v 2', jsg.Empty))",
        "setattr(self, 'class', class_ if class_ is not jsg.Empty else _kwargs.get('class', jsg.Empty))"]
    assert str(t) == "pairDef: (x1 | v 2 | class) : valueType: builtinValueType: @null"
    assert t.dependency_list() == []
    assert t.members_entries() == [('x1', 'jsg.JSGNull'), ('v 2', 'jsg.JSGNull'), ('class', 'jsg.JSGNull')]

    text = "(def 'v 2' class) : @null"
    t = cast(JSGPairDef, parse(text, "pairDef", JSGPairDef))
    assert t.initializers() == [
        "setattr(self, 'def', def_ if def_ is not jsg.Empty else _kwargs.get('def', jsg.Empty))",
        "setattr(self, 'v 2', _kwargs.get('v 2', jsg.Empty))",
        "setattr(self, 'class', class_ if class_ is not jsg.Empty else _kwargs.get('class', jsg.Empty))"]


def test_pairdef_valuetype_ref():
    text = "nonobj = {a:@string b:@number?};  obj = {nonobj}"
    t = cast(JSGPairDef, parse(text, "grammarElt", JSGPairDef))
    assert t.signatures() == ['a: typing.Optional[float] = None', 'b: typing.Optional[float] = None']


@pytest.mark.parametrize("text,sig,init,s", builtins, ids=[b[0] for b in builtins])
def test_pairdef_builtins(text, sig, init, s):
    t = cast(JSGPairDef, parse(text, "pairDef", JSGPairDef))
    assert t.signatures() == sig
    assert t.initializers() == init
    assert str(t) == s
    assert t.dependency_list() == []
    assert t.members_entries() == [('k', 'jsg.String')]


def test_pairdef_reference():
    text = """
Patient {name: @string+ age: @int}
b {Patient*}
"""
    d = cast(JSGDocParser, parse(text, "doc", JSGDocParser))
    assert d is not None
    t = d._context.reference('b')
    assert str(t) == 'objectExpr: simple object'
    assert t.signatures() == ['name: typing.List[str] = None', 'age: int = None']
    assert t.initializers() == ['self.name = name', 'self.age = age']
    assert t.dependency_list() == ['Patient']
    assert t.members_entries() == [
        ('name', "jsg.ArrayFactory('name', _CONTEXT, jsg.ArrayFactory('name', _CONTEXT, jsg.String, 1, None), 0, None)"),
        ('age', "jsg.ArrayFactory('age', _CONTEXT, jsg.Integer, 0, None)")]
    assert t.mt_value() == 'None'
