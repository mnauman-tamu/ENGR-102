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


from scipy.misc import *
import numpy as np
import matplotlib.pyplot as plot

dx = 0.5


def funcDer(x, func):
    """
    Returns value of numerically calculated derivative of func at x
    """
    return derivative(func, x, dx)


def funcDer2(x, func):
    """
    Returns value of numerically calculated second derivative of func at x
    """
    return derivative(funcDer, x, dx, n=1, args=[func])


def run(func, funcD, funcD2, xL, xR):
    """
    Draws func (function), funcD (derivative) and funcD@ (second derivative) in the given bounds (xL - xR)
    If funcD is None (not provided) it is calculated with funcDer
    If funcD2 is None (not provided) it is calculated with funcDer2
    """

    xV = np.linspace(xL, xR, 200)
    fV = np.fromiter((func(xi) for xi in xV), xV.dtype, count=len(xV))

    if funcD is None:
        fV_D = np.fromiter((funcDer(xi, func) for xi in xV), xV.dtype, count=len(xV))
    else:
        fV_D = np.fromiter((funcD(xi) for xi in xV), xV.dtype, count=len(xV))

    if funcD2 is None:
        fV_D2 = np.fromiter((funcDer2(xi, func) for xi in xV), xV.dtype, count=len(xV))
    else:
        fV_D2 = np.fromiter((funcD2(xi) for xi in xV), xV.dtype, count=len(xV))

    critsX = []
    critsY = []

    prevSign = -2
    for i in range(1, len(xV) - 1):
        yL = fV[i - 1]
        yM = fV[i]
        yR = fV[i + 1]

        if (yL > yM and yR > yM) or (yL < yM and yR < yM):
            critsX.append(xV[i])
            critsY.append(fV[i])


    plot.scatter(xV, fV, color="#0064FF", s=1.5)
    plot.scatter(xV, fV_D, color="orange", s=1.5)
    plot.scatter(xV, fV_D2, color="#ff5050", s=1.5)
    plot.scatter(critsX, critsY, color="black", s=16)
    plot.grid(True)
    plot.show()


if __name__ == "__main__":
    run(
        lambda x: 3 * x ** 2 + 2 * x + 1,
        lambda x: 6 * x + 2,
        lambda x: 6, -6, 6)
