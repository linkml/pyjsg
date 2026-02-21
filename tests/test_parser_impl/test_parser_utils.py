import keyword
from pyjsg.parser_impl.parser_utils import flatten, flatten_unique, as_set, is_valid_python, esc_kw


def test_flatten():
    assert flatten([]) == []
    assert flatten([1, [2], [3, [4, 5], [6], []]]) == [1, 2, 3, 4, 5, 6]
    assert flatten([["a", "c"], ["a", "e"], ["e", "a"]]) == ["a", "c", "a", "e", "e", "a"]


def test_flatten_unique():
    assert flatten_unique([]) == []
    assert flatten_unique([1, [2], [3, [4, 5], [[[6]]], []]]) == [1, 2, 3, 4, 5, 6]
    assert flatten_unique([["a", "c"], ["a", "e"], ["e", "a"]]) == ["a", "c", "e"]


def test_as_set():
    assert as_set([]) == set()
    assert as_set([1, [2], [3, [4, 5], [[[6]]], []]]) == {1, 2, 3, 4, 5, 6}
    assert as_set([["a", "c"], ["a", "e"], ["e", "a"]]) == {"a", "c", "e"}


def test_is_valid_python():
    assert is_valid_python('a')
    assert is_valid_python('is_valid_python')
    assert not is_valid_python('def')
    assert not is_valid_python('class')
    assert not is_valid_python('a 1')
    assert not is_valid_python('a-1')
    assert not is_valid_python('1a')


def test_esc_kw():
    assert esc_kw('a') == 'a'
    assert esc_kw('def') == 'def_'
    for k in keyword.kwlist:
        assert esc_kw(k) == k + '_'
        assert esc_kw(k + 'x') == k + 'x'