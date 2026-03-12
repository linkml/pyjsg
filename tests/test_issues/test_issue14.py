import os
from contextlib import redirect_stdout
from io import StringIO

from pyjsg.parser_impl.generate_python import generate


def test_e_option():
    """ Test the '-e' option """
    shexj_jsg = os.path.join(os.path.dirname(__file__), '..', 'test_basics', 'jsg', 'ShExJ.jsg')
    outf = StringIO()
    with redirect_stdout(outf):
        # Should not fail
        assert 0 == generate([shexj_jsg, "-e"])

