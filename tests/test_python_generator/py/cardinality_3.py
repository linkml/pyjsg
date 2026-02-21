# Auto generated from JSGPython by PyJSG version 0.8b1
# Generation date: 2018-07-31 11:27
#
import typing
import pyjsg.jsglib as jsg

# .TYPE and .IGNORE settings
_CONTEXT = jsg.JSGContext()
_CONTEXT.TYPE_EXCEPTIONS.append("doc")


class doc(jsg.JSGObject):
    _reference_types = []
    _members = {'l0nl0n': jsg.ArrayFactory('l0nl0n', _CONTEXT, jsg.ArrayFactory('l0nl0n', _CONTEXT, jsg.AnyTypeFactory('l0nl0n', _CONTEXT), 0, None), 0, None)}
    _strict = True

    def __init__(self,
                 l0nl0n: list[list[object]] = None,
                 **_kwargs: dict[str, object]):
        super().__init__(_CONTEXT, **_kwargs)
        self.l0nl0n = l0nl0n


_CONTEXT.NAMESPACE = locals()
