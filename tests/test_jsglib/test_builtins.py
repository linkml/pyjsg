import pytest

from pyjsg.jsglib import String, JSGPattern, Number, Integer, Boolean, JSGNull, Empty


def test_string(do_builtin_test):
    do_builtin_test(String, "a simple string")
    do_builtin_test(String, True, "true", fail=True)
    do_builtin_test(String, False, "false", fail=True)
    do_builtin_test(String, 143, "143", fail=True)
    do_builtin_test(String, 95.221E+5, "9522100.0", fail=True)
    do_builtin_test(String, "95.221E+5")
    do_builtin_test(String, "^<80>߿ࠀ࿿က쿿퀀퟿�𐀀𿿽񀀀󿿽􀀀􏿽$/")
    do_builtin_test(String, "^\/\t\n\r\-\\\u0061\U0001D4B8$", "^\\/\t\n\r\\-\\a𝒸$")
    do_builtin_test(String, None, fail=True)
    do_builtin_test(String, -119, "-119", fail=True)

    class PAT_STR(String):
        pattern = JSGPattern(r'[a-z][0-9]+')

    do_builtin_test(PAT_STR, 'a143')

    with pytest.raises(ValueError):
        PAT_STR('17')

    class INT_STR(String):
        pattern = JSGPattern(r'0|([1-9][0-9]*)')

    do_builtin_test(INT_STR, "17")

    with pytest.raises(ValueError):
        INT_STR("-17")
    with pytest.raises(ValueError):
        INT_STR("something")


def test_number(do_builtin_test):
    isinstance(do_builtin_test(Number, 42), float)
    isinstance(do_builtin_test(Number, -173), float)
    isinstance(do_builtin_test(Number, 0.1723), float)
    with pytest.raises(ValueError):
        Number("+173.0003E-5")          # JSON doesn't allow plus signs
    do_builtin_test(Number, "-173.0003E-5", -0.001730003)

    class POS_NUMBER(Number):
        pattern = JSGPattern(r'(0|[1-9][0-9]*)(.[0-9]+)?([eE][+-]?[0-9]+)?')

    do_builtin_test(POS_NUMBER, 1003675)
    with pytest.raises(ValueError):
        POS_NUMBER(-1)
    with pytest.raises(ValueError):
        POS_NUMBER("-117.438")


def test_integer(do_builtin_test):
    isinstance(do_builtin_test(Integer, 42), int)
    isinstance(do_builtin_test(Integer, -173), int)
    isinstance(do_builtin_test(Integer, 0), int)
    isinstance(do_builtin_test(Integer, "-119221", -119221), int)
    with pytest.raises(ValueError):
        Integer(0.1723)
    with pytest.raises(ValueError):
        Integer("-173.0003E-5")
    with pytest.raises(ValueError):
        Integer("a")
    with pytest.raises(ValueError):
        Integer("")
    with pytest.raises(ValueError):
        Integer(False)
    with pytest.raises(ValueError):
        Integer(None)

    class NEG_INTEGER(Integer):
        pattern = JSGPattern(r'-(0|[1-9][0-9]*)')

    isinstance(do_builtin_test(NEG_INTEGER, -119), int)
    with pytest.raises(ValueError):
        NEG_INTEGER(17)


def test_bool(do_builtin_test):
    isinstance(do_builtin_test(Boolean, True), bool)
    isinstance(do_builtin_test(Boolean, "True", True), bool)
    isinstance(do_builtin_test(Boolean, "true", True), bool)
    isinstance(do_builtin_test(Boolean, False), bool)
    isinstance(do_builtin_test(Boolean, "False", False), bool)
    isinstance(do_builtin_test(Boolean, "false", False), bool)
    with pytest.raises(ValueError):
        Boolean(None)
    with pytest.raises(ValueError):
        Boolean(0)
    with pytest.raises(ValueError):
        Boolean("")

    class TRUE_ONLY(Boolean):
        pattern = Boolean.true_pattern

    isinstance(do_builtin_test(TRUE_ONLY, True), bool)
    with pytest.raises(ValueError):
        TRUE_ONLY(False)


def test_incompatible_pattern():
    class INCOMPAT(Integer):
        pattern = JSGPattern(r'[a-z]+')

    with pytest.raises(ValueError):
        INCOMPAT("a")

    with pytest.raises(ValueError):
        INCOMPAT(17)


def test_null():
    assert JSGNull(None).val is None
    assert JSGNull(JSGNull).val is None
    with pytest.raises(ValueError):
        JSGNull(Empty)
    with pytest.raises(ValueError):
        JSGNull('null')


def test_empty_type():
    """ Make sure that Empty is a class only thingie """
    assert Empty is Empty()

