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

    def __add__(self, other) -> Vector:
        raise NotImplementedError()

    def __sub__(self, other) -> Vector:
        raise NotImplementedError()

    def __neg__(self):
        raise NotImplementedError()

    def __pos__(self):
        raise NotImplementedError()

    def __abs__(self) -> FloatOrInt:
        raise NotImplementedError()


def main() -> int:
    v = Vector.from_point((1, 3))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
