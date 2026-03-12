from pyjsg.jsglib import JSGPattern
from tests.test_jsglib.iri_defn import IRI


def test_wild_card():
    pattern = JSGPattern(r'.*')
    assert pattern.matches("")
    assert pattern.matches("any block of text")
    assert pattern.matches("\n\uFDF0*")


def test_fixed_values():
    pattern = JSGPattern(r'http:\/\/www\.w3\.org\/ns\/shex\.jsonld')
    assert pattern.matches("http://www.w3.org/ns/shex.jsonld")
    assert not pattern.matches("http://www.w3.org/ns/shex/jsonldx")
    assert not pattern.matches("http://www.w3.org/ns/shex/jsonld ")
    assert not pattern.matches("http://www.w3.org/ns/shex/jsonld\n")
    assert not pattern.matches(" http://www.w3.org/ns/shex/jsonld")


def test_alternatives():
    pattern = JSGPattern(r'iri|bnode|nonliteral|literal')
    assert pattern.matches('iri')
    assert pattern.matches('literal')
    assert pattern.matches('nonliteral')
    assert pattern.matches('bnode')
    assert not pattern.matches('node')
    assert not pattern.matches('bnod')
    assert not pattern.matches('IRI')
    assert not pattern.matches(' iri')
    assert not pattern.matches('iri ')


def test_assorted_patterns():
    pattern = JSGPattern(r'[+-]?[0-9]+')
    assert pattern.matches("0")
    assert pattern.matches(str(-173))
    assert pattern.matches("+11720000845197308888890")
    assert pattern.matches("01")
    assert not pattern.matches("--17")
    assert not pattern.matches("1.0")

    pattern = JSGPattern(r'[+-]?[0-9]*\.[0-9]+')
    assert not pattern.matches("0")
    assert pattern.matches("0.0")
    assert pattern.matches(str(float(-173)))
    assert pattern.matches("1.0")
    assert pattern.matches("+11720000845197308888.0000000000")

    PN_CHARS_BASE = r'[A-Z]|[a-z]|[\u00C0-\u00D6]|[\u00D8-\u00F6]|[\u00F8-\u02FF]|[\u0370-\u037D]|' \
                    r'[\u037F-\u1FFF]|[\u200C-\u200D]|[\u2070-\u218F]|[\u2C00-\u2FEF]|[\u3001-\uD7FF]|' \
                    r'[\uF900-\uFDCF]|[\uFDF0-\uFFFD]|[\u10000-\uEFFFF]'

    HEX = r'[0-9]|[A-F]|[a-f]'
    UCHAR = r'\\\\u{HEX}{HEX}{HEX}{HEX}|\\\\U{HEX}{HEX}{HEX}{HEX}{HEX}{HEX}{HEX}{HEX}'.format(HEX=HEX)
    PN_CHARS_U = r'{PN_CHARS_BASE}|_'.format(PN_CHARS_BASE=PN_CHARS_BASE)
    PN_CHARS = r'{PN_CHARS_U}|\-|[0-9]|\\u00B7|[\u0300-\u036F]|[\u203F-\u2040]'.format(PN_CHARS_U=PN_CHARS_U)
    pattern = JSGPattern(r'({PN_CHARS}|\.|\:|\/|\\\\|\#|\@|\%|\&|{UCHAR})*'.format(PN_CHARS=PN_CHARS, UCHAR=UCHAR))
    assert pattern.matches("http://a.example/p\u0031")
    assert IRI.pattern.matches("http://a.example/p\u0031")
