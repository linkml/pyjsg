def test_simple_map(do_python_generator_test):
    import tests.test_python_generator.py.objectmap_1 as doc

    jsg = """.TYPE type - Person ;
    Directory {. -> Person}
    Person {name: @string age: @int?}
    """
    test_cases = [
        """{"type": "Directory",
            "1234": {"name": "Sam Smith", "age": 43},
            "1245": {"name": "Jill Jones", "age": 17},
            "Unk person": {"name": "Destroyer"}}""",
        '{"type": "Directory"}'
    ]

    fail_cases = [
        """{"type": "Directory",
            "1234": {"age": 43}}""",
        """{"type": "Directory",
            "v": 1}""",
        """{"type": "Directory",
            "v": {"g": null}"""
    ]
    do_python_generator_test(jsg, 'objectmap_1', doc, test_cases, {}, fail_cases, print_python=False)


def test_cardinality(do_python_generator_test):
    import tests.test_python_generator.py.objectmap_2 as doc

    jsg = """Directory {PNAME -> Person{2,3}}
    Person {name: @string age: @int?}

    @terminals
    PNAME: [A-Z][0-9]+ ;        
    """
    test_cases = [
        """{"A1234": {"name": "Sam Smith", "age": 43},
            "A1245": {"name": "Jill Jones", "age": 17}}""",
        """{"A1234": {"name": "Sam Smith", "age": 43},
            "A1245": {"name": "Jill Jones", "age": 17},
            "A12345": {"name": "Destroyer"}}""",
    ]
    fail_cases = ["""{"B0": {"name": "Sam Smith", "age": 43},
            "B1": {"name": "Jill Jones", "age": 17},
            "B2": {"name": "Destroyer"}},
            "B3"" {"name": "toomany"}}"""
    ]
    do_python_generator_test(jsg, 'objectmap_2', doc, test_cases, {}, fail_cases, print_python=False)


def test_key_types_2(do_python_generator_test):
    import tests.test_python_generator.py.objectmap_3 as doc

    jsg = """Directory {PNAME -> Person}
Person {name: @string age: @int?}

@terminals
PNAME: [A-Z][0-9]+ ;        
"""
    test_cases = [
        '{"A1": {"name": "Sam Smith", "age": 43}}',
        '{"B17": {"name": "Jill Jones", "age": 17}}',
        '{}'
    ]
    fail_cases = [

    ]
    do_python_generator_test(jsg, 'objectmap_3', doc, test_cases, {}, fail_cases, print_python=False)
