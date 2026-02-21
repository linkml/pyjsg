from pyjsg.validate_json import JSGPython


def test_nested_objects():
    """ The issue being tested here is that we appear to be issuing anonymous identifiers for
    inner objects twice -- once when referenced and a second time when publishing.  As an example, the
    'entry' in 'directory' is typed as '_Anon1', while the ArrayFactory names it as '_Anon6'
    """
    jsg = """
    directory {
        entries: {
            id: ID,
            name: {
                first: @string,
                middle: [@string]?,
                last: @string
            },
            address: {
                city: @string,
                state: @string,
                zip: @int?
            }*
        }*
    }

    @terminals
    ID: [1-9][0-9]{7} @int;
    """

    p1 = '''
      {
        "entries": [
            {"id": 11725433,
              "name": {
                  "first": "Sam",
                  "last": "Sneed"
              },
              "address": [
                {
                  "city": "Southwark",
                  "state": "Bliss"
                }
              ]
            },
            {"id": 10000001,
              "name": {
                  "first": "Julie",
                  "middle": ["Mary", "Elizabeth"],
                  "last": "Sneed"
              },
              "address": [
                {
                  "city": "Southwark",
                  "state": "Agony"
                }
              ]
            }
        ]
      }  
    '''

    x = JSGPython(jsg, print_python=False)
    rslt = x.conforms(p1, 'p1')
    if not rslt.success:
        print(str(rslt))

    assert rslt.success
