import typing
import pyjsg.jsglib as jsg

# .TYPE and .IGNORE settings
_CONTEXT = jsg.JSGContext()
_CONTEXT.TYPE_EXCEPTIONS.append("stringFacet_1_")
_CONTEXT.TYPE_EXCEPTIONS.append("stringFacet_2_")
_CONTEXT.TYPE_EXCEPTIONS.append("numericFacet")
_CONTEXT.TYPE_EXCEPTIONS.append("xsFacet_2_")
_CONTEXT.TYPE_EXCEPTIONS.append("stringFacet")
_CONTEXT.TYPE_EXCEPTIONS.append("xsFacet_1_")
_CONTEXT.TYPE_EXCEPTIONS.append("xsFacet")
_CONTEXT.TYPE_EXCEPTIONS.append("NodeConstraint")


class _Anon1(jsg.JSGString):
    pattern = jsg.JSGPattern(r'(iri)|(bnode)|(nonliteral)|(literal)')


class IRI(jsg.JSGString):
    pattern = jsg.JSGPattern(r'[0-9]')


class stringFacet_1_(jsg.JSGObject):
    _reference_types = []
    _members = {'length': jsg.Integer,
                'minlength': jsg.Integer,
                'maxlength': jsg.Integer}
    _strict = True

    def __init__(self,
                 length: int = None,
                 minlength: int = None,
                 maxlength: int = None,
                 **_kwargs: dict[str, object]):
        super().__init__(_CONTEXT, **_kwargs)
        self.length = length
        self.minlength = minlength
        self.maxlength = maxlength



class stringFacet_2_(jsg.JSGObject):
    _reference_types = []
    _members = {'pattern': jsg.String,
                'flags': typing.Optional[jsg.String]}
    _strict = True

    def __init__(self,
                 pattern: str = None,
                 flags: typing.Optional[str] = None,
                 **_kwargs: dict[str, object]):
        super().__init__(_CONTEXT, **_kwargs)
        self.pattern = pattern
        self.flags = flags



class numericFacet(jsg.JSGObject):
    _reference_types = []
    _members = {'mininclusive': jsg.Integer,
                'minexclusive': jsg.Integer,
                'maxinclusive': jsg.Integer,
                'maxexclusive': jsg.Integer,
                'totaldigits': jsg.Integer,
                'fractiondigits': jsg.Integer}
    _strict = True

    def __init__(self,
                 mininclusive: int = None,
                 minexclusive: int = None,
                 maxinclusive: int = None,
                 maxexclusive: int = None,
                 totaldigits: int = None,
                 fractiondigits: int = None,
                 **_kwargs: dict[str, object]):
        super().__init__(_CONTEXT, **_kwargs)
        self.mininclusive = mininclusive
        self.minexclusive = minexclusive
        self.maxinclusive = maxinclusive
        self.maxexclusive = maxexclusive
        self.totaldigits = totaldigits
        self.fractiondigits = fractiondigits



class xsFacet_2_(jsg.JSGObject):
    _reference_types = [numericFacet]
    _members = {'mininclusive': jsg.Integer,
                'minexclusive': jsg.Integer,
                'maxinclusive': jsg.Integer,
                'maxexclusive': jsg.Integer,
                'totaldigits': jsg.Integer,
                'fractiondigits': jsg.Integer}
    _strict = True

    def __init__(self,
                 mininclusive: int = None,
                 minexclusive: int = None,
                 maxinclusive: int = None,
                 maxexclusive: int = None,
                 totaldigits: int = None,
                 fractiondigits: int = None,
                 **_kwargs: dict[str, object]):
        super().__init__(_CONTEXT, **_kwargs)
        self.mininclusive = mininclusive
        self.minexclusive = minexclusive
        self.maxinclusive = maxinclusive
        self.maxexclusive = maxexclusive
        self.totaldigits = totaldigits
        self.fractiondigits = fractiondigits



class stringFacet(jsg.JSGObject):
    _reference_types = [stringFacet_1_, stringFacet_2_]
    _members = {'length': typing.Optional[jsg.Integer],
                'minlength': typing.Optional[jsg.Integer],
                'maxlength': typing.Optional[jsg.Integer],
                'pattern': typing.Optional[jsg.String],
                'flags': typing.Optional[jsg.String]}
    _strict = True

    def __init__(self,
                 opts_: typing.Union[stringFacet_1_, stringFacet_2_] = None,
                 **_kwargs: dict[str, object]):
        super().__init__(_CONTEXT, **_kwargs)
        if opts_ is not None:
            if isinstance(opts_, stringFacet_1_):
                self.length = opts_.length
                self.minlength = opts_.minlength
                self.maxlength = opts_.maxlength
            elif isinstance(opts_, stringFacet_2_):
                self.pattern = opts_.pattern
                self.flags = opts_.flags
            else:
                raise ValueError(f"Unrecognized value type: {opts_}")



