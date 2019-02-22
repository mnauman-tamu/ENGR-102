# ODE.py
#
# Simulate the World’s population from 1950 to 2050 using scipy.integrate.odeint
#
# Muhammad Nauman
# UIN: 927008027
# 11/11/2018
# ENGR 102-213
#
# Lab 11b - 3

import numpy as np
import scipy.integrate


def func(y, t):
    """
    Computes the function dy/dt

    :param y: [int]: The number of people in millions
    :param kgm: [float]: The max growth rate under unlimited conditions
    :param ymax: [int]: The carrying capacity in millions

    :return: dydt: [int, float]: The equation
    """
    dydt = 0.026*(1-(y/12000))*y*(2560/312)
    return dydt


def der(y, t0):
    """
    Computes the derivative of y at t0

    :param y: [int]: The value of which the derivative is computed
    :param t0: [int]: The value at which the derivative is computed

    :return: dy: [int, float]: The derivative at y
    """


# y0 = [2560.0, 2780.0, 3040.0, 3350.0, 3710., 4090.0, 4450.0, 4850., 5280.0, 5690.0, 6080.0]
y0 = [2560.0, 1950]
t = np.linspace(1950, 2000, 11)
sol = scipy.integrate.odeint(func, y0, t)
print(sol)
