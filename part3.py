# part3.py
#
# Using a Root-Finding Module
#
# Implements bisection method using user-defined functions
#
# Patrick Zhong
# Muhammad Nauman
# Daniel Huck
# Alexander Bogdan
# ENGR 102-213
#
# Lab 10 Activity 2.3 - Using a Root-Finding Module

from bisectionwk10_2 import *


def interpret(root, tries, maxtries, params):
    if tries >= maxtries:  # maximum tries reached
        print("\tMaximum tries exceeded - no root found.")
    #else:
        #print("\tThe bounds provided do not bracket the root.")
    else:
        print("\tRoot approximated at x = " + str(root))
        print("\tf(x): " + str(polynom_eqn(root, params)))
        print("\tTries taken: " + str(tries))


if __name__ == "__main__":
    params = [4]

    maxtries = 10000
    root, tries = bisect(10e-6, -4, 2, maxtries, params)  # find roots
    print("\nf(x) = 4:")
    interpret(root, tries, maxtries, params)

    params = [1, 5, 2]
    root, tries = bisect(10E-6, -4, 2, maxtries, params)  # find roots
    print("\nf(x) = x^2 + 5x + 2:")
    print("\tTrue root: -0.438")
    interpret(root, tries, maxtries, params)

    params = [1, 0, 0, 2, -2]
    root, tries = bisect(10E-6, -1, 4, maxtries, params)  # find roots
    print("\nf(x) = x^4 + 2x - 2:")
    print("\tTrue root: 0.798")
    interpret(root, tries, maxtries, params)
