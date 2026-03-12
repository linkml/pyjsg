import typing
import pyjsg.jsglib as jsg

# .TYPE and .IGNORE settings
_CONTEXT = jsg.JSGContext()
_CONTEXT.TYPE_EXCEPTIONS.append("stringFacet")
_CONTEXT.TYPE_EXCEPTIONS.append("numericFacet")
_CONTEXT.TYPE_EXCEPTIONS.append("xsFacet")
_CONTEXT.TYPE_EXCEPTIONS.append("labeledNodeConstraint")


class INTEGER(jsg.JSGString):
    pattern = jsg.JSGPattern(r'[0-9]*')


class DECIMAL(jsg.JSGString):
    pattern = jsg.JSGPattern(r'[0-9]*')


class DOUBLE(jsg.JSGString):
    pattern = jsg.JSGPattern(r'[0-9]*')


class STRING(jsg.JSGString):
    pattern = jsg.JSGPattern(r'[A-Z]*')


class stringFacet(jsg.JSGObject):
    _reference_types = []
    _members = {'length': typing.Optional[INTEGER],
                'minlength': typing.Optional[INTEGER],
                'maxlength': typing.Optional[INTEGER],
                'pattern': STRING,
                'flags': typing.Optional[STRING]}
    _strict = True

    def __init__(self,
                 length: typing.Optional[str] = None,
                 minlength: typing.Optional[str] = None,
                 maxlength: typing.Optional[str] = None,
                 pattern: str = None,
                 flags: typing.Optional[str] = None,
                 **_kwargs: dict[str, object]):
        super().__init__(_CONTEXT, **_kwargs)
        self.length = length
        self.minlength = minlength
        self.maxlength = maxlength
        self.pattern = pattern
        self.flags = flags



class numericFacet(jsg.JSGObject):
    _reference_types = []
    _members = {'mininclusive': typing.Optional[DOUBLE],
                'minexclusive': typing.Optional[DOUBLE],
                'maxinclusive': typing.Optional[DOUBLE],
                'maxexclusive': typing.Optional[DOUBLE],
                'totaldigits': typing.Optional[INTEGER],
                'fractiondigits': typing.Optional[INTEGER]}
    _strict = True

    def __init__(self,
                 mininclusive: typing.Optional[str] = None,
                 minexclusive: typing.Optional[str] = None,
                 maxinclusive: typing.Optional[str] = None,
                 maxexclusive: typing.Optional[str] = None,
                 totaldigits: typing.Optional[str] = None,
                 fractiondigits: typing.Optional[str] = None,
                 **_kwargs: dict[str, object]):
        super().__init__(_CONTEXT, **_kwargs)
        self.mininclusive = mininclusive
        self.minexclusive = minexclusive
        self.maxinclusive = maxinclusive
        self.maxexclusive = maxexclusive
        self.totaldigits = totaldigits
        self.fractiondigits = fractiondigits



class xsFacet(jsg.JSGObject):
    _reference_types = [stringFacet, numericFacet]
    _members = {'length': typing.Optional[INTEGER],
                'minlength': typing.Optional[INTEGER],
                'maxlength': typing.Optional[INTEGER],
                'pattern': STRING,
                'flags': typing.Optional[STRING],
                'mininclusive': typing.Optional[DOUBLE],
                'minexclusive': typing.Optional[DOUBLE],
                'maxinclusive': typing.Optional[DOUBLE],
                'maxexclusive': typing.Optional[DOUBLE],
                'totaldigits': typing.Optional[INTEGER],
                'fractiondigits': typing.Optional[INTEGER]}
    _strict = True

    def __init__(self,
                 length: typing.Optional[str] = None,
                 minlength: typing.Optional[str] = None,
                 maxlength: typing.Optional[str] = None,
                 pattern: str = None,
                 flags: typing.Optional[str] = None,
                 mininclusive: typing.Optional[str] = None,
                 minexclusive: typing.Optional[str] = None,
                 maxinclusive: typing.Optional[str] = None,
                 maxexclusive: typing.Optional[str] = None,
                 totaldigits: typing.Optional[str] = None,
                 fractiondigits: typing.Optional[str] = None,
                 **_kwargs: dict[str, object]):
        super().__init__(_CONTEXT, **_kwargs)
        self.length = length
        self.minlength = minlength
        self.maxlength = maxlength
        self.pattern = pattern
        self.flags = flags
        self.mininclusive = mininclusive
        self.minexclusive = minexclusive
        self.maxinclusive = maxinclusive
        self.maxexclusive = maxexclusive
        self.totaldigits = totaldigits
        self.fractiondigits = fractiondigits



class labeledNodeConstraint(jsg.JSGObject):
    _reference_types = [xsFacet]
    _members = {'first': typing.Optional[INTEGER],
                'length': jsg.ArrayFactory('length', _CONTEXT, typing.Optional[INTEGER], 0, None),
                'minlength': jsg.ArrayFactory('minlength', _CONTEXT, typing.Optional[INTEGER], 0, None),
                'maxlength': jsg.ArrayFactory('maxlength', _CONTEXT, typing.Optional[INTEGER], 0, None),
                'pattern': jsg.ArrayFactory('pattern', _CONTEXT, STRING, 0, None),
                'flags': jsg.ArrayFactory('flags', _CONTEXT, typing.Optional[STRING], 0, None),
                'mininclusive': jsg.ArrayFactory('mininclusive', _CONTEXT, typing.Optional[DOUBLE], 0, None),
                'minexclusive': jsg.ArrayFactory('minexclusive', _CONTEXT, typing.Optional[DOUBLE], 0, None),
                'maxinclusive': jsg.ArrayFactory('maxinclusive', _CONTEXT, typing.Optional[DOUBLE], 0, None),
                'maxexclusive': jsg.ArrayFactory('maxexclusive', _CONTEXT, typing.Optional[DOUBLE], 0, None),
                'totaldigits': jsg.ArrayFactory('totaldigits', _CONTEXT, typing.Optional[INTEGER], 0, None),
                'fractiondigits': jsg.ArrayFactory('fractiondigits', _CONTEXT, typing.Optional[INTEGER], 0, None),
                'last': jsg.ArrayFactory('last', _CONTEXT, STRING, 1, None)}
    _strict = True

    def __init__(self,
                 first: typing.Optional[str] = None,
                 length: typing.Optional[str] = None,
                 minlength: typing.Optional[str] = None,
                 maxlength: typing.Optional[str] = None,
                 pattern: str = None,
                 flags: typing.Optional[str] = None,
                 mininclusive: typing.Optional[str] = None,
                 minexclusive: typing.Optional[str] = None,
                 maxinclusive: typing.Optional[str] = None,
                 maxexclusive: typing.Optional[str] = None,
                 totaldigits: typing.Optional[str] = None,
                 fractiondigits: typing.Optional[str] = None,
                 last: list[str] = None,
                 **_kwargs: dict[str, object]):
        super().__init__(_CONTEXT, **_kwargs)
        self.first = first
        self.length = length
        self.minlength = minlength
        self.maxlength = maxlength
        self.pattern = pattern
        self.flags = flags
        self.mininclusive = mininclusive
        self.minexclusive = minexclusive
        self.maxinclusive = maxinclusive
        self.maxexclusive = maxexclusive
        self.totaldigits = totaldigits
        self.fractiondigits = fractiondigits
        self.last = last


_CONTEXT.NAMESPACE = locals()
