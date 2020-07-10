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
    # Delete the pass statement below and insert your own code
    pass


# -----------------------------------------------------------------------------


class Polynomial:
    # Delete the pass statement below and insert your own code
    pass


print fib(0)
print fib(5)
print fib(10)
