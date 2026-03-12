import typing
import pyjsg.jsglib as jsg

# .TYPE and .IGNORE settings
_CONTEXT = jsg.JSGContext()
_CONTEXT.TYPE_EXCEPTIONS.append("labeledShapeOr")
_CONTEXT.TYPE_EXCEPTIONS.append("labeledShapeAnd")
_CONTEXT.TYPE_EXCEPTIONS.append("labeledShapeNot")
_CONTEXT.TYPE_EXCEPTIONS.append("labeledNodeConstraint")
_CONTEXT.TYPE_EXCEPTIONS.append("labeledShape")
_CONTEXT.TYPE_EXCEPTIONS.append("shapeExprLabel")
_CONTEXT.TYPE_EXCEPTIONS.append("labeledShapeExternal")
_CONTEXT.TYPE_EXCEPTIONS.append("expr_1_")
_CONTEXT.TYPE_EXCEPTIONS.append("expr_2_")
_CONTEXT.TYPE_EXCEPTIONS.append("expr_3_")
_CONTEXT.TYPE_EXCEPTIONS.append("expr_4_")
_CONTEXT.TYPE_EXCEPTIONS.append("expr_5_")
_CONTEXT.TYPE_EXCEPTIONS.append("expr_6_")
_CONTEXT.TYPE_EXCEPTIONS.append("expr_7_")
_CONTEXT.TYPE_EXCEPTIONS.append("expr")


class labeledShapeOr(jsg.JSGObject):
    _reference_types = []
    _members = {}
    _strict = True

    def __init__(self,
                 **_kwargs: dict[str, object]):
        super().__init__(_CONTEXT, **_kwargs)



class labeledShapeAnd(jsg.JSGObject):
    _reference_types = []
    _members = {}
    _strict = True

    def __init__(self,
                 **_kwargs: dict[str, object]):
        super().__init__(_CONTEXT, **_kwargs)



class labeledShapeNot(jsg.JSGObject):
    _reference_types = []
    _members = {}
    _strict = True

    def __init__(self,
                 **_kwargs: dict[str, object]):
        super().__init__(_CONTEXT, **_kwargs)



class labeledNodeConstraint(jsg.JSGObject):
    _reference_types = []
    _members = {}
    _strict = True

    def __init__(self,
                 **_kwargs: dict[str, object]):
        super().__init__(_CONTEXT, **_kwargs)



class labeledShape(jsg.JSGObject):
    _reference_types = []
    _members = {}
    _strict = True

    def __init__(self,
                 **_kwargs: dict[str, object]):
        super().__init__(_CONTEXT, **_kwargs)



class shapeExprLabel(jsg.JSGObject):
    _reference_types = []
    _members = {}
    _strict = True

    def __init__(self,
                 **_kwargs: dict[str, object]):
        super().__init__(_CONTEXT, **_kwargs)



class labeledShapeExternal(jsg.JSGObject):
    _reference_types = []
    _members = {}
    _strict = True

    def __init__(self,
                 **_kwargs: dict[str, object]):
        super().__init__(_CONTEXT, **_kwargs)



class expr_1_(jsg.JSGObject):
    _reference_types = [labeledShapeOr]
    _members = {}
    _strict = True

    def __init__(self,
                 **_kwargs: dict[str, object]):
        super().__init__(_CONTEXT, **_kwargs)



class expr_2_(jsg.JSGObject):
    _reference_types = [labeledShapeAnd]
    _members = {}
    _strict = True

    def __init__(self,
                 **_kwargs: dict[str, object]):
        super().__init__(_CONTEXT, **_kwargs)



class expr_3_(jsg.JSGObject):
    _reference_types = [labeledShapeNot]
    _members = {}
    _strict = True

    def __init__(self,
                 **_kwargs: dict[str, object]):
        super().__init__(_CONTEXT, **_kwargs)



class expr_4_(jsg.JSGObject):
    _reference_types = [labeledNodeConstraint]
    _members = {}
    _strict = True

    def __init__(self,
                 **_kwargs: dict[str, object]):
        super().__init__(_CONTEXT, **_kwargs)



class expr_5_(jsg.JSGObject):
    _reference_types = [labeledShape]
    _members = {}
    _strict = True

    def __init__(self,
                 **_kwargs: dict[str, object]):
        super().__init__(_CONTEXT, **_kwargs)



class expr_6_(jsg.JSGObject):
    _reference_types = [shapeExprLabel]
    _members = {}
    _strict = True

    def __init__(self,
                 **_kwargs: dict[str, object]):
        super().__init__(_CONTEXT, **_kwargs)



class expr_7_(jsg.JSGObject):
    _reference_types = [labeledShapeExternal]
    _members = {}
    _strict = True

    def __init__(self,
                 **_kwargs: dict[str, object]):
        super().__init__(_CONTEXT, **_kwargs)



class expr(jsg.JSGObject):
    _reference_types = [expr_1_, expr_2_, expr_3_, expr_4_, expr_5_, expr_6_, expr_7_]
    _members = {}
    _strict = True

    def __init__(self,
                 opts_: typing.Union[expr_1_, expr_2_, expr_3_, expr_4_, expr_5_, expr_6_, expr_7_] = None,
                 **_kwargs: dict[str, object]):
        super().__init__(_CONTEXT, **_kwargs)
        if opts_ is not None:
            if isinstance(opts_, expr_1_):
                pass
            elif isinstance(opts_, expr_2_):
                pass
            elif isinstance(opts_, expr_3_):
                pass
            elif isinstance(opts_, expr_4_):
                pass
            elif isinstance(opts_, expr_5_):
                pass
            elif isinstance(opts_, expr_6_):
                pass
            elif isinstance(opts_, expr_7_):
                pass
            else:
                raise ValueError(f"Unrecognized value type: {opts_}")


_CONTEXT.NAMESPACE = locals()
