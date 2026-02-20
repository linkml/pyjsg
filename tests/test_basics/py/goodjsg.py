import typing
import pyjsg.jsglib as jsg

# .TYPE and .IGNORE settings
_CONTEXT = jsg.JSGContext()
_CONTEXT.TYPE_EXCEPTIONS.append("optFacet")
_CONTEXT.TYPE_EXCEPTIONS.append("reqFacet")
_CONTEXT.TYPE_EXCEPTIONS.append("listFacet")
_CONTEXT.TYPE_EXCEPTIONS.append("optOpt")
_CONTEXT.TYPE_EXCEPTIONS.append("optReq")
_CONTEXT.TYPE_EXCEPTIONS.append("optList")
_CONTEXT.TYPE_EXCEPTIONS.append("reqOpt")
_CONTEXT.TYPE_EXCEPTIONS.append("reqReq")
_CONTEXT.TYPE_EXCEPTIONS.append("reqList")
_CONTEXT.TYPE_EXCEPTIONS.append("listOpt")
_CONTEXT.TYPE_EXCEPTIONS.append("listReq")
_CONTEXT.TYPE_EXCEPTIONS.append("listList")


class INTEGER(jsg.JSGString):
    pattern = jsg.JSGPattern(r'[0-9]*')


class DECIMAL(jsg.JSGString):
    pattern = jsg.JSGPattern(r'[0-9]*')


class DOUBLE(jsg.JSGString):
    pattern = jsg.JSGPattern(r'[0-9]*')


class STRING(jsg.JSGString):
    pattern = jsg.JSGPattern(r'[a-z]*')


numericLiteral = typing.Union[INTEGER, DECIMAL, DOUBLE]


class optFacet(jsg.JSGObject):
    _reference_types = []
    _members = {'mininclusive': typing.Optional[numericLiteral],
                'minexclusive': typing.Optional[numericLiteral],
                'maxinclusive': typing.Optional[numericLiteral],
                'maxexclusive': typing.Optional[numericLiteral]}
    _strict = True

    def __init__(self,
                 mininclusive: typing.Optional[typing.Union[str, str, str]] = None,
                 minexclusive: typing.Optional[typing.Union[str, str, str]] = None,
                 maxinclusive: typing.Optional[typing.Union[str, str, str]] = None,
                 maxexclusive: typing.Optional[typing.Union[str, str, str]] = None,
                 **_kwargs: typing.dict[str, object]):
        super().__init__(_CONTEXT, **_kwargs)
        self.mininclusive = mininclusive
        self.minexclusive = minexclusive
        self.maxinclusive = maxinclusive
        self.maxexclusive = maxexclusive



class reqFacet(jsg.JSGObject):
    _reference_types = []
    _members = {'mininclusive': numericLiteral,
                'minexclusive': numericLiteral,
                'maxinclusive': numericLiteral,
                'maxexclusive': numericLiteral}
    _strict = True

    def __init__(self,
                 mininclusive: typing.Union[str, str, str] = None,
                 minexclusive: typing.Union[str, str, str] = None,
                 maxinclusive: typing.Union[str, str, str] = None,
                 maxexclusive: typing.Union[str, str, str] = None,
                 **_kwargs: typing.dict[str, object]):
        super().__init__(_CONTEXT, **_kwargs)
        self.mininclusive = mininclusive
        self.minexclusive = minexclusive
        self.maxinclusive = maxinclusive
        self.maxexclusive = maxexclusive



class listFacet(jsg.JSGObject):
    _reference_types = []
    _members = {'mininclusive': jsg.ArrayFactory('mininclusive', _CONTEXT, numericLiteral, 0, None),
                'minexclusive': jsg.ArrayFactory('minexclusive', _CONTEXT, numericLiteral, 0, None),
                'maxinclusive': jsg.ArrayFactory('maxinclusive', _CONTEXT, numericLiteral, 0, None),
                'maxexclusive': jsg.ArrayFactory('maxexclusive', _CONTEXT, numericLiteral, 0, None)}
    _strict = True

    def __init__(self,
                 mininclusive: typing.List[typing.Union[str, str, str]] = None,
                 minexclusive: typing.List[typing.Union[str, str, str]] = None,
                 maxinclusive: typing.List[typing.Union[str, str, str]] = None,
                 maxexclusive: typing.List[typing.Union[str, str, str]] = None,
                 **_kwargs: typing.dict[str, object]):
        super().__init__(_CONTEXT, **_kwargs)
        self.mininclusive = mininclusive
        self.minexclusive = minexclusive
        self.maxinclusive = maxinclusive
        self.maxexclusive = maxexclusive



