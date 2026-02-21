import tests.test_python_generator.py.builtins_cooked as doc


def test_builtins_cooked(do_python_generator_test):
    jsg = '''doc {
       v1: @string,
       v2: @number,
       v3: @int,
       v4: @bool,
       v5: @null,
       v6: @array,
       v7: @object 
    }
    another_object { , }'''
    json_doc = '''
    { "v1": "This is text!",
      "v2": -117.432e+2,
      "v3": -100173,
      "v4": false,
      "v5": null,
      "v6": [12, "text", null],
      "v7": {"q": "life", "a": 42}
    }'''
    load_vals = {
        "v1": 1,
        "v2": "text",
        "v3": "text",
        "v4": "text",
        "v5": "text",
        "v6": "text",
        "v7": "text"
    }
    do_python_generator_test(jsg, 'builtins_cooked', doc, [json_doc], load_vals)


def test_builtins_semiraw(do_python_generator_test):
    jsg = '''doc {
       class: @string,
       def: @number,
       import: @int,
       with: @bool,
       if: @null,
       else: @array,
       raise: @object 
    }
    another_object { , }'''
    json_doc = '''
    { "class": "This is text!",
      "def": -117.432e+2,
      "import": -100173,
      "with": false,
      "if": null,
      "else": [12, "text", null],
      "raise": {"q": "life", "a": 42}
    }'''
    do_python_generator_test(jsg, 'builtins_semiraw', doc, [json_doc], {})


def test_builtins_raw(do_python_generator_test):
    jsg = '''doc {
       "v 1": @string,
       "v 2": @number,
       "v 3": @int,
       "v 4": @bool,
       "v 5": @null,
       "v 6": @array,
       "v 7": @object 
    }
    another_object { , }'''
    json_doc = '''
    { "v 1": "This is text!",
      "v 2": -117.432e+2,
      "v 3": -100173,
      "v 4": false,
      "v 5": null,
      "v 6": [12, "text", null],
      "v 7": {"q": "life", "a": 42}
    }'''
    do_python_generator_test(jsg, 'builtins_raw', doc, [json_doc], {})
