#
# File:   designLab01Work.py
# Author: 6.01 Staff
# Date:   02-Sep-11
#
# Below are templates for your answers to three parts of Design Lab 1

# -----------------------------------------------------------------------------
from cmath import sqrt
import unittest


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
        return self.add(other)

    def __mul__(self, other):
        return self.mul(other)


# -----------------------------------------------------------------------------


class Polynomial:
    def __init__(self, coefficients):
        self.coeffs = coefficients

    def coeff(self, i):
        """
        :param i:
        :return: return the coefficient of the x^i term of the polynomial
        """
        return self.coeffs[len(self.coeffs) - i - 1]

    def add(self, other):
        """
        :param other:
        :return: a new Polynomial representing the sum of Polynomials self and other
        """
        if len(self.coeffs) > len(other.coeffs):
            lower_order_coeffs = other.coeffs
            new_coeffs = self.coeffs.copy()
        else:
            lower_order_coeffs = self.coeffs
            new_coeffs = other.coeffs.copy()

        i = len(new_coeffs) - 1
        j = len(lower_order_coeffs) - 1
        while j >= 0:
            new_coeffs[i] += lower_order_coeffs[j]
            i -= 1
            j -= 1
        return Polynomial(new_coeffs)

    def __add__(self, other):
        return self.add(other)

    def mul(self, other):
        """
        :param other:
        :return: a new Polynomial representing the product of Polynomials self and other
        """
        new_len = len(self.coeffs) + len(other.coeffs) - 1
        new_coeffs = [0] * new_len
        for i in range(len(self.coeffs)):
            for j in range(len(other.coeffs)):
                new_coeffs[i + j] += self.coeffs[i] * other.coeffs[j]
        return Polynomial(new_coeffs)

    def __mul__(self, other):
        return self.mul(other)

    def __str__(self):
        s = ''
        for i in range(len(self.coeffs)):
            order = len(self.coeffs) - i - 1
            if self.coeffs[i] != 0:
                s += str(self.coeffs[i])
                if order >= 2:
                    s += ' z**' + str(order)
                elif order == 1:
                    s += ' z'
                if order > 0:
                    s += ' + '
        return s

    def val(self, v):
        """
        :param v:
        :return: the numerical result of evaluating the polynomial when x equals v
        """
        result = 0
        for i in range(len(self.coeffs)):
            order = len(self.coeffs) - i - 1
            result += self.coeffs[i] * v ** order
        return result

    def __call__(self, x):
        return self.val(x)

    def roots(self):
        """
        :return: a list containing the roots of first or second order polynomial
        """
        roots = []
        if len(self.coeffs) >= 4 or len(self.coeffs) <= 1:
            return "Impossible to handle this polynomial!"

        if len(self.coeffs) == 2:
            if self.coeffs[0] == 0:
                roots = ["Infinity"]
            else:
                roots = [(-1 * self.coeffs[1] / self.coeffs[0])]
            return roots

        a = self.coeffs[0]
        b = self.coeffs[1]
        c = self.coeffs[2]

        if a == 0:
            if b == 0:
                roots = ["Infinity"]
            else:
                roots = [-c / b]
        else:
            delta = b * b - 4 * a * c
            if delta != 0:
                roots = [(-b + sqrt(delta)) / (2 * a), (-b - sqrt(delta)) / (2 * a)]
            elif delta == 0:
                roots = [-b / (2 * a)]
        return roots


p1 = Polynomial([1, 2, 3])
print(p1)
p2 = Polynomial([100, 200])
print(p1.add(p2))
print(p1 + p2)
print(p1(1))
print(p1(-1))
print((p1 + p2)(10))
print(p1.mul(p1))
print(p1 * p1)
print(p1 * p2 + p1)
print(p1.roots())
print(p2.roots())
p3 = Polynomial([3, 2, -1])
print(p3.roots())
print((p1 * p1).roots())
