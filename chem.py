# chem.py
#
# Find the correct solution of a complex equation using scipy.optimize.fsolve
#
# Muhammad Nauman
# UIN: 927008027
# 11/6/2018
# ENGR 102-213
#
# Lab 11b - 2

import math
import scipy.optimize
import numpy

p = int(input("Enter the total pressure of the mixture: "))


def eqn(x, p):
    """
    Finds x in the equation given p

    Parameters:
    -----------
    p: int, float
        The total pressure of the mixture
    x: int, float
        The value at which to calculate f_x

    Returns:
    --------
    f_x: int, float
        The value of the function at x
    """
    f_x = 0.05 - ((x/(1-x)) * (math.sqrt((2*p)/(2+x))))
    return f_x


if __name__ == "__main__":
    val = [0]
    val = numpy.array(val)
    ans = scipy.optimize.fsolve(eqn, val, args=(p))
    print(ans)
