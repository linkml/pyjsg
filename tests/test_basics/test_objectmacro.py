import pytest
from typing import cast

from pyjsg.parser_impl.jsg_doc_parser import JSGDocParser
from tests.test_basics.parser import parse


@pytest.mark.parametrize("jsg", [
    "macro = labeledShapeOr ; labeledShapeOr {}",
    "macro = a:@int | b:@int ;",
    "macro = a| b ; a {} b {}",
])
def test_single_option(jsg):
    t = cast(JSGDocParser, parse(jsg, "doc", JSGDocParser))
    exec(t.as_python(test_single_option.__name__), dict())
