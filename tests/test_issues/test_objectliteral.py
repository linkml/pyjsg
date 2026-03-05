from pathlib import Path

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


def test_ol():
    """ Test that the 'type' variable in the ObjectLiteral is not mistaken as a real, unresolved type."""
    shexj_jsg = (Path(__file__).resolve().parent / '..' / 'test_basics' / 'jsg' / 'ShExJ.jsg').resolve()
    x = JSGPython(str(shexj_jsg))
    rval = x.conforms(json_str, "1val1DECIMAL")

    assert str(rval) == "1val1DECIMAL: Conforms to Schema"
    assert rval.success
