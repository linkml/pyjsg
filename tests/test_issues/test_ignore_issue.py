from pyjsg.validate_json import JSGPython


def test_ignore_issue():
    """ Test list of sequences in documentation """
    x = JSGPython('''
.IGNORE target;
doc {a:@string}
''')

    rslt = x.conforms('{"a":"hello", "target":"earthling"}')
    assert rslt.success
