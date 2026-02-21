from contextlib import redirect_stderr
from io import StringIO
from typing import cast

from pyjsg.parser_impl.jsg_doc_parser import JSGDocParser
from tests.test_basics.parser import parse


def test_parse_error():
    # In the test_parser_impl unit tests, if we feed an illegal string, the parsing goes on. This test
    # is to figure out why and what to do about it
    outf = StringIO()
    with redirect_stderr(outf):
        d = cast(JSGDocParser, parse("a a {}", "objectDef", JSGDocParser))
    assert d is None
    assert "line 1:2 extraneous input 'a' expecting OBRACE" == outf.getvalue().strip()

