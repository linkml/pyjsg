import tests.test_python_generator.py.list as doc


def test_list(do_python_generator_test):
    jsg = 'l {e:@string*}'
    test_cases = [
        '{"e": []}',
        '{"e": ["abc"]}'
    ]
    do_python_generator_test(jsg, 'list', doc, test_cases, {})

    import tests.test_python_generator.py.list_2 as doc2
    jsg2 = 'l {e:@string+}'
    test_cases2 = [
        '{"e": ["abc"]}'
    ]
    fail_test_cases2 = [
        '{}',
        '{"e": null}',
        '{"e": []}',
    ]
    do_python_generator_test(jsg2, 'list_2', doc2, test_cases2, {}, fail_test_cases2)

