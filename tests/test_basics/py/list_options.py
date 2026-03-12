import typing
import pyjsg.jsglib as jsg

# .TYPE and .IGNORE settings
_CONTEXT = jsg.JSGContext()
_CONTEXT.TYPE_EXCEPTIONS.append("list_eval")


class INT(jsg.JSGString):
    pattern = jsg.JSGPattern(r'[0-9]')


class list_eval(jsg.JSGObject):
    _reference_types = []
    _members = {'req': INT,
                'opt': typing.Optional[INT],
                'zero_or_more': jsg.ArrayFactory('zero_or_more', _CONTEXT, INT, 0, None),
                'one_or_more': jsg.ArrayFactory('one_or_more', _CONTEXT, INT, 1, None),
                'two_or_more': jsg.ArrayFactory('two_or_more', _CONTEXT, INT, 2, None),
                'three_or_four': jsg.ArrayFactory('three_or_four', _CONTEXT, INT, 3, 4),
                'one_or_more_v2': jsg.ArrayFactory('one_or_more_v2', _CONTEXT, INT, 1, None)}
    _strict = True

    def __init__(self,
                 req: str = None,
                 opt: typing.Optional[str] = None,
                 zero_or_more: list[str] = None,
                 one_or_more: list[str] = None,
                 two_or_more: list[str] = None,
                 three_or_four: list[str] = None,
                 one_or_more_v2: list[str] = None,
                 **_kwargs: dict[str, object]):
        super().__init__(_CONTEXT, **_kwargs)
        self.req = req
        self.opt = opt
        self.zero_or_more = zero_or_more
        self.one_or_more = one_or_more
        self.two_or_more = two_or_more
        self.three_or_four = three_or_four
        self.one_or_more_v2 = one_or_more_v2


_CONTEXT.NAMESPACE = locals()
