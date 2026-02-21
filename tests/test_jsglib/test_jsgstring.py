from tests.test_jsglib.iri_defn import *


def test_wildcard(do_string_test):
    class WildCard(JSGString):
        pattern = JSGPattern(r'.*')
        python_type = object

    do_string_test(WildCard, "")
    do_string_test(WildCard, False)
    do_string_test(WildCard, "any block of text")
    do_string_test(WildCard, "^<80>߿ࠀ࿿က쿿퀀퟿�𐀀𿿽񀀀󿿽􀀀􏿽$/")
    do_string_test(WildCard, "\n\uFDF0*")


def test_fixedvalues(do_string_test):
    class IRI(JSGString):
        pattern = JSGPattern(r'http:\/\/www\.w3\.org\/ns\/shex\.jsonld')
        
    do_string_test(IRI,"http://www.w3.org/ns/shex.jsonld")
    do_string_test(IRI,"http://www.w3.org/ns/shex/jsonldx", False)
    do_string_test(IRI,"http://www.w3.org/ns/shex/jsonld ", False)
    do_string_test(IRI,"http://www.w3.org/ns/shex/jsonld\n", False)
    do_string_test(IRI," http://www.w3.org/ns/shex/jsonld", False)


def test_alternatives(do_string_test):
    class Alts(JSGString):
        pattern = JSGPattern(r'iri|bnode|nonliteral|literal')
    do_string_test(Alts,'iri')
    do_string_test(Alts,'literal')
    do_string_test(Alts,'nonliteral')
    do_string_test(Alts,'bnode')
    do_string_test(Alts,'node', False)
    do_string_test(Alts,'bnod', False)
    do_string_test(Alts,'IRI', False)
    do_string_test(Alts,' iri', False)
    do_string_test(Alts,'iri ', False)


def test_bool(do_string_test):
    class BOOL(JSGString):
        pattern = JSGPattern(r'[Tt]rue|[Ff]alse')
        python_type = (str, bool)

    do_string_test(BOOL, 'true')
    do_string_test(BOOL, 'false')
    do_string_test(BOOL, 'TRUE', False)
    do_string_test(BOOL, 'True')
    do_string_test(BOOL, 'False')
    do_string_test(BOOL, True)
    do_string_test(BOOL, False)
    do_string_test(BOOL, 0, False)
    do_string_test(BOOL, None, False)


def test_assorted(do_string_test):
    class INT(JSGString):
        pattern = JSGPattern(r'[+-]?[0-9]+')
        
    do_string_test(INT, "0")
    do_string_test(INT, str(-173))
    do_string_test(INT, "+11720000845197308888890")
    do_string_test(INT, "01")
    do_string_test(INT, "--17", False)
    do_string_test(INT, "1.0", False)

    class NUM(JSGString):
        pattern = JSGPattern(r'[+-]?[0-9]*\.[0-9]+')
        
    do_string_test(NUM, "0", False)
    do_string_test(NUM, "0.0")
    do_string_test(NUM, str(float(-173)))
    do_string_test(NUM, "1.0")
    do_string_test(NUM, "+11720000845197308888.0000000000")

    do_string_test(IRI, "http://a.example/p\u0031")
