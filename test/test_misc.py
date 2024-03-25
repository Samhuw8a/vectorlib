from vectorlib import Vector
from hypothesis import given
from hypothesis.strategies import lists, integers


@given(lists(integers()))
def test_equal(val: list) -> None:
    assert Vector(val) == Vector(val)
    assert Vector(val) == Vector(tuple(val))
