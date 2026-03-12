def test_missing_items(do_test_harness):
    do_test_harness("doc {status: .}", "{}", False, False, True, "doc: Missing required field: 'status'")
    do_test_harness("doc {status: .} item {}", "{}")
    do_test_harness("doc {status: .} item {v: .}", "{}", False, False, True, "doc: Missing required field: 'status'")
    do_test_harness("item {v: .} doc {status: .} ", "{}", False, False, True, "item: Missing required field: 'v'")
    do_test_harness("doc {status: .} item {v: .}", '{"status": null}')
    do_test_harness("doc {status: .} item {v: .}", '{"status": 17}')
    do_test_harness("doc {status: .} item {v: .}", '{"status": "stuff"}')
    do_test_harness("doc {status: .} item {v: .}", '{"v": true}', True)
