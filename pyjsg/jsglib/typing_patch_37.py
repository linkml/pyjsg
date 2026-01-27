import sys
from collections.abc import Iterable

# Typing_patch module for Python 3.7+

if sys.version_info >= (3, 7):
    from typing import Dict, Any, Union, ForwardRef, Callable, Type, _eval_type


def proc_forward(etype, namespace: Dict[str, Any]):
    """ Resolve etype to an actual type if it is a forward reference """
    return _eval_type(etype, namespace, namespace) if type(etype) is ForwardRef else etype


def is_union(etype) -> bool:
    """ Determine whether etype is a Union """
    if sys.version_info >= (3, 14):
        from types import UnionType
        from typing import get_origin
        return get_origin(etype) in {Union, UnionType}

    return getattr(etype, '__origin__', None) is not None and \
           getattr(etype.__origin__, '_name', None) and\
           etype.__origin__._name == 'Union'


def is_dict(etype) -> bool:
    """ Determine whether etype is a Dict """
    return issubclass(type(etype), dict)


def is_iterable(etype) -> bool:
    """ Determine whether etype is a List or other iterable """
    return getattr(etype, '__origin__', None) is not None and issubclass(etype.__origin__, Iterable)


def union_conforms(element: Union, etype, namespace: Dict[str, Any], conforms: Callable) -> bool:
    """ Determine whether element conforms to at least one of the types in etype

    :param element: element to test
    :param etype: type to test against
    :param namespace: Namespace to use for resolving forward references
    :param conforms: conformance test function
    :return: True if element conforms to at least one type in etype
    """
    return any(conforms(element, t, namespace) for t in etype.__args__)