class optOpt(jsg.JSGObject):
    _reference_types = [optFacet]
    _members = {'first': typing.Optional[INTEGER],
                'mininclusive': typing.Optional[numericLiteral],
                'minexclusive': typing.Optional[numericLiteral],
                'maxinclusive': typing.Optional[numericLiteral],
                'maxexclusive': typing.Optional[numericLiteral],
                'last': jsg.ArrayFactory('last', _CONTEXT, STRING, 1, None)}
    _strict = True

    def __init__(self,
                 first: typing.Optional[str] = None,
                 mininclusive: typing.Optional[typing.Union[str, str, str]] = None,
                 minexclusive: typing.Optional[typing.Union[str, str, str]] = None,
                 maxinclusive: typing.Optional[typing.Union[str, str, str]] = None,
                 maxexclusive: typing.Optional[typing.Union[str, str, str]] = None,
                 last: typing.List[str] = None,
                 **_kwargs: typing.dict[str, object]):
        super().__init__(_CONTEXT, **_kwargs)
        self.first = first
        self.mininclusive = mininclusive
        self.minexclusive = minexclusive
        self.maxinclusive = maxinclusive
        self.maxexclusive = maxexclusive
        self.last = last



class optReq(jsg.JSGObject):
    _reference_types = [optFacet]
    _members = {'first': jsg.Integer,
                'mininclusive': typing.Optional[numericLiteral],
                'minexclusive': typing.Optional[numericLiteral],
                'maxinclusive': typing.Optional[numericLiteral],
                'maxexclusive': typing.Optional[numericLiteral],
                'last': jsg.String}
    _strict = True

    def __init__(self,
                 first: int = None,
                 mininclusive: typing.Optional[typing.Union[str, str, str]] = None,
                 minexclusive: typing.Optional[typing.Union[str, str, str]] = None,
                 maxinclusive: typing.Optional[typing.Union[str, str, str]] = None,
                 maxexclusive: typing.Optional[typing.Union[str, str, str]] = None,
                 last: str = None,
                 **_kwargs: typing.dict[str, object]):
        super().__init__(_CONTEXT, **_kwargs)
        self.first = first
        self.mininclusive = mininclusive
        self.minexclusive = minexclusive
        self.maxinclusive = maxinclusive
        self.maxexclusive = maxexclusive
        self.last = last



class optList(jsg.JSGObject):
    _reference_types = [optFacet]
    _members = {'first': jsg.ArrayFactory('first', _CONTEXT, INTEGER, 0, None),
                'mininclusive': jsg.ArrayFactory('mininclusive', _CONTEXT, typing.Optional[numericLiteral], 0, None),
                'minexclusive': jsg.ArrayFactory('minexclusive', _CONTEXT, typing.Optional[numericLiteral], 0, None),
                'maxinclusive': jsg.ArrayFactory('maxinclusive', _CONTEXT, typing.Optional[numericLiteral], 0, None),
                'maxexclusive': jsg.ArrayFactory('maxexclusive', _CONTEXT, typing.Optional[numericLiteral], 0, None),
                'last': jsg.ArrayFactory('last', _CONTEXT, STRING, 0, None)}
    _strict = True

    def __init__(self,
                 first: typing.List[str] = None,
                 mininclusive: typing.Optional[typing.Union[str, str, str]] = None,
                 minexclusive: typing.Optional[typing.Union[str, str, str]] = None,
                 maxinclusive: typing.Optional[typing.Union[str, str, str]] = None,
                 maxexclusive: typing.Optional[typing.Union[str, str, str]] = None,
                 last: typing.List[str] = None,
                 **_kwargs: typing.dict[str, object]):
        super().__init__(_CONTEXT, **_kwargs)
        self.first = first
        self.mininclusive = mininclusive
        self.minexclusive = minexclusive
        self.maxinclusive = maxinclusive
        self.maxexclusive = maxexclusive
        self.last = last



