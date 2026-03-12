import os
from dict_compare import compare_dicts
from jsonasobj.jsonobj import as_json, as_dict

import tests.test_basics.py.ShExJ as ShExJ
from pyjsg.jsglib.loader import loads, is_valid, Logger
from jsonasobj import loads as jao_loads


def test_facet():
    file_loc = os.path.join(os.path.dirname(__file__), '..', 'data', '1bnodeLength.json')
    with open(file_loc)  as f:
        text = f.read()
    facets = loads(text, ShExJ)

    log = Logger()
    val = is_valid(facets, log)

    assert val
    d1 = jao_loads(text)
    d2 = jao_loads(as_json(facets))
    assert compare_dicts(as_dict(d1), as_dict(d2))
