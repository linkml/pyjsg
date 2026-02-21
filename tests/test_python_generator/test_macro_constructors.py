def test_macro1(do_python_generator_test):
    import tests.test_python_generator.py.macrotest_1 as doc

    jsg = 'Shape {id:(@int|@string)?}'
    test_cases = [
        '{"id": 17}',
        '{"id": "abc"}'
    ]
    fail_cases = [
        '{"id": 12.2}',
        '{"id": 17, "j": 1}'
    ]
    do_python_generator_test(jsg, 'macrotest_1', doc, test_cases, {}, fail_cases)


def test_macro2(do_python_generator_test):
    import tests.test_python_generator.py.macrotest_2 as doc2
    jsg2 = """
shapeExprLabel   = @int|@string ;
Shape            {id:shapeExprLabel?}
"""
    test_cases = [
        '{"id": 17}',
        '{"id": "abc"}'
    ]
    fail_cases = [
        '{"id": 12.2}',
        '{"id": 17, "j": 1}'
    ]
    do_python_generator_test(jsg2, 'macrotest_2', doc2, test_cases, {}, fail_cases)


def test_macro3(do_python_generator_test):
    import tests.test_python_generator.py.macrotest_3 as doc3
    testfile = "macrotest_3"

    jsg3 = """
shapeExprLabel   = IRIREF|BNODE ;
Shape            {id:shapeExprLabel?}

@terminals
IRIREF           : [A-Z]+ ;
BNODE            : '_:' [A-Z]+ ;\
"""
    test_cases = [
        '{"id": "AAA"}',
        '{"id": "_:AAA"}'
    ]
    fail_cases = [
        '{"id": "aaa"}',
        '{"id": "AAA", "j": 1}'
    ]
    do_python_generator_test(jsg3, testfile, doc3, test_cases, {}, fail_cases, print_python=False)
