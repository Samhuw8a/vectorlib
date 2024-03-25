from vectorlib import Vector


def test_abs():
    assert abs(Vector((1, 1, 1, 2, 3))) == 4
    assert abs(Vector((3, 4))) == 5
