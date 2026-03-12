import pytest
from jsonasobj import loads as jsonloads
from jsonasobj.jsonobj import as_json

from pyjsg.jsglib import JSGObjectMap, JSGContext, ArrayFactory, Integer
from tests.test_jsglib.iri_defn import *

_CONTEXT = JSGContext()


def test_basic_map():
    class IntObjectMap(JSGObjectMap):
        _name_filter = HEX
        _value_type = ArrayFactory('', _CONTEXT, Integer, 0, None)

        def __init__(self,
                     **_kwargs):
            super().__init__(_CONTEXT, **_kwargs)


    x = IntObjectMap()
    x.E = [1,2,3]
    assert x._is_valid()
    assert as_json(x) == as_json(jsonloads('{"E":[1,2,3]}'))
    with pytest.raises(ValueError):
        x.G = [1, 2, 4]
    with pytest.raises(ValueError):
        x.C = 1
    with pytest.raises(ValueError):
        IntObjectMap(aa=[1])


def test_any_key():
    class ALPHA(JSGString):
        pattern = JSGPattern(r'[A-Za-z]')

    class AnyKeyObjectMap(JSGObjectMap):
        _value_type = ALPHA

        def __init__(self,
                     **_kwargs):
            super().__init__(_CONTEXT, **_kwargs)

    x = AnyKeyObjectMap(**dict(I1="a"))
    x["item 2"] = "b"
    assert x._is_valid()
    with pytest.raises(ValueError):
        x.c = "1"


def test_any_value():
    class IRIKey(JSGObjectMap):
        _name_filter = IRI

        def __init__(self,
                     **_kwargs):
            super().__init__(_CONTEXT, **_kwargs)

    x = IRIKey(**{"http://example.org": 42, "http://ex.org?id=1": None})
    assert '{"http://example.org": 42, "http://ex.org?id=1": null}' == as_json(x, indent=None)
    assert x._is_valid()
    assert 42 == x["http://example.org"]
    assert not x["http://ex.org?id=1"]
