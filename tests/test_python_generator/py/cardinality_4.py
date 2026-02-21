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
    _members = {'l23 38n': jsg.ArrayFactory('l23 38n', _CONTEXT, jsg.ArrayFactory('l23 38n', _CONTEXT, jsg.String, 2, 8), 2, 3)}
    _strict = True

    def __init__(self,
                 **_kwargs: dict[str, object]):
        super().__init__(_CONTEXT, **_kwargs)
        setattr(self, 'l23 38n', _kwargs.get('l23 38n', None))


_CONTEXT.NAMESPACE = locals()
