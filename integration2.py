# integration2.py
#
# This program compares 2 ways of integrating a polynomial
#
# Daniel Huck, Muhammad Nauman, Patrick Zhong, Alex Bogdan
# 827003691
# 11/7/18
# ENGR 201-213
# Week 11 activity 3

import scipy.integrate
import Newton


def integrate(xi, xf, i, n=10e4):
   """
   Parameters
   ----------
   xi: int
       initial x value of f(x)
   xf: int
       final x value of f(x)
   i: list
       parameter values for integrand function
   :return:
   area: float
       area under the curve in the given domain
   count: int
       number of rectangles used to approximate area
   """
   area = 0
   x = xi
   while x < xf:
       a = (xf-xi)/n
       area += a * ((Newton.eq(x, i) + Newton.eq(x+a, i))/2)
       x += a

   area2 = scipy.integrate.quad(Newton.eq, xi, xf, args=(i))
   fun = (area, n)
   diff = area - area2[0]
   comp = 'The difference between the function calculation and the module calculation is ' + str(diff)
   return fun, area2, comp


if __name__ == '__main__':
   xi = 0
   xf = 25
   n = 100
   i = [5, -3, 8, 0]
   print(integrate(xi, xf, i, n))
   print(integrate(xi, xf, i))

