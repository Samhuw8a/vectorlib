from vectorlib import Vector
from hypothesis import given
from hypothesis.strategies import lists, integers


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
