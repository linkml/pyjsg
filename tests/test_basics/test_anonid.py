import pytest
from pyjsg.parser_impl.anonymousidentifierfactory import AnonymousIdentifierFactory


def test_anonymous_identifier_factory_default():
    fact = AnonymousIdentifierFactory()
    assert fact.next_id() == "_Anon1"
    assert fact.next_id() == "_Anon2"
    assert fact.is_anon("_Anon173")
    assert not fact.is_anon("_Anon01")
    assert not fact.is_anon("_Anona1")


def test_anonymous_identifier_factory_custom_prefix():
    fact = AnonymousIdentifierFactory("ID")
    assert fact.next_id() == "ID1"
    assert fact.next_id() == "ID2"
    assert fact.is_anon("ID1173")
    assert not fact.is_anon("ID01")
    assert not fact.is_anon("_Anon1")