import pytest
from dataclasses import dataclass
from typing import cast, List, Tuple, Optional

from pyjsg.parser_impl.jsg_doc_parser import JSGDocParser
from pyjsg.parser_impl.jsg_objectexpr_parser import JSGObjectExpr
from tests.test_basics.parser import parse


@dataclass
class DataTestEntry:
    text: str
    name: str
    deps: list[str]
    sigs: list[str]
    membs: list[Tuple[str, str]]
    inits: list[str]

    @staticmethod
    def gen_entry(t: JSGObjectExpr, text: Optional[str] = None) -> str:
        return str(DataTestEntry(text if text else t.text, str(t),
                             t.dependency_list(), t.signatures(), t.members_entries(), t.initializers()))


i0 = DataTestEntry(text='a {}', name='objectExpr: simple object', deps=[], sigs=[], membs=[], inits=[])
i1 = DataTestEntry(text='a {,}', name='objectExpr: simple object', deps=[], sigs=[], membs=[], inits=[])
i2 = DataTestEntry(text='a {a: @int}', name='objectExpr: simple object', deps=[], sigs=['a: int = None'],
               membs=[('a', 'jsg.Integer')], inits=['self.a = a'])
i3 = DataTestEntry(text='a {b: .}', name='objectExpr: simple object', deps=[], sigs=['b: object = jsg.Empty'],
               membs=[('b', "jsg.AnyTypeFactory('b', _CONTEXT)")], inits=['self.b = b'])
i4 = DataTestEntry(text='a {b: .? c: . d: .* e: .+ f: a}',
               name='objectExpr: simple object',
               deps=['a'],
               sigs=['b: typing.Optional[object] = jsg.Empty', 'c: object = jsg.Empty',
                     'd: list[object] = None',
                     'e: list[object] = None', 'f: a = None'],
               membs=[('b', "typing.Optional[jsg.AnyTypeFactory('b', _CONTEXT)]"),
                      ('c', "jsg.AnyTypeFactory('c', _CONTEXT)"),
                      ('d', "jsg.ArrayFactory('d', _CONTEXT, jsg.AnyTypeFactory('d', _CONTEXT), 0, None)"),
                      ('e', "jsg.ArrayFactory('e', _CONTEXT, jsg.AnyTypeFactory('e', _CONTEXT), 1, None)"),
                      ('f', 'a')],
               inits=['self.b = b', 'self.c = c', "self.d = d", "self.e = e", 'self.f = f'])
i5 = DataTestEntry(text='a {b: @int c:@string |, }',
               name='objectExpr: object choices',
               deps=['a_1_', 'a_2_'],
               sigs=['opts_: typing.Union[a_1_, a_2_] = None'],
               membs=[('b', 'typing.Optional[jsg.Integer]'), ('c', 'typing.Optional[jsg.String]')],
               inits=['if opts_ is not None:', '    if isinstance(opts_, a_1_):', '        self.b = opts_.b',
                      '        self.c = opts_.c', '    elif isinstance(opts_, a_2_):', '        pass', '    else:',
                      '        raise ValueError(f"Unrecognized value type: {opts_}")'])
i6 = DataTestEntry(text='a {b: . | c: .}',
               name='objectExpr: object choices',
               deps=['a_1_', 'a_2_'],
               sigs=['opts_: typing.Union[a_1_, a_2_] = None'],
               membs=[('b', "typing.Optional[jsg.AnyTypeFactory('b', _CONTEXT)]"),
                      ('c', "typing.Optional[jsg.AnyTypeFactory('c', _CONTEXT)]")],
               inits=['if opts_ is not None:', '    if isinstance(opts_, a_1_):', '        self.b = opts_.b',
                      '    elif isinstance(opts_, a_2_):', '        self.c = opts_.c', '    else:',
                      '        raise ValueError(f"Unrecognized value type: {opts_}")'])
