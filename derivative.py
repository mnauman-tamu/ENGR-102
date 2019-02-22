# derivative.py
#
# Compute the derivative and  a numerical estimate of the derivative using the forward difference, backward difference,
# and central difference given coefficients in a cubic function and an x-value
#
# Muhammad Nauman, Daniel Huck, Alexander Bodgan, Patrick Zhong
# UIN: 927008027
# 10-01-2018
# Engr 102-213
#
# Lab 6-2.a

import math

# Pre-processor
A = int(input("Give A in Ax^3 + Bx^2 + Cx + D = 0: "))
while A == 0:
    A = int(input("Give A in Ax^3 + Bx^2 + Cx + D = 0: "))
B = int(input("Give B in Ax^3 + Bx^2 + Cx + D = 0: "))
C = int(input("Give C in Ax^3 + Bx^2 + Cx + D = 0: "))
D = int(input("Give D in Ax^3 + Bx^2 + Cx + D = 0: "))
x = float(input("Give the x value of the point where the derivative should be computed: "))
TOL = 10**-6
deltax = 100                            # delta x
count = 0
fx = float(A*x**3 + B*x**2 + C*x + D)

# Processor
der = 3*A*x**2 + 2*B*x + C                  # derivative
xix = x + deltax                            # xi + delta x
ximx = x - deltax                           # xi - delta x
fxix = fx                                   # will save the latest f(xix) to compare
fxix2 = A*xix**3 + B*xix**2 + C*xix + D     # f(xix)
fxix3 = 0                                   # will save the second last f(xix) to compare

while (math.fabs(fxix3 - fxix)) >= TOL:
    fxix = (fxix2-fx)/deltax
    fxix3 = fxix                            # second last fxix
    deltax /= 2                             # halves every time to get close to 0
    xix = x + deltax
    fxix2 = A*xix**3 + B*xix**2 + C*xix + D
    fxix = (fxix2 - fx) / deltax            # latest f(xix)
    count += 1                              # There might be some error in count +-1, but since we are comparing
#                                           # relatively, this shouldn't be a problem

deltax = 100                                # resets delta x
count2 = 0
fximx = A*ximx**3 + B*ximx**2 + C*ximx + D  # f(xi-delta x)
fximx2 = fximx                              # fximx2 and 3 are for comparative purposes
fximx3 = 0

while (math.fabs(fximx3 - fximx2)) >= TOL:  # Similar to the previous one
    fximx2 = (fx - fximx)/deltax
    fximx3 = fximx2
    deltax /= 2
    ximx = x - deltax
    fximx = A*ximx**3 + B*ximx**2 + C*ximx + D
    fximx2 = (fx - fximx) / deltax
    count2 += 1

deltax = 100                                # resets delta x
xix = x + deltax                            # x hasn't changed
ximx = x - deltax
fcdp = A*xix**3 + B*xix**2 + C*xix + D      # f(x + delta x)
fcdm = A*ximx**3 + B*ximx**2 + C*ximx + D   # f(x - delta x)
fcd = (fcdp - fcdm) / (2*deltax)            # computes central difference
fcd2 = 0                                    # for comparative purposes
count3 = 0

while math.fabs(fcd2 - fcd) > TOL:
    fcd2 = fcd
    deltax /= 2
    xix = x + deltax
    ximx = x - deltax
    fcdp = A * xix ** 3 + B * xix ** 2 + C * xix + D
    fcdm = A * ximx ** 3 + B * ximx ** 2 + C * ximx + D
    fcd = (fcdp - fcdm) / (2 * deltax)
    count3 += 1

# Post-processor
print("The exact derivative is " + str(der))
print("The forward difference is " + str(fxix) + " and it took " + str(count) + " iterations")
print("The backward difference is " + str(fximx2) + " and it took " + str(count2) + " iterations")
print("The central difference is " + str(fcd) + " and it took " + str(count3) + " iterations")
print("The central difference takes the least iterations because the denominator increases twice as fast")
