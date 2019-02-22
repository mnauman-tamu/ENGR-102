# roots.py
#
# This program creates functions to solve for the roots of an equation and
# tests these functions with polynomials.
#
# S. Socolofsky
# ENGR 102
# November 2018


# Create a function for a general polynomial
def polynomial(x, a):
    """
    Function to compute an arbitrary polynomial

    Computes the polynomial f_n(x) = a_0x^n + a_1x^(n-1) + a_2x^(n-2) + ... +
    a_nx^(n-n) at the given point x, where [a_0, a_1, a_2, ... a_n] are
    coefficient values provided in the input list a. The order of the
    polynomial is one less than the length of the list.

    Parameters
    ----------
    x : float
        Coordinate value for the independent variable of the function
    a : list of floats
        Coefficients of the polynomial organized as [a_0, a_1, a_2, ...,
        a_n]

    Returns
    -------
    y : float
        Coordinate value of the dependent variable of the function at the
        given value of x.

    """
    # Compute the cubic polynomial
    y = 0.  # This will make the output a float
    n = len(a) - 1
    for i in range(n + 1):
        y += a[i] * x ** (n - i)

    # Return the result
    return y


# Create a function for the first derivative of a general polynomial
def poly_der(x, a):
    """
    Function to compute the first derivative of an arbitrary polynomial

    Computes the first derivative of the general polynomial f_n(x) = a_0x^n +
    a_1x^(n-1) + a_2x^(n-2) + ... + a_nx^(n-n) at the given point x, where
    [a_0, a_1, a_2, ... a_n] are coefficient values provided in the input
    list a. The order of the polynomial is one less than the length of the
    list.

    Parameters
    ----------
    x : float
        Coordinate value for the independent variable of the function
    a : list of floats
        Coefficients of the polynomial organized as [a_0, a_1, a_2, ...,
        a_n]

    Returns
    -------
    yp : float
        Coordinate value of the first derivative of the function at the
        given value of x.

    """
    # Compute the cubic polynomial
    y = 0.  # This will make the output a float
    n = len(a) - 1
    for i in range(n + 1):
        y += a[i] * (n - i) * x ** (n - i - 1)

    # Return the result
    return y


# Compute one step of Newton's method
def newton_step(x0, fun, fun_prime, args=()):
    """
    Compute one step of Newton's method for root finding

    Compute one step of Newton's root-finding method using the function
    defined in fun and its derivative defined in fun_prime. Returns a new
    estimate for the root.

    Parameters
    ----------
    x0 : float
        Current estimate for the root
    fun : function, form fun(x0, [args])
        Function to compute f(x) with optional input parameters args
    fun_prime : function, form fun_prime(x0, [args])
        Function to compute f'(x) with optional input parameters args
    args : tuple
        Optional additional parameters to pass to fun and fun_prime

    Returns
    -------
    xr : float
        New estimate for the root using Newton's method

    """
    # Compute f(x) and f'(x) at the guess x0
    f = fun(x0, *args)
    fp = fun_prime(x0, *args)

    # Use Newton's method equation to get new guess for root at xr
    xr = x0 - f / fp

    # Return the root
    return xr


# Find a root using Newton's method
def newton_root(x0, fun, fun_prime, args=()):
    """
    Find a root using Newton's method

    Find a root to an equation f(x) = 0 using iterations of Newton's method.
    Since Newton's method is an open method, we limit the search to 1000
    iterations. The convergence criteria for a root is an absolute error of
    1e-8. Returns the root and a flag indicating if a root was found (True =
    yes, False = no).

    Newton's method using the function f(x), given by fun, and its first
    derivative f'(x) (given by fun_prime).

    Parameters
    ----------
    x0 : float
        Initial guess for the root
    fun : function, form fun(x0, [args])
        Function to compute f(x) with optional input parameters args
    fun_prime : function, form fun_prime(x0, [args])
        Function to compute f'(x) with optional input parameters args
    args : tuple
        Optional additional parameters to pass to fun and fun_prime

    Returns
    -------
    xr : float
        Final estimate of the root
    flag : bool
        Boolean variable reporting whether the method converged on a root

    """
    # Initialize loop variables
    imax = 1000
    TOL = 1e-8
    error = 1
    i = 0

    # Iterate to find a root
    while abs(error) > TOL and i < imax:
        xr = newton_step(x0, fun, fun_prime, args)
        error = xr - x0
        x0 = xr
        i += 1

    # Check if we found a root
    flag = True
    if error > TOL:
        print("Newton's method did not converge on a root")
        flag = False

    # Return the results
    return (xr, flag)


if __name__ == '__main__':

    # Test general polynomial
    a = 1
    b = -1
    c = -6
    a = [a, b, c]
    x = 2
    y = polynomial(x, a)
    print('\nThe value of f(x) = x^2 - x - 6 at x = 2 is: ', y)

    # Test derivative of general polynomial
    yp = poly_der(x, a)
    print('\nThe first derivative of this polynomial at x = 2 is: ', yp)

    # Test newton_step
    xr = newton_step(x, polynomial, poly_der, [a])
    print('\nAn estimate for a root near x = 2 after one step of ')
    print("Newton's method is: ", xr)

    # Test newton's method
    (xr, found) = newton_root(x, polynomial, poly_der, [a])
    if found:
        print("\nNewton's method found a root near x = 2.  The root is: ", xr)
    else:
        print("\nNewton's method could not find a root near x = 2.")