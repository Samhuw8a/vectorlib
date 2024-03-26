from __future__ import annotations
from typing import Union, Any, List, Tuple
from math import sqrt

FloatOrInt = Union[float, int]
Components = Union[List[FloatOrInt], Tuple[FloatOrInt, ...]]


class Vector:
    """a python representation of a mathmatical Vector"""

    def __init__(self, components: Components) -> None:
        if not isinstance(components, (tuple, list)):
            raise TypeError("Vector only takes tuples or lists as parameters")
        if len(components) == 0:
            raise ValueError("A Vector can't be zero dimensional")

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
            raise ValueError(
                f"Vector of len:{len(other)} can't be added to Vector of len:{len(self)}"
            )

        new_comp = [s + o for s, o in zip(self.components, other.components)]
        return Vector(new_comp)

    def __sub__(self, other: Vector) -> Vector:
        if not isinstance(other, Vector):
            raise TypeError("Addition is only suported between Vectors.")
        elif len(other) != len(self):
            raise ValueError(
                f"Vector of len:{len(other)} can't be added to Vector of len:{len(self)}"
            )

        new_comp = [s - o for s, o in zip(self.components, other.components)]
        return Vector(new_comp)

    def __mul__(self, other: FloatOrInt) -> Vector:
        if not isinstance(other, (float, int)):
            raise TypeError("Vector multiplication is only supported for numbers")
        new_comp = [i * other for i in self.components]
        return Vector(new_comp)

    def __rmul__(self, other: FloatOrInt) -> Vector:
        return self.__mul__(other)

    def __neg__(self) -> Vector:
        new_comp = [i.__neg__() for i in self.components]
        return Vector(new_comp)

    def __pos__(self) -> Vector:
        return self

    def __abs__(self) -> FloatOrInt:
        return sqrt(sum((i**2 for i in self.components)))

    def cross(self, other: Vector) -> Vector:
        if not isinstance(other, Vector):
            raise TypeError(
                "the crossproduct can only be calculated between to 3D Vectors"
            )
        if len(self) != 3 or len(other) != 3:
            raise ValueError(
                f"the crossproduct can only be calculated between to 3D Vectors got: {len(self)}:{len(other)}"
            )
        a1 = self.components[1] * other.components[2]
        a2 = self.components[2] * other.components[1]

        b1 = self.components[2] * other.components[0]
        b2 = self.components[0] * other.components[2]

        c1 = self.components[0] * other.components[1]
        c2 = self.components[1] * other.components[0]
        new_comp = (a1 - a2, b1 - b2, c1 - c2)
        return Vector(new_comp)

    def scalar(self, other: Vector) -> FloatOrInt:
        raise NotImplementedError()


def main() -> int:
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
