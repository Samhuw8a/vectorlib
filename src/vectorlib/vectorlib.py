from __future__ import annotations
from typing import Sequence, Union, Any
from math import sqrt

FloatOrInt = Union[float, int]


class Vector:
    """a python representation of a mathmatical Vector"""

    def __init__(self, components: Sequence[FloatOrInt]) -> None:
        self.components: tuple = tuple(components)

    def __repr__(self) -> str:
        return f"Vector({tuple(self.components)})"

    def __len__(self) -> int:
        return len(self.components)

    def __hash__(self) -> int:
        return sum(self.components)

    def __eq__(self, other: Any) -> bool:
        if not isinstance(other, Vector):
            return False
        return other.components == self.components

    def __add__(self, other: Vector) -> Vector:
        if not isinstance(other, Vector):
            raise TypeError("Addition is only suported between Vectors.")
        elif len(other) != len(self):
            raise TypeError(
                f"Vector of len:{len(other)} can't be added to Vector of len:{len(self)}"
            )

        new_comp = [s + o for s, o in zip(self.components, other.components)]
        return Vector(new_comp)

    def __sub__(self, other: Vector) -> Vector:
        if not isinstance(other, Vector):
            raise TypeError("Addition is only suported between Vectors.")
        elif len(other) != len(self):
            raise TypeError(
                f"Vector of len:{len(other)} can't be added to Vector of len:{len(self)}"
            )

        new_comp = [s - o for s, o in zip(self.components, other.components)]
        return Vector(new_comp)

    def __neg__(self) -> Vector:
        raise NotImplementedError()

    def __pos__(self) -> Vector:
        raise NotImplementedError()

    def __abs__(self) -> FloatOrInt:
        return sqrt(sum((i**2 for i in self.components)))

    def cross(self, other: Vector) -> Vector:
        raise NotImplementedError()

    def scalar(self, other: Vector) -> FloatOrInt:
        raise NotImplementedError()


def main() -> int:
    v = Vector((1, 2, 4))
    a = Vector((5, 3, 2))
    print(v + a)
    print(v + a - v == a)
    print(abs(v))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())