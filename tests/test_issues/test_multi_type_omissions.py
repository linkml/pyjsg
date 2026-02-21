jsg1 = '''
.TYPE t - id val ;
doc {a:.,}
id {b: @int}
val {c: @string}
'''


def test_one_pass(do_test_harness, jsg1):
    do_test_harness(jsg1, '{"t": "doc", "a": {"b": 173}}')
    do_test_harness(jsg1, '{"c": "sails"}')
    do_test_harness(jsg1, '{"b": -117}')


def test_one_fail(do_test_harness, jsg1):
    do_test_harness(jsg1, '{"t": "doc", "a": {"b": "x"}}', False, False, False, 'Invalid Integer value: "x"')
    do_test_harness(jsg1, '{"c": 112}', False, False, False, 'Invalid String value "112"')
    do_test_harness(jsg1, '{"b": "test"}', False, False, False, 'Invalid Integer value: "x"')
    do_test_harness(jsg1, '{"d": 117}', False)

