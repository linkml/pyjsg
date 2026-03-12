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
    _members = {'class': jsg.String,
                'def': jsg.Number,
                'import': jsg.Integer,
                'with': jsg.Boolean,
                'if': jsg.JSGNull,
                'else': jsg.ArrayFactory('else', _CONTEXT, jsg.AnyType, 0, None),
                'raise': jsg.ObjectFactory('raise', _CONTEXT, jsg.Object)}
    _strict = True

    def __init__(self,
                 class_: str = None,
                 def_: float = None,
                 import_: int = None,
                 with_: bool = None,
                 if_: type(None) = jsg.Empty,
                 else_: list = None,
                 raise_: object = None,
                 **_kwargs: dict[str, object]):
        super().__init__(_CONTEXT, **_kwargs)
        setattr(self, 'class', class_ if class_ is not None else _kwargs.get('class', None))
        setattr(self, 'def', def_ if def_ is not None else _kwargs.get('def', None))
        setattr(self, 'import', import_ if import_ is not None else _kwargs.get('import', None))
        setattr(self, 'with', with_ if with_ is not None else _kwargs.get('with', None))
        setattr(self, 'if', if_ if if_ is not jsg.Empty else _kwargs.get('if', jsg.Empty))
        setattr(self, 'else', else_ if else_ is not None else _kwargs.get('else', None))
        setattr(self, 'raise', raise_ if raise_ is not None else _kwargs.get('raise', None))



class another_object(jsg.JSGObject):
    _reference_types = []
    _members = {}
    _strict = False

    def __init__(self,
                 **_kwargs: dict[str, object]):
        super().__init__(_CONTEXT, **_kwargs)


_CONTEXT.NAMESPACE = locals()
