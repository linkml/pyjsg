from typing import Dict, Optional

import pytest
from dict_compare import dict_compare
from io import StringIO
from jsonasobj import loads as json_loads

from pyjsg.jsglib import JSGNull, String, Integer, Boolean, Number, JSGContext, JSGObject, Empty

_CONTEXT = JSGContext()


def check_json(t: JSGObject, c: str):
    assert dict_compare(json_loads(c)._as_dict, t._as_json_obj())


def test_simple_object():
    class Person(JSGObject):
        _reference_types = []
        _members = {'name': String,
                    'age': Integer,
                    'married': Boolean,
                    'weight': Number,
                    'tag': Optional[JSGNull]}
        _strict = True

        def __init__(self,
                     name: str = None,
                     age: int = None,
                     married: bool = None,
                     weight: float = None,
                     tag: Optional[type(None)] = Empty,
                     **_kwargs: Dict[str, object]):
            super().__init__(_CONTEXT, **_kwargs)
            self.name = name
            self.age = age
            self.married = married
            self.weight = weight
            self.tag = tag

    log = StringIO()

    x = Person()
    x.name = "Grunt P Snooter"
    x = Person(name="Sally Pope", age=42, married=True, weight=117)
    x.name = "Joe"
    check_json(x, '{"name": "Sally Pope", "age": 42, "married": true, "weight": 117.5}')
    x = Person("Sally Pope", "42")
    check_json(x, '{"name": "Sally Pope", "age": 42}')
    x = Person("Sally Pope")
    assert not x._is_valid(log)
    assert ('Person: Missing required field: \'age\'\n'
           'Person: Missing required field: \'married\'\n'
            'Person: Missing required field: \'weight\'\n' == log.getvalue())
    log = StringIO()
    x.age = 99
    assert not x._is_valid()
    x.married = False
    assert not x._is_valid()
    x.weight = "112"
    assert x._is_valid()
    check_json(x, '{"name": "Sally Pope", "age": 99, "married": false, "weight": 112}')
    x.tag = None
    check_json(x, '{"name": "Sally Pope", "age": 99, "married": false, "weight": 112, "tag": null}')
    x.tag = Empty
    check_json(x, '{"name": "Sally Pope", "age": 99, "married": false, "weight": 112}')
    with pytest.raises(ValueError):
        x.age = "abc"
    del x.weight
    x._is_valid(log)
    assert 'Person: Missing required field: \'weight\'\n' == log.getvalue()