i7 = DataTestEntry(text='a {b: .? c: . | d: .*, e: .+ | f: a, }',
               name='objectExpr: object choices',
               deps=['a_1_', 'a_2_', 'a', 'a_3_'],
               sigs=['opts_: typing.Union[a_1_, a_2_, a_3_] = None'],
               membs=[('b', "typing.Optional[jsg.AnyTypeFactory('b', _CONTEXT)]"),
                      ('c', "typing.Optional[jsg.AnyTypeFactory('c', _CONTEXT)]"),
                      ('d', "typing.Optional[jsg.ArrayFactory('d', _CONTEXT, jsg.AnyTypeFactory('d', _CONTEXT), 0, None)]"),
                      ('e', "typing.Optional[jsg.ArrayFactory('e', _CONTEXT, jsg.AnyTypeFactory('e', _CONTEXT), 1, None)]"),
                      ('f', 'typing.Optional[a]')],
               inits=['if opts_ is not None:', '    if isinstance(opts_, a_1_):', '        self.b = opts_.b',
                      '        self.c = opts_.c', '    elif isinstance(opts_, a_2_):', '        self.d = opts_.d',
                      '        self.e = opts_.e', '    elif isinstance(opts_, a_3_):', '        self.f = opts_.f',
                      '    else:',
                      '        raise ValueError(f"Unrecognized value type: {opts_}")'])

o0 = DataTestEntry(text='{}', name='objectExpr: simple object', deps=[], sigs=[], membs=[], inits=[])
o1 = DataTestEntry(text='{,}', name='objectExpr: simple object', deps=[], sigs=[], membs=[], inits=[])
o2 = DataTestEntry(text='{a: @int}', name='objectExpr: simple object', deps=[], sigs=['a: int = None'],
               membs=[('a', 'jsg.Integer')], inits=['self.a = a'])
o3 = DataTestEntry(text='{b: .}', name='objectExpr: simple object', deps=[], sigs=['b: object = jsg.Empty'],
               membs=[('b', "jsg.AnyTypeFactory('b', _CONTEXT)")], inits=['self.b = b'])
o4 = DataTestEntry(text='{b: .? c: . d: .* e: .+ f: a}',
               name='objectExpr: simple object',
               deps=['a'],
               sigs=['b: typing.Optional[object] = jsg.Empty', 'c: object = jsg.Empty',
                     'd: list[object] = None',
                     'e: list[object] = None', 'f: Undefined(a) = None'],
               membs=[('b', "typing.Optional[jsg.AnyTypeFactory('b', _CONTEXT)]"),
                      ('c', "jsg.AnyTypeFactory('c', _CONTEXT)"),
                      ('d', "jsg.ArrayFactory('d', _CONTEXT, jsg.AnyTypeFactory('d', _CONTEXT), 0, None)"),
                      ('e', "jsg.ArrayFactory('e', _CONTEXT, jsg.AnyTypeFactory('e', _CONTEXT), 1, None)"),
                      ('f', 'Undefined(a)')],
               inits=['self.b = b', 'self.c = c', "self.d = d", "self.e = e", 'self.f = f'])
o5 = DataTestEntry(text='{b: @int c:@string |, }',
               name='objectExpr: object choices',
               deps=['_Anon1_1_', '_Anon1_2_'],
               sigs=['opts_: typing.Union[_Anon1_1_, _Anon1_2_] = None'],
               membs=[('b', 'typing.Optional[jsg.Integer]'), ('c', 'typing.Optional[jsg.String]')],
               inits=['if opts_ is not None:', '    if isinstance(opts_, _Anon1_1_):', '        self.b = opts_.b',
                      '        self.c = opts_.c', '    elif isinstance(opts_, _Anon1_2_):', '        pass', '    else:',
                      '        raise ValueError(f"Unrecognized value type: {opts_}")'])
o6 = DataTestEntry(text='{b: . | c: .}',
               name='objectExpr: object choices',
               deps=['_Anon1_1_', '_Anon1_2_'],
               sigs=['opts_: typing.Union[_Anon1_1_, _Anon1_2_] = None'],
               membs=[('b', "typing.Optional[jsg.AnyTypeFactory('b', _CONTEXT)]"),
                      ('c', "typing.Optional[jsg.AnyTypeFactory('c', _CONTEXT)]")],
               inits=['if opts_ is not None:', '    if isinstance(opts_, _Anon1_1_):', '        self.b = opts_.b',
                      '    elif isinstance(opts_, _Anon1_2_):', '        self.c = opts_.c', '    else:',
                      '        raise ValueError(f"Unrecognized value type: {opts_}")'])