class reqOpt(jsg.JSGObject):
    _reference_types = [reqFacet]
    _members = {'first': typing.Optional[INTEGER],
                'mininclusive': typing.Optional[numericLiteral],
                'minexclusive': typing.Optional[numericLiteral],
                'maxinclusive': typing.Optional[numericLiteral],
                'maxexclusive': typing.Optional[numericLiteral],
                'last': jsg.ArrayFactory('last', _CONTEXT, STRING, 1, None)}
    _strict = True

    def __init__(self,
                 first: typing.Optional[str] = None,
                 mininclusive: typing.Union[str, str, str] = None,
                 minexclusive: typing.Union[str, str, str] = None,
                 maxinclusive: typing.Union[str, str, str] = None,
                 maxexclusive: typing.Union[str, str, str] = None,
                 last: typing.List[str] = None,
                 **_kwargs: typing.dict[str, object]):
        super().__init__(_CONTEXT, **_kwargs)
        self.first = first
        self.mininclusive = mininclusive
        self.minexclusive = minexclusive
        self.maxinclusive = maxinclusive
        self.maxexclusive = maxexclusive
        self.last = last



class reqReq(jsg.JSGObject):
    _reference_types = [reqFacet]
    _members = {'first': jsg.Integer,
                'mininclusive': numericLiteral,
                'minexclusive': numericLiteral,
                'maxinclusive': numericLiteral,
                'maxexclusive': numericLiteral,
                'last': jsg.String}
    _strict = True

    def __init__(self,
                 first: int = None,
                 mininclusive: typing.Union[str, str, str] = None,
                 minexclusive: typing.Union[str, str, str] = None,
                 maxinclusive: typing.Union[str, str, str] = None,
                 maxexclusive: typing.Union[str, str, str] = None,
                 last: str = None,
                 **_kwargs: typing.dict[str, object]):
        super().__init__(_CONTEXT, **_kwargs)
        self.first = first
        self.mininclusive = mininclusive
        self.minexclusive = minexclusive
        self.maxinclusive = maxinclusive
        self.maxexclusive = maxexclusive
        self.last = last



class reqList(jsg.JSGObject):
    _reference_types = [reqFacet]
    _members = {'first': jsg.ArrayFactory('first', _CONTEXT, INTEGER, 0, None),
                'mininclusive': jsg.ArrayFactory('mininclusive', _CONTEXT, numericLiteral, 0, None),
                'minexclusive': jsg.ArrayFactory('minexclusive', _CONTEXT, numericLiteral, 0, None),
                'maxinclusive': jsg.ArrayFactory('maxinclusive', _CONTEXT, numericLiteral, 0, None),
                'maxexclusive': jsg.ArrayFactory('maxexclusive', _CONTEXT, numericLiteral, 0, None),
                'last': jsg.ArrayFactory('last', _CONTEXT, STRING, 0, None)}
    _strict = True

    def __init__(self,
                 first: typing.List[str] = None,
                 mininclusive: typing.Union[str, str, str] = None,
                 minexclusive: typing.Union[str, str, str] = None,
                 maxinclusive: typing.Union[str, str, str] = None,
                 maxexclusive: typing.Union[str, str, str] = None,
                 last: typing.List[str] = None,
                 **_kwargs: typing.dict[str, object]):
        super().__init__(_CONTEXT, **_kwargs)
        self.first = first
        self.mininclusive = mininclusive
        self.minexclusive = minexclusive
        self.maxinclusive = maxinclusive
        self.maxexclusive = maxexclusive
        self.last = last



