from pyjsg.validate_json import JSGPython


def test_extra():
    x = JSGPython('doc {a:@string}')
    assert not x.conforms('{"a":"hello", "target":"earthling"}').success