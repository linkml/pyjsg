import typing
import pyjsg.jsglib as jsg

# .TYPE and .IGNORE settings
_CONTEXT = jsg.JSGContext()
_CONTEXT.TYPE_EXCEPTIONS.append("ShapeExternal")
_CONTEXT.TYPE_EXCEPTIONS.append("NodeConstraint")
_CONTEXT.TYPE_EXCEPTIONS.append("Shape")
_CONTEXT.TYPE_EXCEPTIONS.append("labeledShapeNot")
_CONTEXT.TYPE_EXCEPTIONS.append("ShapeOr")
_CONTEXT.TYPE_EXCEPTIONS.append("ShapeAnd")
_CONTEXT.TYPE_EXCEPTIONS.append("ShapeNot")


class _Anon1(jsg.JSGString):
    pattern = jsg.JSGPattern(r'ShapeNot')


class ShapeExternal(jsg.JSGObject):
    _reference_types = []
    _members = {}
    _strict = True

    def __init__(self,
                 **_kwargs: dict[str, object]):
        super().__init__(_CONTEXT, **_kwargs)



class NodeConstraint(jsg.JSGObject):
    _reference_types = []
    _members = {}
    _strict = True

    def __init__(self,
                 **_kwargs: dict[str, object]):
        super().__init__(_CONTEXT, **_kwargs)



class Shape(jsg.JSGObject):
    _reference_types = []
    _members = {}
    _strict = True

    def __init__(self,
                 **_kwargs: dict[str, object]):
        super().__init__(_CONTEXT, **_kwargs)



shapeExprLabel = jsg.String


class labeledShapeNot(jsg.JSGObject):
    _reference_types = []
    _members = {'type': _Anon1,
                'id': shapeExprLabel,
                'shapeExpr': "shapeExpr"}
    _strict = True

    def __init__(self,
                 type: str = None,
                 id: str = None,
                 shapeExpr: typing.Union["ShapeOr", "ShapeAnd", "ShapeNot", NodeConstraint, Shape, str, ShapeExternal] = None,
                 **_kwargs: dict[str, object]):
        super().__init__(_CONTEXT, **_kwargs)
        self.type = type
        self.id = id
        self.shapeExpr = shapeExpr



labeledShapeExpr = typing.Union[labeledShapeNot, jsg.String]


shapeExpr = typing.Union["ShapeOr", "ShapeAnd", "ShapeNot", NodeConstraint, Shape, jsg.String, ShapeExternal]


class ShapeOr(jsg.JSGObject):
    _reference_types = []
    _members = {'shapeExprs': jsg.ArrayFactory('shapeExprs', _CONTEXT, typing.Union["ShapeOr", "ShapeAnd", "ShapeNot", NodeConstraint, Shape, jsg.String, ShapeExternal], 2, None)}
    _strict = True

    def __init__(self,
                 shapeExprs: list[typing.Union["ShapeOr", "ShapeAnd", "ShapeNot", NodeConstraint, Shape, str, ShapeExternal]] = None,
                 **_kwargs: dict[str, object]):
        super().__init__(_CONTEXT, **_kwargs)
        self.shapeExprs = shapeExprs



class ShapeAnd(jsg.JSGObject):
    _reference_types = []
    _members = {'shapeExprs': jsg.ArrayFactory('shapeExprs', _CONTEXT, typing.Union[ShapeOr, "ShapeAnd", "ShapeNot", NodeConstraint, Shape, jsg.String, ShapeExternal], 2, None)}
    _strict = True

    def __init__(self,
                 shapeExprs: list[typing.Union[ShapeOr, "ShapeAnd", "ShapeNot", NodeConstraint, Shape, str, ShapeExternal]] = None,
                 **_kwargs: dict[str, object]):
        super().__init__(_CONTEXT, **_kwargs)
        self.shapeExprs = shapeExprs



class ShapeNot(jsg.JSGObject):
    _reference_types = []
    _members = {'shapeExpr': shapeExpr}
    _strict = True

    def __init__(self,
                 shapeExpr: typing.Union[ShapeOr, ShapeAnd, "ShapeNot", NodeConstraint, Shape, str, ShapeExternal] = None,
                 **_kwargs: dict[str, object]):
        super().__init__(_CONTEXT, **_kwargs)
        self.shapeExpr = shapeExpr


_CONTEXT.NAMESPACE = locals()