o7 = DataTestEntry(text='{b: .? c: . | d: .*, e: .+ | f: a, }',
               name='objectExpr: object choices',
               deps=['_Anon1_1_', '_Anon1_2_', 'a', '_Anon1_3_'],
               sigs=['opts_: typing.Union[_Anon1_1_, _Anon1_2_, _Anon1_3_] = None'],
               membs=[('b', "typing.Optional[jsg.AnyTypeFactory('b', _CONTEXT)]"),
                      ('c', "typing.Optional[jsg.AnyTypeFactory('c', _CONTEXT)]"),
                      ('d', "typing.Optional[jsg.ArrayFactory('d', _CONTEXT, jsg.AnyTypeFactory('d', _CONTEXT), 0, None)]"),
                      ('e', "typing.Optional[jsg.ArrayFactory('e', _CONTEXT, jsg.AnyTypeFactory('e', _CONTEXT), 1, None)]"),
                      ('f', 'typing.Optional[Undefined(a)]')],
               inits=['if opts_ is not None:', '    if isinstance(opts_, _Anon1_1_):', '        self.b = opts_.b',
                      '        self.c = opts_.c', '    elif isinstance(opts_, _Anon1_2_):', '        self.d = opts_.d',
                      '        self.e = opts_.e', '    elif isinstance(opts_, _Anon1_3_):', '        self.f = opts_.f',
                      '    else:',
                      '        raise ValueError(f"Unrecognized value type: {opts_}")'])

test_entries: list[Tuple[str, DataTestEntry, DataTestEntry]] = [
    ('{}', i0, o0),
    ('{,}', i1, o1),
    ('{a: @int}', i2, o2),
    ('{b: .}', i3, o3),
    ('{b: .? c: . d: .* e: .+ f: a}', i4, o4),
    ('{b: @int c:@string |, }', i5, o5),
    ('{b: . | c: .}', i6, o6),
    ('{b: .? c: . | d: .*, e: .+ | f: a, }', i7, o7),
]


def test_mt_value():
    d = cast(JSGDocParser, parse('a ' + test_entries[0][0], "objectDef", JSGDocParser))
    t = d._context.reference('a')
    assert t.mt_value() == "None"


@pytest.mark.parametrize("expr,e,_", test_entries, ids=[te[0] for te in test_entries])
def test_basics(expr, e, _):
    text = "a " + expr
    d = cast(JSGDocParser, parse(text, "objectDef", JSGDocParser))
    assert d is not None, f"Parse error: {text}"
    t = d._context.reference('a')
    assert str(t) == e.name
    assert t.signature_type() == 'a', text
    assert t.python_type() == 'a', text
    assert t.dependency_list() == e.deps, text
    assert t.signatures() == e.sigs, text
    assert t.members_entries() == e.membs, text
    assert t.initializers() == e.inits, text


@pytest.mark.parametrize("expr,_,e", test_entries, ids=[te[0] for te in test_entries])
def test_anonymous_entries(expr, _, e):
    t = cast(JSGObjectExpr, parse(expr, "objectExpr", JSGObjectExpr))
    assert t is not None, f"Parse error: {e.text}"
    assert str(t) == e.name
    assert t.signature_type() == '_Anon1', e.text
    assert t.python_type() == '_Anon1', e.text
    assert t.dependency_list() == e.deps, e.text
    assert t.signatures() == e.sigs, e.text
    assert t.members_entries() == e.membs, e.text
    assert t.initializers() == e.inits, e.text


def test_opt_choice_branch():
    text = '{id: @string |}'
    t = cast(JSGObjectExpr, parse(text, 'objectExpr', JSGObjectExpr))
    assert t is not None, "Parse error"
    assert str(t) == 'objectExpr: object choices'
    assert t.signature_type() == '_Anon1', text
    assert t.python_type() == '_Anon1', text
    assert t.dependency_list() == ['_Anon1_1_', '_Anon1_2_'], text
    assert t.signatures() == ['opts_: typing.Union[_Anon1_1_, _Anon1_2_] = None'], text
    assert t.members_entries() == [('id', 'typing.Optional[jsg.String]')], text
    assert t.initializers() == [
        'if opts_ is not None:',
        '    if isinstance(opts_, _Anon1_1_):',
        '        self.id = opts_.id',
        '    elif isinstance(opts_, _Anon1_2_):',
        '        pass',
        '    else:',
        '        raise ValueError(f"Unrecognized value type: {opts_}")'], text
