#!/usr/bin/env python

from math import hypot


class Vector:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    # __repr__ called by repr built-in getting the string representation of object for inspection and debug
    # when __str__ is not available, Python calls __repr__ as a fallback
    # always consider __repr__ as first choice
    def __repr__(self):
        print(self.__class__.__name__)
        return f'Vector({self.x}, {self.y})'

    # __str__ called by str() used by print function for display
    def __str__(self):
        print(self.__class__.__name__)
        return f'Vector({self.x}, {self.y})'

    def __abs__(self):
        return hypot(self.x, self.y)

    # by default, instances of user-defined classes are considered truthy, unless either __bool__ or __len__ is implemented
    # bool(x) built-in calls x.__bool__(). If __bool__ is not implemented, Python tries to call x.__len__().
    # for any value other than zero, it returns True; otherwise False.
    def __bool__(self):
        return bool(abs(self))

    # new objects are created and returned, no operands are modified
    def __add__(self, other):
        x = self.x + other.x
        y = self.y + other.y
        return Vector(x, y)

    # new objects are created and returned, no operands are modified
    def __mul__(self, scalar):
        return Vector(self.x * scalar, self.y * scalar)


if __name__ == '__main__':
    v1 = Vector(2, 4)
    v2 = Vector(2, 1)
    print(v1 + v2)
    print(abs(v1))
    print(v1 * 3)
