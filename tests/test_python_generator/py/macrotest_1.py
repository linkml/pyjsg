# Auto generated from JSGPython by PyJSG version 0.7b2
# Generation date: 2018-07-18 18:06
#
import typing
import pyjsg.jsglib as jsg

# .TYPE and .IGNORE settings
_CONTEXT = jsg.JSGContext()
_CONTEXT.TYPE_EXCEPTIONS.append("Shape")


class Shape(jsg.JSGObject):
    _reference_types = []
    _members = {'id': typing.Optional[typing.Union[jsg.Integer, jsg.String]]}
    _strict = True

    def __init__(self,
                 id: typing.Optional[typing.Union[int, str]] = None,
                 **_kwargs: dict[str, object]):
        super().__init__(_CONTEXT, **_kwargs)
        self.id = id


_CONTEXT.NAMESPACE = locals()
