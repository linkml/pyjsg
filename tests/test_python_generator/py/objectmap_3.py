# Auto generated from JSGPython by PyJSG version 0.8b1
# Generation date: 2018-07-31 11:32
#
import typing
import pyjsg.jsglib as jsg

# .TYPE and .IGNORE settings
_CONTEXT = jsg.JSGContext()
_CONTEXT.TYPE_EXCEPTIONS.append("Person")
_CONTEXT.TYPE_EXCEPTIONS.append("Directory")


class PNAME(jsg.JSGString):
    pattern = jsg.JSGPattern(r'[A-Z][0-9]+')


class Person(jsg.JSGObject):
    _reference_types = []
    _members = {'name': jsg.String,
                'age': typing.Optional[jsg.Integer]}
    _strict = True

    def __init__(self,
                 name: str = None,
                 age: typing.Optional[int] = None,
                 **_kwargs: dict[str, object]):
        super().__init__(_CONTEXT, **_kwargs)
        self.name = name
        self.age = age



class Directory(jsg.JSGObjectMap):
    _name_filter = PNAME
    _value_type = Person

    def __init__(self,
                 **_kwargs):
        super().__init__(_CONTEXT, **_kwargs)

_CONTEXT.NAMESPACE = locals()
