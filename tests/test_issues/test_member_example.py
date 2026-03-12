from pyjsg.validate_json import JSGPython


def test_member_example():
    x = JSGPython('''doc {
        last_name : @string,       # exactly one last name of type string
        first_name : @string+      # array or one or more first names
        age : @int?,               # optional age of type int
        weight : @number*          # array of zero or more weights
    }
    ''')
    rslts = x.conforms('''
    { "last_name" : "snooter",
      "first_name" : ["grunt", "peter"],
      "weight" : []
    }''')
    assert rslts.success
