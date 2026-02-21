import pytest
import tests.test_python_generator.py.any_type as any_type
import tests.test_python_generator.py.any_type_2 as any_type_2
import tests.test_python_generator.py.any_type_3 as any_type_3


@pytest.mark.parametrize("jsg,test_file,module,test_cases", [
    (
        'doc {status: .}',
        'any_type',
        any_type,
        ['{"status": 17}', '{"status": "test"}', '{"status": null}',
         '{"status": []}', '{"status": {"status": -117.2}}', '{"status": [{"status": "inside"}]}']
    ),
    (
        'doc {class: .}',
        'any_type_2',
        any_type_2,
        ['{"class": 17}', '{"class": "test"}', '{"class": null}',
         '{"class": []}', '{"class": {"class": -117.2}}', '{"class": [{"class": "inside"}]}']
    ),
    (
        'doc {"A 1": .}',
        'any_type_3',
        any_type_3,
        ['{"A 1": 17}', '{"A 1": "test"}', '{"A 1": null}',
         '{"A 1": []}', '{"A 1": {"A 1": -117.2}}', '{"A 1": [{"A 1": "inside"}]}']
    ),
], ids=['any_type', 'any_type_2', 'any_type_3'])
def test_any_object(do_python_generator_test, jsg, test_file, module, test_cases):
    do_python_generator_test(jsg, test_file, module, test_cases, {})