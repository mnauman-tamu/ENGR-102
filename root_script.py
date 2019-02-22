# root_script.py
#
# This program uses the functions defined in roots.py to solve for the roots
# of equations.
#
# S. Socolofsky
# ENGR 102
# Novmeber 2018

import roots


def get_int(text):
    """
    Get integers from the user

    Ask the user to input an integer and provide error handling to allow
    the user to fix one error.  Returns the inputed integer as an integer.

    Parameter
    ---------
    text : str
        The text to print to the screen within in the input statement

    """
    try:
        num = int(input(text))
    except ValueError:
        print('You must enter an integer value.')
        num = int(input(text))

    return (num)


def get_float(text):
    """
    Get floats from the user

    Ask the user to input a value and provide error handling to allow
    the user to fix one error.  Returns the inputed number as a float.

    Parameter
    ---------
    text : str
        The text to print to the screen within in the input statement

    """
    try:
        num = float(input(text))
    except ValueError:
        print('You must enter a numerical value.')
        num = float(input(text))

    return (num)


# Ask the user to input the coefficients of a polynomial
print('\nThis program will solve for the roots of a polynomial ')
print("for polynomials of any order using Newton's method.  The ")
print('general form of the polynomial is given by:')
print('\n    f(x) = a_0x^n + a_1x^(n-1) + a_2x^(n-2) + ... +')
print('           a_nx^(n-n)')

# Get the input data from the user
n = get_int('\nEnter the order of the polynomial you wish to solve: ')
a = []
for i in range(n + 1):
    a.append(get_float('    Enter the value for a_' + str(i) + ': '))

# Solve for roots of the polynomial
done = False
while not done:
    x0 = get_float('\nEnter an initial guess for a root: ')
    (xr, worked) = roots.newton_root(x0, roots.polynomial, roots.poly_der,
                                     [a])

    # Print results
    if worked:
        print('\n    Found a root at:', xr)
    else:
        print('\n    Could not find a root with that initial guess.')

    ans = input('\nDo you want to try again? (y/n): ')
    done = not (ans[0] == 'Y' or ans[0] == 'y')

