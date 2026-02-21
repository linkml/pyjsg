import typing
import pyjsg.jsglib as jsg

# .TYPE and .IGNORE settings
_CONTEXT = jsg.JSGContext()
_CONTEXT.TYPE_EXCEPTIONS.append("EachOf")
_CONTEXT.TYPE_EXCEPTIONS.append("TripleConstraint")
_CONTEXT.TYPE_EXCEPTIONS.append("OneOf")


class _Anon1(jsg.JSGString):
    pattern = jsg.JSGPattern(r'unbounded')


class IRI(jsg.String):
    pattern = jsg.JSGPattern(r'')


class BNODE(jsg.String):
    pattern = jsg.JSGPattern(r'')


class INTEGER(jsg.String):
    pattern = jsg.JSGPattern(r'')


class EachOf(jsg.JSGObject):
    _reference_types = []
    _members = {}
    _strict = True

    def __init__(self,
                 **_kwargs: dict[str, object]):
        super().__init__(_CONTEXT, **_kwargs)



class TripleConstraint(jsg.JSGObject):
    _reference_types = []
    _members = {}
    _strict = True

    def __init__(self,
                 **_kwargs: dict[str, object]):
        super().__init__(_CONTEXT, **_kwargs)



tripleExprLabel = typing.Union[IRI, BNODE]


tripleExpr = typing.Union[EachOf, "OneOf", typing.Union[IRI, BNODE]]


class OneOf(jsg.JSGObject):
    _reference_types = []
    _members = {'id': typing.Optional[tripleExprLabel],
                'expressions': jsg.ArrayFactory('expressions', _CONTEXT, typing.Union[EachOf, "OneOf", typing.Union[IRI, BNODE]], 2, None),
                'min': typing.Optional[INTEGER],
                'max': typing.Optional[typing.Union[_Anon1, INTEGER]]}
    _strict = True

    def __init__(self,
                 id: typing.Optional[typing.Union[str, str]] = None,
                 expressions: list[typing.Union[EachOf, "OneOf", typing.Union[str, str]]] = None,
                 min: typing.Optional[str] = None,
                 max: typing.Optional[typing.Union[str, str]] = None,
                 **_kwargs: dict[str, object]):
        super().__init__(_CONTEXT, **_kwargs)
        self.id = id
        self.expressions = expressions
        self.min = min
        self.max = max


_CONTEXT.NAMESPACE = locals()
