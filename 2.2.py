# UsingARootFindingModule.py
#
# This program does stuff
#
# Patrick Zhong
# Muhammad Nauman
# Daniel Huck
# Alexander Bogdan
# 11/5/18
# ENGR 102-213

import numpy
import math as m


def polynom_eqn(x):
    """
    compute the cubic equation
    parameters
    ----------
    x:float,int, numpy.array
    i: list
        coefficient values for polynomial
    Returns
    -------
    fn_x: float, int, numpy.array
        value of cubic equation at x
    """
    fn_x = 0
    for q in range(len(i)):
        fn_x += i[q] * x ** (len(i) - q)

    return (fn_x)


def bisect(tol, left, right, maxtries):
    """
    :param
    tol:  float,int
    left: float, int
        lower bounds for search
    right: float, int
        upper bounds for search
    maxtries: int
        limit on number of iterations
    f: function
        calculates the polynomial function based on the inputs
    :return:
    root: float, int, numpy.array
        x values for which the function = 0
    tries: int
        number of tries to find the root
    """
    i = left
    j = right

    signI = numpy.sign(polynom_eqn(i))
    signJ = numpy.sign(polynom_eqn(j))

    tries = 0

    if signI == 0:  # found root
        return i, tries

    if signJ == 0:  # found root
        return j, tries

    root = left  # start with left bound

    while (abs(polynom_eqn(root)) > tol) | (tries < maxtries):  # exit if within tolerance or exceeded max tries
        tries += 1

        root = (i + j) / 2  # bisection
        sign = numpy.sign(polynom_eqn(root))
        if sign == 0:  # found root
            return j, tries

        if sign == signI:
            i = root  # set midpoint as left bracket
        else:
            j = root  # set midpoint as right bracket

    return root, tries  # found root


if __name__ == '__main__':

    i = []
    a = float(input("\nEnter the value of the first coefficient: "))
    while a != -666:
        i.append(a)
        a = float(input("\nEnter the value of the next coefficient(Enter A when you are done: "))

    # SOURCE https://en.wikipedia.org/wiki/Properties_of_polynomial_roots#Based_on_the_Rouch%C3%A9_theorem
    right = 0  # Rouche's theorem for upper magnitude of roots
    for n in i:
        right += abs(n) / abs(i[0])
        left = - right

    maxtries = float(input("\nEnter the maximum number of tries: "))

    if right < left:  # reorder left and right bounds
        temp = right
        right = left
        left = temp

    print("\nLeft bound: " + str(left))
    print("\nRight bound: " + str(right))

    root, tries = bisect(10E-6, left, right, maxtries)  # find roots

    if tries >= maxtries:  # maximum tries reached
        print("\bMaximum tries exceeded - no root found.")
    else:
        print("\nRoot approximated at x = " + str(root))
        print("f(x): " + str(polynom_eqn(root)))
        print("\nTries taken: " + str(tries))
