import typing
import pyjsg.jsglib as jsg

# .TYPE and .IGNORE settings
_CONTEXT = jsg.JSGContext()
_CONTEXT.TYPE_EXCEPTIONS.append("Wildcard")
_CONTEXT.TYPE_EXCEPTIONS.append("ObjectLiteral")
_CONTEXT.TYPE_EXCEPTIONS.append("Stem")
_CONTEXT.TYPE_EXCEPTIONS.append("StemRange")


class IRI(jsg.String):
    pattern = jsg.JSGPattern(r'')


class Wildcard(jsg.JSGObject):
    _reference_types = []
    _members = {}
    _strict = True

    def __init__(self,
                 **_kwargs: dict[str, object]):
        super().__init__(_CONTEXT, **_kwargs)



class ObjectLiteral(jsg.JSGObject):
    _reference_types = []
    _members = {'value': jsg.String,
                'language': typing.Optional[jsg.String],
                'type': typing.Optional[jsg.String]}
    _strict = True

    def __init__(self,
                 value: str = None,
                 language: typing.Optional[str] = None,
                 type: typing.Optional[str] = None,
                 **_kwargs: dict[str, object]):
        super().__init__(_CONTEXT, **_kwargs)
        self.value = value
        self.language = language
        self.type = type



objectValue = typing.Union[IRI, ObjectLiteral]


class Stem(jsg.JSGObject):
    _reference_types = []
    _members = {'stem': IRI}
    _strict = True

    def __init__(self,
                 stem: str = None,
                 **_kwargs: dict[str, object]):
        super().__init__(_CONTEXT, **_kwargs)
        self.stem = stem



class StemRange(jsg.JSGObject):
    _reference_types = []
    _members = {'stem': typing.Union[IRI, Wildcard],
                'exclusions': typing.Optional[jsg.ArrayFactory('exclusions', _CONTEXT, typing.Union[typing.Union[IRI, ObjectLiteral], Stem], 1, None)]}
    _strict = True

    def __init__(self,
                 stem: typing.Union[str, Wildcard] = None,
                 exclusions: typing.Optional[list[typing.Union[typing.Union[str, ObjectLiteral], Stem]]] = None,
                 **_kwargs: dict[str, object]):
        super().__init__(_CONTEXT, **_kwargs)
        self.stem = stem
        self.exclusions = exclusions


_CONTEXT.NAMESPACE = locals()
