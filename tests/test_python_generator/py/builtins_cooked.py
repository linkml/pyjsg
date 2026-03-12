# Auto generated from JSGPython by PyJSG version 0.8b1
# Generation date: 2018-07-31 11:31
#
import typing
import pyjsg.jsglib as jsg

# .TYPE and .IGNORE settings
_CONTEXT = jsg.JSGContext()
_CONTEXT.TYPE_EXCEPTIONS.append("doc")
_CONTEXT.TYPE_EXCEPTIONS.append("another_object")


class doc(jsg.JSGObject):
    _reference_types = []
    _members = {'v1': jsg.String,
                'v2': jsg.Number,
                'v3': jsg.Integer,
                'v4': jsg.Boolean,
                'v5': jsg.JSGNull,
                'v6': jsg.ArrayFactory('v6', _CONTEXT, jsg.AnyType, 0, None),
                'v7': jsg.ObjectFactory('v7', _CONTEXT, jsg.Object)}
    _strict = True

    def __init__(self,
                 v1: str = None,
                 v2: float = None,
                 v3: int = None,
                 v4: bool = None,
                 v5: type(None) = jsg.Empty,
                 v6: list = None,
                 v7: object = None,
                 **_kwargs: dict[str, object]):
        super().__init__(_CONTEXT, **_kwargs)
        self.v1 = v1
        self.v2 = v2
        self.v3 = v3
        self.v4 = v4
        self.v5 = v5
        self.v6 = v6
        self.v7 = v7



class another_object(jsg.JSGObject):
    _reference_types = []
    _members = {}
    _strict = False

    def __init__(self,
                 **_kwargs: dict[str, object]):
        super().__init__(_CONTEXT, **_kwargs)


_CONTEXT.NAMESPACE = locals()
