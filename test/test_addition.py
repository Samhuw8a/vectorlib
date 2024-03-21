from vectorlib import Vector


def test_addition() -> None:
    v1 = Vector((3, 1, 7))
    v2 = Vector((2, 5, 1))
    res = Vector((5, 6, 8))
    assert v1 + v2 == res
