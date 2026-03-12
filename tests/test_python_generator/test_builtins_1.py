from pyjsg.validate_json import JSGPython


def test_name_valuetype():
    x = JSGPython('''doc {
        last_name : @string,       # exactly one last name of type string
        "first name" : @string+      # array or one or more first names
        age : @int?,               # optional age of type int
        weight : @number*,         # array of zero or more weights
        rating : @int{2,},         # at least two ratings
        spin: [@bool{0, 2}]?
    }
    ''', print_python=False)
    r = x.conforms('''
    { "last_name" : "snooter",
      "first name" : ["grunt", "peter"],
      "weight" : [],
      "rating" : [10, 10]
    }''')
    assert r.success, str(r)
    r = x.conforms('''
    { 
      "first name" : ["grunt", "peter"],
      "weight" : [],
      "rating" : [10, 10]
    }''')
    assert not r.success
    assert "FAIL - doc: Missing required field: 'last_name'" == str(r)
    r = x.conforms('''
    { "last_name" : "snooter",
      "first name" : [],
      "weight" : [],
      "rating" : [9, 9]
    }''')
    assert not r.success
    assert "FAIL - Wrong type for first name: [] - expected: <class 'pyjsg.jsglib.jsg_array.first name'> got list" == str(r)
    r = x.conforms('''
       { "last_name" : "snooter",
         "first name" : "jim",
         "weight" : [],
         "rating" : [1, 2]
       }''')
    assert not r.success
    assert "FAIL - Wrong type for first name: 'jim' - expected: <class 'pyjsg.jsglib.jsg_array.first name'> got str" == str(r)
    r = x.conforms('''
      { "last_name" : "snooter",
        "first name" : [17, 12.3, false],
        "weight" : [],
        "rating" : [1, 1]
      }''')
    assert not r.success
    # TODO: Get these error messages up and running
    print(f"TODO: first name element 0: 17 is not a String\n"
                     f"first name element 1: 12.3 is not a String\n"
                     f"first name element 2: False is not a String !=  {str(r)}")
    # self.assertEqual("FAIL - first name element 0: 17 is not a String\n")
    #                  "first name element 1: 12.3 is not a String\n"
    #                  "first name element 2: False is not a String", str(r))
    r = x.conforms('''
       { "last_name" : "snooter",
         "first name" : ["jim"],
         "weight" : [],
         "rating" : [1]
       }''')
    assert not r.success
    # TODO: Fix this
    print(f"TODO - rating: at least 2 values required - element has 1 != {str(r)}")
    # self.assertEqual("FAIL - rating: at least 2 values required - element has 1", str(r))
    r = x.conforms('''
       { "last_name" : "snooter",
         "first name" : ["jim"],
         "weight" : [],
         "rating" : [1, 10],
         "spin" : [false, true, false]
       }''')
    assert not r.success
    # TODO: Fix this
    print(f"TODO - spin: no more than 2 values permitted - element has 3 != {str(r)}")
    # self.assertEqual("FAIL - spin: no more than 2 values permitted - element has 3", str(r))


def test_builtins():
    x = JSGPython('''
    doc {
        v1: @string,
        v2: @number,
        v3: @int,
        v4: @bool,
        v5: @null,
        v6: @array,
        v7: @object 
    }
    another_object { , }''')

    r = x.conforms('''
    { "v1": "This is text!",
      "v2": -117.432e+2,
      "v3": -100173,
      "v4": false,
      "v5": null,
      "v6": [12, "text", null],
      "v7": {"q": "life", "a": 42}
    }''')
    assert r.success
