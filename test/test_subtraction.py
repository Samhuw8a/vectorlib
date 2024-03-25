from vectorlib import Vector
from hypothesis import given
from hypothesis.strategies import lists, integers
import pytest


def calc_res(v1: list, v2: list) -> list:
    return [i - j for i, j in zip(v1, v2)]


@given(
    lists(integers(), min_size=1, max_size=1), lists(integers(), min_size=1, max_size=1)
)
def test_subtraction_1(v1: list, v2: list) -> None:
    res = calc_res(v1, v2)
    assert Vector(v1) - Vector(v2) == Vector(res)


@given(
    lists(integers(), min_size=3, max_size=3), lists(integers(), min_size=3, max_size=3)
)
def test_subtraction_3(v1: list, v2: list) -> None:
    res = calc_res(v1, v2)
    assert Vector(v1) - Vector(v2) == Vector(res)


@given(
    lists(integers(), min_size=4, max_size=4), lists(integers(), min_size=4, max_size=4)
)
def test_subtraction_4(v1: list, v2: list) -> None:
    res = calc_res(v1, v2)
    assert Vector(v1) - Vector(v2) == Vector(res)


def test_dimension_missmatch():
    with pytest.raises(ValueError):
        Vector((1, 3)) + Vector((1,))
        Vector((1, 4, 5)) + Vector((1,))
        Vector((1, 3)) + Vector((1, 2, 4))


def test_type_missmatch():
    with pytest.raises(TypeError):
        Vector(1, 2) + 3
        Vector(1, 2) + 1.0
        Vector(1, 2) + []
        Vector(1, 2) + ""