class xsFacet_1_(jsg.JSGObject):
    _reference_types = [stringFacet]
    _members = {'length': typing.Optional[jsg.Integer],
                'minlength': typing.Optional[jsg.Integer],
                'maxlength': typing.Optional[jsg.Integer],
                'pattern': typing.Optional[jsg.String],
                'flags': typing.Optional[jsg.String]}
    _strict = True

    def __init__(self,
                 opts_: typing.Union[stringFacet_1_, stringFacet_2_] = None,
                 **_kwargs: dict[str, object]):
        super().__init__(_CONTEXT, **_kwargs)
        if opts_ is not None:
            if isinstance(opts_, stringFacet_1_):
                self.length = opts_.length
                self.minlength = opts_.minlength
                self.maxlength = opts_.maxlength
            elif isinstance(opts_, stringFacet_2_):
                self.pattern = opts_.pattern
                self.flags = opts_.flags
            else:
                raise ValueError(f"Unrecognized value type: {opts_}")



class xsFacet(jsg.JSGObject):
    _reference_types = [xsFacet_1_, xsFacet_2_]
    _members = {'length': typing.Optional[typing.Optional[jsg.Integer]],
                'minlength': typing.Optional[typing.Optional[jsg.Integer]],
                'maxlength': typing.Optional[typing.Optional[jsg.Integer]],
                'pattern': typing.Optional[typing.Optional[jsg.String]],
                'flags': typing.Optional[typing.Optional[jsg.String]],
                'mininclusive': typing.Optional[typing.Optional[jsg.Integer]],
                'minexclusive': typing.Optional[typing.Optional[jsg.Integer]],
                'maxinclusive': typing.Optional[typing.Optional[jsg.Integer]],
                'maxexclusive': typing.Optional[typing.Optional[jsg.Integer]],
                'totaldigits': typing.Optional[typing.Optional[jsg.Integer]],
                'fractiondigits': typing.Optional[typing.Optional[jsg.Integer]]}
    _strict = True

    def __init__(self,
                 opts_: typing.Union[xsFacet_1_, xsFacet_2_] = None,
                 **_kwargs: dict[str, object]):
        super().__init__(_CONTEXT, **_kwargs)
        if opts_ is not None:
            if isinstance(opts_, xsFacet_1_):
                if opts_ is not None:
                    if isinstance(opts_, stringFacet_1_):
                        self.length = opts_.length
                        self.minlength = opts_.minlength
                        self.maxlength = opts_.maxlength
                    elif isinstance(opts_, stringFacet_2_):
                        self.pattern = opts_.pattern
                        self.flags = opts_.flags
                    else:
                        raise ValueError(f"Unrecognized value type: {opts_}")
            elif isinstance(opts_, xsFacet_2_):
                self.mininclusive = opts_.mininclusive
                self.minexclusive = opts_.minexclusive
                self.maxinclusive = opts_.maxinclusive
                self.maxexclusive = opts_.maxexclusive
                self.totaldigits = opts_.totaldigits
                self.fractiondigits = opts_.fractiondigits
            else:
                raise ValueError(f"Unrecognized value type: {opts_}")



class NodeConstraint(jsg.JSGObject):
    _reference_types = [xsFacet]
    _members = {'nodeKind': typing.Optional[_Anon1],
                'datatype': typing.Optional[IRI],
                'length': typing.Optional[typing.Optional[jsg.Integer]],
                'minlength': typing.Optional[typing.Optional[jsg.Integer]],
                'maxlength': typing.Optional[typing.Optional[jsg.Integer]],
                'pattern': typing.Optional[typing.Optional[jsg.String]],
                'flags': typing.Optional[typing.Optional[jsg.String]],
                'mininclusive': typing.Optional[typing.Optional[jsg.Integer]],
                'minexclusive': typing.Optional[typing.Optional[jsg.Integer]],
                'maxinclusive': typing.Optional[typing.Optional[jsg.Integer]],
                'maxexclusive': typing.Optional[typing.Optional[jsg.Integer]],
                'totaldigits': typing.Optional[typing.Optional[jsg.Integer]],
                'fractiondigits': typing.Optional[typing.Optional[jsg.Integer]]}
    _strict = True

    def __init__(self,
                 nodeKind: typing.Optional[str] = None,
                 datatype: typing.Optional[str] = None,
                 opts_: typing.Union[xsFacet_1_, xsFacet_2_] = None,
                 **_kwargs: dict[str, object]):
        super().__init__(_CONTEXT, **_kwargs)
        self.nodeKind = nodeKind
        self.datatype = datatype
        if opts_ is not None:
            if isinstance(opts_, xsFacet_1_):
                if opts_ is not None:
                    if isinstance(opts_, stringFacet_1_):
                        self.length = opts_.length
                        self.minlength = opts_.minlength
                        self.maxlength = opts_.maxlength
                    elif isinstance(opts_, stringFacet_2_):
                        self.pattern = opts_.pattern
                        self.flags = opts_.flags
                    else:
                        raise ValueError(f"Unrecognized value type: {opts_}")
            elif isinstance(opts_, xsFacet_2_):
                self.mininclusive = opts_.mininclusive
                self.minexclusive = opts_.minexclusive
                self.maxinclusive = opts_.maxinclusive
                self.maxexclusive = opts_.maxexclusive
                self.totaldigits = opts_.totaldigits
                self.fractiondigits = opts_.fractiondigits
            else:
                raise ValueError(f"Unrecognized value type: {opts_}")


_CONTEXT.NAMESPACE = locals()
