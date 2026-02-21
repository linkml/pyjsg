import os
from pathlib import Path

import pytest

from pyjsg.validate_json import JSGPython

json_str = """
{
  "@context": "http://www.w3.org/ns/shex.jsonld",
  "type": "Schema",
  "shapes": [
    {
      "id": "http://a.example/S1",
      "type": "Shape",
      "expression": {
        "type": "TripleConstraint",
        "predicate": "http://a.example/p1",
        "valueExpr": {
          "type": "NodeConstraint",
          "values": [
            {
              "value": "0.0",
              "type": "http://www.w3.org/2001/XMLSchema#decimal"
            }
          ]
        }
      }
    }
  ]
}
"""

#TODO: discuss in developer call, seemingly when running all tests in terminal the global state gets changed and is
# not reset so this test will fail unless it is being run in a different thread using pytest-forked. Can anyone pinpoint
# the problem so we can drop the pytest-forked dependency?
# Note that on windows there is a warning due to poor windows support of pytest-forked. For now not disabling on windows
# given that it is only a warning.
def test_ol():
    """ Test that the 'type' variable in the ObjectLiteral is not mistaken as a real, unresolved type."""
    shexj_jsg = (Path(__file__).resolve().parent / '..' / 'test_basics' / 'jsg' / 'ShExJ.jsg').resolve()
    rval = JSGPython(str(shexj_jsg)).conforms(json_str, "1val1DECIMAL")

    assert str(rval) == "1val1DECIMAL: Conforms to Schema"
    assert rval.success
