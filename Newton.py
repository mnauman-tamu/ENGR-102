# Newton.py
#
# Use Newton's method to find roots of an equation
#
# Muhammad Nauman, Alexander Bogdan, Daniel Huck, Patrick Zhong
# 11/6/2018
# ENGR 102-213
#
# Lab 11 - 1

import scipy.optimize
import numpy


def eq(x, pars):
    """
    Solves the equation for a general nth-order polynomial

    Parameters:
    -----------
    x: int, float
        The value at which to compute the polynomial
    pars: list
        The list of coefficients

    Returns:
    --------
    f_x: int, float
        The value of the equation at x
    """
    n = len(pars)
    f_x = 0
    for i in range(n):
        f_x += pars[i]*x**(n-i)
    return f_x


def der(x, pars):
    """
    Solves the derivative of the equation for a general nth-order polynomial

    Parameters:
    -----------
    x: int, float
        The value at which to compute the polynomial
    pars: list
        The list of coefficients

    Returns:
    --------
    fdx: int, float
        The value of the derivative of the equation at x
    """
    n = len(pars)
    fdx = 0
    for i in range(n-1):
        fdx += (n-i)*pars[i]*x**(n-i-1)
    return fdx


def newton_step(root_guess, equation, derivative, par):
    """
    Performs one step of Newton's method

    Parameters:
    -----------
    root_guess: int, float
        The current guess for the root
    equation: func
        The equation of the polynomial solved at root_guess
    derivative: func
        The derivative of the function at root_guess
    par: list
        The coefficients of the equation

    Returns:
    --------
    new_guess: int, float
        A new value of the root using the Newton's method
    """
    new_guess = root_guess - (equation(root_guess, par)/derivative(root_guess, par))
    return new_guess


def newton_final(x0, equation, derivative, one_step, par, tol=10**-8, maxtries=10**5):
    """
    Parameters:
    -----------
    tol:  float,int
        The tolerance of error
    maxtries: int
        limit on number of iterations
    x0: int, float
        The current guess
    equation: function
        calculates the polynomial function based on the inputs
    derivative: func
        The derivative of the function at root_guess
    one_step: func
        The function that calculates one-step of a newton method
    par: list
        The coefficients of the equation

    Returns:
    --------
    root: float, int, numpy.array
        x values for which the function = 0
    tries: int, string
        number of tries to find the root or error message if exceeded maxtries
    """
    tries = 0

    while abs(eq(x0, par)) > tol and tries < maxtries:  # exit if within tolerance or exceeded max tries
        tries += 1
        x0 = one_step(x0, equation, derivative, par)
    root = x0

    if tries == maxtries:
        tries = "The root-finding method did not converge on a root"

    return (root, tries) # found root


if __name__ == "__main__":
    order = int(input("What is the order of the polynomial: "))
    a = []
    for i in range(order):
        c = float(input("Enter #" + str(i+1) + " coefficient: "))
        a.append(c)
    guess = float(input("Enter a guess for a root of the polynomial: "))
    print("f(x) = " + str(eq(guess, a)))
    print("f'(x) = " + str(der(guess, a)))
    print("First root estimate is: " + str(newton_step(guess, eq, der, a)))
    print()
    a = [3., 4., 5., 6.]
    root = newton_final(guess, eq, der, newton_step, a)
    print("The root estimation is: " + str(root[0]) + "and it took " + str(root[1]) + " tries.")
    guess = numpy.array(guess)
    print()
    real_root = scipy.optimize.fsolve(eq, guess, args=(a))
    print("The fsolve answer is " + str(real_root))
    diff = abs(root[0]-real_root[0])
    print("The difference between the two is: " + str(diff))
    print("The error is within the tolerance and is very small")
