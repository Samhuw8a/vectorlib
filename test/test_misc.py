from vectorlib import Vector
from hypothesis import given
from hypothesis.strategies import lists, integers
import pytest


@given(lists(integers(), min_size=1))
def test_equal(val: list) -> None:
    assert Vector(val) == Vector(val)
    assert Vector(val) == Vector(tuple(val))


def test_init_raises():
    with pytest.raises(TypeError):
        Vector("asdf")
        Vector(1)
        Vector(1.0)
        Vector({1, 2, 4})
        Vector((1, 2, 4, float("nan")))
        Vector([1, 2, 4, float("nan")])
    with pytest.raises(ValueError):
        Vector([])
        Vector(tuple())
