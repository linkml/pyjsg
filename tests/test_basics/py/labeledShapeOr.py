import typing
import pyjsg.jsglib as jsg

# .TYPE and .IGNORE settings
_CONTEXT = jsg.JSGContext()
_CONTEXT.TYPE_EXCEPTIONS.append("shapeExprLabel")
_CONTEXT.TYPE_EXCEPTIONS.append("labeledShapeOr")


class _Anon1(jsg.JSGString):
    pattern = jsg.JSGPattern(r'ShapeOr')


class SHAPEEXPR(jsg.JSGString):
    pattern = jsg.JSGPattern(r'[a-z]')


class shapeExprLabel(jsg.JSGObject):
    _reference_types = []
    _members = {}
    _strict = True

    def __init__(self,
                 **_kwargs: dict[str, object]):
        super().__init__(_CONTEXT, **_kwargs)



class labeledShapeOr(jsg.JSGObject):
    _reference_types = []
    _members = {'type': _Anon1,
                'id': shapeExprLabel,
                'shapeExprs': jsg.ArrayFactory('shapeExprs', _CONTEXT, SHAPEEXPR, 2, None)}
    _strict = True

    def __init__(self,
                 type: str = None,
                 id: shapeExprLabel = None,
                 shapeExprs: list[str] = None,
                 **_kwargs: dict[str, object]):
        super().__init__(_CONTEXT, **_kwargs)
        self.type = type
        self.id = id
        self.shapeExprs = shapeExprs


_CONTEXT.NAMESPACE = locals()
