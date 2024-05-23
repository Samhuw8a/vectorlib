from vectorlib import Vector
from hypothesis import given
from hypothesis.strategies import lists, integers, floats
# import pytest


@given(
    lists(floats(allow_nan=False), min_size=1),
    integers(min_value=0, max_value=100)
)
def test_float_getitem(items: list, index: int) -> None:
    if index < len(items):
        assert Vector(items)[index] == items[index]


@given(
    lists(floats(allow_nan=False), min_size=1),
    integers(min_value=0, max_value=100),
    integers()
)
def test_float_setitem_int(items: list, index: int, val: int) -> None:
    if index < len(items):
        v = Vector(items)
        v[index] = val
        assert v.components[index] == val


@given(
    lists(floats(allow_nan=False), min_size=1),
    integers(min_value=0, max_value=100),
    floats(allow_nan=False)
)
def test_float_setitem_float(items: list, index: int, val: int) -> None:
    if index < len(items):
        v = Vector(items)
        v[index] = val
        assert v.components[index] == val


@given(
    lists(integers(), min_size=1),
    integers(min_value=0, max_value=100)
)
def test_getitem(items: list, index: int) -> None:
    if index < len(items):
        assert Vector(items)[index] == items[index]


@given(
    lists(integers(), min_size=1),
    integers(min_value=0, max_value=100),
    integers()
)
def test_setitem_int(items: list, index: int, val: int) -> None:
    if index < len(items):
        v = Vector(items)
        v[index] = val
        assert v.components[index] == val


@given(
    lists(integers(), min_size=1),
    integers(min_value=0, max_value=100),
    floats(allow_nan=False)
)
def test_setitem_float(items: list, index: int, val: int) -> None:
    if index < len(items):
        v = Vector(items)
        v[index] = val
        assert v.components[index] == val
