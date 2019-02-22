# derivative2.py
#
# Estimate the derivative of four complex function using central difference
#
# Muhammad Nauman, Daniel Huck, Alexander Bodgan, Patrick Zhong
# UIN: 927008027
# 10-01-2018
# Engr 102-213
#
# Lab 6-2.b

import math

# Pre-processor
func1 = "f1 = (x^2 - x - 2) / (x - 1)"
func2 = "f2 = 5*x*e^x"
func3 = "f3 = (x^3 + 5*x - 6) / (e^(2+x))"
func4 = "f4 = sin(cos(x))"
print(func1)
print(func2)
print(func3)
print(func4)
choice = input("The derivative of which function should be evaluated (f1-f4): ")
x = float(input("Give the x value of the point where the derivative should be computed: "))
while x == 0 or x == 1 or x <= -2:
    print("Please choose again. One or more functions are undefined at this value.")
    x = float(input("Give the x value of the point where the derivative should be computed: "))
TOL = float(input("Choose a tolerance of error: "))
while TOL <= 10**-3 or TOL >= 10**3:
    print("Please choose tolerance again. The tolerance is too small or large.")
    TOL = float(input("Choose a tolerance of error: "))
f1 = (x**2 - x - 2) / (x - 1)
f2 = math.exp(x)*5*x
f3 = (x**3 + 5*x - 6) / (math.exp(2+x))
f4 = math.sin(math.cos(x))
count = 0

# Processor
if choice == "f1":
    deltax = 100
    xix = x + deltax
    ximx = x - deltax
    fcdp = (xix**2 - xix - 2) / (xix - 1)
    fcdm = (ximx**2 - ximx - 2) / (ximx - 1)
    fcd = (fcdp - fcdm) / (2*deltax)
    fcd2 = 0
    count3 = 0

    while math.fabs(fcd2 - fcd) > TOL:
        fcd2 = fcd
        deltax /= 2
        xix = x + deltax
        ximx = x - deltax
        fcdp = (xix**2 - xix - 2) / (xix - 1)
        fcdm = (ximx**2 - ximx - 2) / (ximx - 1)
        fcd = (fcdp - fcdm) / (2 * deltax)
        count3 += 1

elif choice == "f2":
    deltax = 100
    xix = x + deltax
    ximx = x - deltax
    fcdp = math.exp(xix)*5*xix
    fcdm = math.exp(ximx)*5*ximx
    fcd = (fcdp - fcdm) / (2 * deltax)
    fcd2 = 0
    count3 = 0

    while math.fabs(fcd2 - fcd) > TOL:
        fcd2 = fcd
        deltax /= 2
        xix = x + deltax
        ximx = x - deltax
        fcdp = math.exp(xix) * 5 * xix
        fcdm = math.exp(ximx) * 5 * ximx
        fcd = (fcdp - fcdm) / (2 * deltax)
        count3 += 1

elif choice == "f3":
    deltax = 100
    xix = x + deltax
    ximx = x - deltax
    fcdp = (xix**3 + 5*xix - 6) / (math.exp(2+xix))
    fcdm = (ximx**3 + 5*ximx - 6) / (math.exp(2+ximx))
    fcd = (fcdp - fcdm) / (2 * deltax)
    fcd2 = 0
    count3 = 0

    while math.fabs(fcd2 - fcd) > TOL:
        fcd2 = fcd
        deltax /= 2
        xix = x + deltax
        ximx = x - deltax
        fcdp = (xix ** 3 + 5 * xix - 6) / (math.exp(2 + xix))
        fcdm = (ximx ** 3 + 5 * ximx - 6) / (math.exp(2 + ximx))
        fcd = (fcdp - fcdm) / (2 * deltax)
        count3 += 1

elif choice == "f4":
    deltax = 100
    xix = x + deltax
    ximx = x - deltax
    fcdp = math.sin(math.cos(xix))
    fcdm = math.sin(math.cos(ximx))
    fcd = (fcdp - fcdm) / (2 * deltax)
    fcd2 = 0
    count3 = 0

    while math.fabs(fcd2 - fcd) > TOL:
        fcd2 = fcd
        deltax /= 2
        xix = x + deltax
        ximx = x - deltax
        fcdp = math.sin(math.cos(xix))
        fcdm = math.sin(math.cos(ximx))
        fcd = (fcdp - fcdm) / (2 * deltax)
        count3 += 1

# Post-processor
print("The numerical derivative is " + str(fcd) + " and it took " + str(count3) + " iterations")
print("The estimate for the absolute error is " + str(TOL))
