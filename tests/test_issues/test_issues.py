import pytest
from pyjsg.jsglib import JSGString, JSGPattern, Boolean


def test_issue_7():
    class LANGTAG(JSGString):
        pattern = JSGPattern(r'[a-zA-Z]+(\-([a-zA-Z0-9])+)*')

    x = LANGTAG("de")
    assert x != "fr"


def test_issue_7_bool():
    with pytest.raises(ValueError):
        Boolean("Aardvark")
    b2 = Boolean("False")
    b1 = b2
    assert not b1
    with pytest.raises(ValueError):
        Boolean(0)


def test_none_as_string_instance():
    class S(JSGString):
        pattern = JSGPattern(r'[a-zA-Z]+')

    assert isinstance('abc', S)
    assert not isinstance('abc1', S)
    assert not isinstance('', S)
    assert not isinstance(None, S)


def test_issue_9():
    assert isinstance("abc", JSGString)
    assert isinstance("", JSGString)
    assert not isinstance(None, JSGString)
    assert not isinstance(1, JSGString)
    assert not isinstance([], JSGString)
    assert JSGString("abc")

    class T(JSGString):
        pass
    assert T("abc")

    class TP(JSGString):
        pattern = JSGPattern("[a-zA-Z]+")
    assert TP("abc")