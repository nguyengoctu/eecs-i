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
        pass

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


p1 = Polynomial([1, 0, 3])
p2 = Polynomial([100, 200])
print(p1)
print(p1.add(p2))
print(p1 + p2)
