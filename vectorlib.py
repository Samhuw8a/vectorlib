from __future__ import annotations
from typing import Sequence, Union, Optional

FloatOrInt = Union[float, int]


class Vector:
    """a python representation of a mathmatical Vector"""

    def __init__(self, *, components: Optional[Sequence[FloatOrInt]] = None) -> None:
        pass

    @classmethod
    def from_point(cls, point: Sequence[FloatOrInt]) -> Vector:
        return Vector()

    def __add__(self, other):
        pass

    def __sub__(self, other):
        pass

    def __mul__(self, other):
        pass

    def __div__(self, other):
        pass

    def __truediv__(self, other):
        pass

    def __neg__(self):
        pass

    def __pos__(self):
        pass

    def __abs__(self):
        pass

    def __invert__(self):
        pass


def main() -> int:
    v = Vector.from_point((1, 3))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
