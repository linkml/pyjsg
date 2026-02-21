# Auto generated from JSGPython by PyJSG version 0.8b1
# Generation date: 2018-07-31 12:20
#
import typing
import pyjsg.jsglib as jsg

# .TYPE and .IGNORE settings
_CONTEXT = jsg.JSGContext()
_CONTEXT.TYPE_EXCEPTIONS.append("doc")


class doc(jsg.JSGObject):
    _reference_types = []
    _members = {'A 1': jsg.AnyTypeFactory('A 1', _CONTEXT)}
    _strict = True

    def __init__(self,
                 **_kwargs: dict[str, object]):
        super().__init__(_CONTEXT, **_kwargs)
        setattr(self, 'A 1', _kwargs.get('A 1', jsg.Empty))


_CONTEXT.NAMESPACE = locals()
