# integration11.py
#
# Estimate the probability of scoring 90% or lower using Gaussian PDF
#
# Muhammad Nauman
# UIN: 927008027
# 11/5/2018
# ENGR 102-213
#
# Lab 11b - 1

import math
import scipy.integrate
import numpy as np


def Gaussian(x, mean=73.4, s_d=12.4):
    """
    Computes the Gaussian PDF at the given x-value

    Parameter:
    ----------
    x: float, int
        The value at which the Gaussian PDF should be computed
    mean: float, int
        The mean of all values
    s_d: float, int
        The standard deviation

    Returns:
    -------
    f_x: float
        The Gaussian PDF at the given x
    """

    f_x = (1/(s_d*(math.sqrt(2*math.pi))))*(math.exp(-1*(((x-mean)**2)/(2*s_d**2))))
    return f_x


if __name__ == '__main__':
    y = scipy.integrate.quad(Gaussian, -np.inf, 90)
    print("The probability to score 90% or less is: " + str(y[0]*100) + "%")