class listOpt(jsg.JSGObject):
    _reference_types = [listFacet]
    _members = {'first': typing.Optional[INTEGER],
                'mininclusive': typing.Optional[jsg.ArrayFactory('mininclusive', _CONTEXT, numericLiteral, 0, None)],
                'minexclusive': typing.Optional[jsg.ArrayFactory('minexclusive', _CONTEXT, numericLiteral, 0, None)],
                'maxinclusive': typing.Optional[jsg.ArrayFactory('maxinclusive', _CONTEXT, numericLiteral, 0, None)],
                'maxexclusive': typing.Optional[jsg.ArrayFactory('maxexclusive', _CONTEXT, numericLiteral, 0, None)],
                'last': jsg.ArrayFactory('last', _CONTEXT, STRING, 1, None)}
    _strict = True

    def __init__(self,
                 first: typing.Optional[str] = None,
                 mininclusive: typing.List[typing.Union[str, str, str]] = None,
                 minexclusive: typing.List[typing.Union[str, str, str]] = None,
                 maxinclusive: typing.List[typing.Union[str, str, str]] = None,
                 maxexclusive: typing.List[typing.Union[str, str, str]] = None,
                 last: typing.List[str] = None,
                 **_kwargs: typing.dict[str, object]):
        super().__init__(_CONTEXT, **_kwargs)
        self.first = first
        self.mininclusive = mininclusive
        self.minexclusive = minexclusive
        self.maxinclusive = maxinclusive
        self.maxexclusive = maxexclusive
        self.last = last



class listReq(jsg.JSGObject):
    _reference_types = [listFacet]
    _members = {'first': jsg.Integer,
                'mininclusive': jsg.ArrayFactory('mininclusive', _CONTEXT, numericLiteral, 0, None),
                'minexclusive': jsg.ArrayFactory('minexclusive', _CONTEXT, numericLiteral, 0, None),
                'maxinclusive': jsg.ArrayFactory('maxinclusive', _CONTEXT, numericLiteral, 0, None),
                'maxexclusive': jsg.ArrayFactory('maxexclusive', _CONTEXT, numericLiteral, 0, None),
                'last': jsg.String}
    _strict = True

    def __init__(self,
                 first: int = None,
                 mininclusive: typing.List[typing.Union[str, str, str]] = None,
                 minexclusive: typing.List[typing.Union[str, str, str]] = None,
                 maxinclusive: typing.List[typing.Union[str, str, str]] = None,
                 maxexclusive: typing.List[typing.Union[str, str, str]] = None,
                 last: str = None,
                 **_kwargs: typing.dict[str, object]):
        super().__init__(_CONTEXT, **_kwargs)
        self.first = first
        self.mininclusive = mininclusive
        self.minexclusive = minexclusive
        self.maxinclusive = maxinclusive
        self.maxexclusive = maxexclusive
        self.last = last



class listList(jsg.JSGObject):
    _reference_types = [listFacet]
    _members = {'first': jsg.ArrayFactory('first', _CONTEXT, INTEGER, 0, None),
                'mininclusive': jsg.ArrayFactory('mininclusive', _CONTEXT, jsg.ArrayFactory('mininclusive', _CONTEXT, numericLiteral, 0, None), 0, None),
                'minexclusive': jsg.ArrayFactory('minexclusive', _CONTEXT, jsg.ArrayFactory('minexclusive', _CONTEXT, numericLiteral, 0, None), 0, None),
                'maxinclusive': jsg.ArrayFactory('maxinclusive', _CONTEXT, jsg.ArrayFactory('maxinclusive', _CONTEXT, numericLiteral, 0, None), 0, None),
                'maxexclusive': jsg.ArrayFactory('maxexclusive', _CONTEXT, jsg.ArrayFactory('maxexclusive', _CONTEXT, numericLiteral, 0, None), 0, None),
                'last': jsg.ArrayFactory('last', _CONTEXT, STRING, 0, None)}
    _strict = True

    def __init__(self,
                 first: typing.List[str] = None,
                 mininclusive: typing.List[typing.Union[str, str, str]] = None,
                 minexclusive: typing.List[typing.Union[str, str, str]] = None,
                 maxinclusive: typing.List[typing.Union[str, str, str]] = None,
                 maxexclusive: typing.List[typing.Union[str, str, str]] = None,
                 last: typing.List[str] = None,
                 **_kwargs: typing.dict[str, object]):
        super().__init__(_CONTEXT, **_kwargs)
        self.first = first
        self.mininclusive = mininclusive
        self.minexclusive = minexclusive
        self.maxinclusive = maxinclusive
        self.maxexclusive = maxexclusive
        self.last = last


_CONTEXT.NAMESPACE = locals()
