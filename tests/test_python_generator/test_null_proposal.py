import pytest
from jsonasobj.jsonobj import as_json

from pyjsg.jsglib.loader import is_valid, loads
from pyjsg.jsglib import Empty
from pyjsg.validate_json import JSGPython


def test_required_null():
    j = JSGPython('doc { x: @null }', print_python=False)
    rslt = j.conforms('{"x": null}')
    if not rslt.success:
        print(str(rslt))
    assert rslt.success
    jclass = getattr(j.module, 'doc')
    j2 = jclass()
    assert '{}' == as_json(j2)
    assert not is_valid(j2)
    j2.x = None
    assert '{"x": null}' == as_json(j2, indent=None)
    assert is_valid(j2)
    j2.x = Empty
    assert '{}' == as_json(j2)
    assert not is_valid(j2)
    with pytest.raises(ValueError):
        j2.x = 17


def test_optional_null():
    j = JSGPython('doc { x: @null? }', print_python=False)
    rslt = j.conforms('{"x": null}')
    if not rslt.success:
        print(str(rslt))
    assert rslt.success
    jclass = getattr(j.module, 'doc')
    j2 = jclass()
    assert '{}' == as_json(j2)
    assert is_valid(j2)
    j2.x = None
    assert '{"x": null}' == as_json(j2, indent=None)
    assert is_valid(j2)
    j2.x = Empty
    assert '{}' == as_json(j2)
    assert is_valid(j2)
    with pytest.raises(ValueError):
        j2.x = 17


def test_required_any():
    j = JSGPython('doc { x: . }', print_python=False)
    rslt = j.conforms('{"x": null}')
    if not rslt.success:
        print(str(rslt))
    assert rslt.success
    jclass = getattr(j.module, 'doc')
    j2 = jclass()
    assert '{}' == as_json(j2)
    assert not is_valid(j2)
    j2.x = None
    assert '{"x": null}' == as_json(j2, indent=None)
    assert is_valid(j2)
    j2.x = Empty
    assert '{}', as_json(j2)
    assert not is_valid(j2)


def test_various_anys():
    j = JSGPython('doc {x: . }')
    for v in ['null', '17', '-22', '-22.0', 'true', '"A string"', '{"x": 243}']:
        json = f'{{"x": {v}}}'
        j2 = loads(json, j.module)
        assert json == as_json(j2, indent=None)
    json = '{"x": -17395e-2}'
    assert '{"x": -173.95}' == as_json(loads(json, j.module), indent=None)


def test_various_optional_anys():
    j = JSGPython('doc {x: .? }')
    for v in ['null', '17', '-22', '-22.0', 'false', '"A string"', '{"x": null}']:
        json = f'{{"x": {v}}}'
        j2 = loads(json, j.module)
        assert json == as_json(j2, indent=None)
    json = '{"x": -17395e-2}'
    assert '{"x": -173.95}' == as_json(loads(json, j.module), indent=None)


def test_optional_any():
    j = JSGPython('doc { x: .? }', print_python=False)
    rslt = j.conforms('{"x": null}')
    if not rslt.success:
        print(str(rslt))
    assert rslt.success
    jclass = getattr(j.module, 'doc')
    j2 = jclass()
    assert '{}' == as_json(j2)
    assert is_valid(j2)
    j2.x = None
    assert '{"x": null}' == as_json(j2, indent=None)
    assert is_valid(j2)
    j2.x = Empty
    assert '{}' == as_json(j2)
    assert is_valid(j2)
