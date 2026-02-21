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
    _members = {'v 1': jsg.String,
                'v 2': jsg.Number,
                'v 3': jsg.Integer,
                'v 4': jsg.Boolean,
                'v 5': jsg.JSGNull,
                'v 6': jsg.ArrayFactory('v 6', _CONTEXT, jsg.AnyType, 0, None),
                'v 7': jsg.ObjectFactory('v 7', _CONTEXT, jsg.Object)}
    _strict = True

    def __init__(self,
                 **_kwargs: dict[str, object]):
        super().__init__(_CONTEXT, **_kwargs)
        setattr(self, 'v 1', _kwargs.get('v 1', None))
        setattr(self, 'v 2', _kwargs.get('v 2', None))
        setattr(self, 'v 3', _kwargs.get('v 3', None))
        setattr(self, 'v 4', _kwargs.get('v 4', None))
        setattr(self, 'v 5', _kwargs.get('v 5', jsg.Empty))
        setattr(self, 'v 6', _kwargs.get('v 6', None))
        setattr(self, 'v 7', _kwargs.get('v 7', None))



class another_object(jsg.JSGObject):
    _reference_types = []
    _members = {}
    _strict = False

    def __init__(self,
                 **_kwargs: dict[str, object]):
        super().__init__(_CONTEXT, **_kwargs)


_CONTEXT.NAMESPACE = locals()
