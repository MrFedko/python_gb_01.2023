from cmath import sqrt


def negative(a: complex, b: complex, c: complex):
    discr: complex = b * b - 4 * a * c
    x1: complex = (-b + sqrt(discr)) / (2 * a)
    x2: complex = (-b - sqrt(discr)) / (2 * a)
    return discr, x1, x2
