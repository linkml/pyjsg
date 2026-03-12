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
    _members = {'class': jsg.AnyTypeFactory('class', _CONTEXT)}
    _strict = True

    def __init__(self,
                 class_: object = jsg.Empty,
                 **_kwargs: dict[str, object]):
        super().__init__(_CONTEXT, **_kwargs)
        setattr(self, 'class', class_ if class_ is not jsg.Empty else _kwargs.get('class', jsg.Empty))


_CONTEXT.NAMESPACE = locals()
