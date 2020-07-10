#
# File:   designLab01Work.py
# Author: 6.01 Staff
# Date:   02-Sep-11
#
# Below are templates for your answers to three parts of Design Lab 1

# -----------------------------------------------------------------------------


def fib(n):
    result = 1
    if n < 1:
        return result
    for i in range(2, n + 1):
        result *= i
    return result


# -----------------------------------------------------------------------------


class V2:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return 'V2[' + str(self.x) + ', ' + str(self.y) + ']'

    def getX(self):
        return self.x

    def getY(self):
        return self.y

    def add(self, v):
        return V2(v.getX() + self.x,
                  v.getY() + self.y)

    def mul(self, factor):
        return V2(factor * self.x,
                  factor * self.y)

    def __add__(self, other):
        return V2(self.getX() + other.getX(),
                  self.getY() + other.getY())

    def __mul__(self, other):
        return V2(self.getX() * other,
                  self.getY() * other)


# -----------------------------------------------------------------------------


class Polynomial:
    # Delete the pass statement below and insert your own code
    pass


a = V2(1.0, 2.0)
b = V2(2.2, 3.3)
print(a.add(b))
print(a + b)
print(a.mul(2))
print(a * 2)
print(a.add(b).mul(-1))
print((a + b) * -1)
