# integration.py
#
# Estimate the integral of a function using user-defined functions
#
# Muhammad Nauman
# UIN: 927008027
# 10/29/2018
# ENGR 102-213
#
# Lab 10b - 3

import math

def integrand(x, par):
    """
    Defines a cubic polynomial

    Parameters
    ----------
    x: int, float
        The value at which the function should be computed
    par: list
        The coefficients a, b, c, and d in ax^3 + bx^2 + cx + d

    Returns
    -------
    fx: int, float
        The value of the function at x
    """

    fx = par[0] * x**3 + par[1] * x**2 + par[2] * x + par[3]
    return fx


def integration(x0, xf, par, segment = -12):
    """
    Performs integration using rectangles from x0 to xf in segment segments if segment is specified; otherwise use 10^-8 tolerance

     Parameters
    ----------
    x0: int, float
        The beginning value
    xf: int, float
        The end value
    par: list
        The coefficients a, b, c, and d in ax^3 + bx^2 + cx + d
    segment: int, optional
        Optional; number of segments for which integration is performed

    Returns
    -------
    integral: int, float
        The integral value of the function
    seg: int
        The number of segments computed
    err: float
        The estimated value of the error
    """

    integral_i = par[0] * ((x0**4)/4) + par[1] * ((x0**3)/3) + par[2] * ((x0**2)/2) + par[3]*x0
    integral_f = par[0] * ((xf**4)/4) + par[1] * ((xf**3)/3) + par[2] * ((xf**2)/2) + par[3]*xf

    true_integral = integral_f - integral_i
    err = true_integral
    integral = 0
    xi = x0

    if segment != -12:
        delta_x = ((xf - x0)/segment)
        for i in range(segment):
            h = (integrand(xi, par) + integrand((xi + delta_x), par))/2
            xi += delta_x
            integral += (delta_x * h)

    else:
        segment = 499900
        while math.fabs(err) > 10**-8:
            segment += 100
            delta_x = ((xf - x0) / segment)
            for i in range(segment):
                h = (integrand(xi, par) + integrand((xi + delta_x), par))/2
                xi += delta_x
                integral += (delta_x * h)
            err = true_integral - integral

    err = true_integral - integral
    return (integral, segment, err)


if __name__ == '__main__':
    ans = integration(0, 2, [1, 2, 3, 4], 50)
    print(ans)

    ans = integration(0, 4, [1, 2, 3, 4], 500)
    print(ans)

    ans = integration(0, 2, [1, 2, 3, 4])
    print(ans)

    ans = integration(0, 4, [1, 2, 3, 4])
    print(ans)

    ans = integration(0, 3.5, [5, 4, 0, 9], 500)
    print(ans)

    ans = integration(0, 3.5, [5, 4, 0, 9])
    print(ans)