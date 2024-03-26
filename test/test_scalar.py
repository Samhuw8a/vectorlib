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
def test_scalar_3(v1, v2) -> None:
    res = float(np.dot(v1, v2))
    assert Vector(v1).scalar(Vector(v2)) == res
