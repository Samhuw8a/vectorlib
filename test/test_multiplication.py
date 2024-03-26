from vectorlib import Vector
from hypothesis import given
from hypothesis.strategies import lists, floats, integers
import pytest


@given(lists(integers(), min_size=1), floats(allow_infinity=False, allow_nan=False))
def test_multiplication_float(v: list, n: float) -> None:
    res = Vector([i * n for i in v])
    assert Vector(v) * n == res


@given(lists(integers(), min_size=1), integers())
def test_multiplication_int(v: list, n: int) -> None:
    res = Vector([i * n for i in v])
    assert Vector(v) * n == res


@given(lists(integers(), min_size=1), floats(allow_infinity=False, allow_nan=False))
def test_r_multiplication_float(v: list, n: float) -> None:
    res = Vector([i * n for i in v])
    assert n * Vector(v) == res


@given(lists(integers(), min_size=1), integers())
def test_r_multiplication_int(v: list, n: int) -> None:
    res = Vector([i * n for i in v])
    assert n * Vector(v) == res


def test_raises():
    with pytest.raises(TypeError):
        Vector((1, 2)) * Vector((1, 3))
        Vector((1, 2)) * "af"
