from vectorlib import Vector
from hypothesis import given
from hypothesis.strategies import lists, integers
import pytest
import numpy as np

MAX = 100_000_000


@given(
    lists(integers(max_value=MAX, min_value=-MAX), min_size=3, max_size=3),
    lists(integers(max_value=MAX, min_value=-MAX), min_size=3, max_size=3),
)
def test_crossproduct(v1: list, v2: list) -> None:
    res = [int(i) for i in np.cross(v1, v2)]
    assert Vector(v1).cross(Vector(v2)) == Vector(res)


def test_raises_dimension():
    with pytest.raises(ValueError):
        Vector((1, 2, 3)).cross(Vector((1, 2)))
        Vector((2, 3)).cross(Vector((1, 2, 3)))
        Vector((1, 2)).cross(Vector((1, 2)))
        Vector((1, 2, 3, 4)).cross(Vector((1, 2, 3, 4)))


def test_raises_type():
    with pytest.raises(TypeError):
        Vector((1, 2, 3)).cross(2)
        Vector((1, 2, 3)).cross("asd")
        Vector((1, 2, 3)).cross(1.0)
        Vector((1, 2, 3)).cross([1, 4])
        Vector((1, 2, 3)).cross((1, 4))
