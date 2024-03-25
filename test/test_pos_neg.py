from vectorlib import Vector
from hypothesis import given
from hypothesis.strategies import lists, integers


@given(lists(integers(), min_size=1))
def test_pos_neg_reversal(v: list):
    assert Vector(v) == +(-Vector(v))
    assert -Vector(v) == -(+Vector(v))
