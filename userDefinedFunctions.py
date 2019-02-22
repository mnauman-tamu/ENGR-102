# userDefinedFunctions.py


def cubic_eqn(x, a, b, c, d):
    """
    Compute the cubic equation

    Parameters
    ----------
    x: float, int, numpy.array

    a, b, c, d: float
        parameters of the cubic equation

    Returns
    -------
    f_x: float, int, numpy.array
        Value of cubic equation at x
    n: int
        Order of the polynomial
    """
    f_x = a * x**3 + b * x**2 + c * x + d
    n = 3

    return f_x, n


x_val = float(input("Enter a value for x to compute cubic equation: "))
a, b, c, d = (1., 1.5, 2., 2.5)

y_val = cubic_eqn(x_val, a, b, c, d)

print(y_val[0])
