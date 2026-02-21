# Auto generated from JSGPython by PyJSG version 0.8b1
# Generation date: 2018-07-31 12:55
#
import typing
import pyjsg.jsglib as jsg

# .TYPE and .IGNORE settings
_CONTEXT = jsg.JSGContext()
_CONTEXT.TYPE_EXCEPTIONS.append("Shape")


class IRIREF(jsg.JSGString):
    pattern = jsg.JSGPattern(r'[A-Z]+')


class BNODE(jsg.JSGString):
    pattern = jsg.JSGPattern(r'_:[A-Z]+')


shapeExprLabel = typing.Union[IRIREF, BNODE]


class Shape(jsg.JSGObject):
    _reference_types = []
    _members = {'id': typing.Optional[shapeExprLabel]}
    _strict = True

    def __init__(self,
                 id: typing.Optional[str] = None,
                 **_kwargs: dict[str, object]):
        super().__init__(_CONTEXT, **_kwargs)
        self.id = id


_CONTEXT.NAMESPACE = locals()
