# Program for Plotting Functions
#
# Plots a given function, first and second derivatives, and min/maxes
#
# Alexander M Bogdan
# Patrick Zhong
# Muhammad Nauman
# Daniel Huck
# November 19, 2018
# ENGR 102-213
#
# Lab 12 Activity 1 - Program for Plotting Functions

import part1 as p1


def func(x):
    return (x ** (4/5)) * ((x - 4) ** 2)


def funcD(x):
    return (2 * (x - 4) * (7 * x - 8)) / (5 * x ** (1/5))


def funcD2(x):
    return 5

p1.run(func, funcD, None, -1, 6)
