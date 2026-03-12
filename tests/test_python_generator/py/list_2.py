# Auto generated from JSGPython by PyJSG version 0.8b1
# Generation date: 2018-07-31 11:33
#
import typing
import pyjsg.jsglib as jsg

# .TYPE and .IGNORE settings
_CONTEXT = jsg.JSGContext()
_CONTEXT.TYPE_EXCEPTIONS.append("l")


class l(jsg.JSGObject):
    _reference_types = []
    _members = {'e': jsg.ArrayFactory('e', _CONTEXT, jsg.String, 1, None)}
    _strict = True

    def __init__(self,
                 e: list[str] = None,
                 **_kwargs: dict[str, object]):
        super().__init__(_CONTEXT, **_kwargs)
        self.e = e


_CONTEXT.NAMESPACE = locals()
