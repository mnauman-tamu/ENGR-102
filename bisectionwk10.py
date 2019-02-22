# bisectionwk10.py
#
# This program find cubic roots using the bisection method
#
# Daniel Huck
# Muhammad Nauman
# 827003691
# 10/31/18
# ENGR 102-213

import numpy

def cubic_eqn(x):
   """
   compute the cubic equation
   parameters
   ----------
   x:float,int, numpy.array
   a,b,c,d: float
       parameters of the cubic equation
   Returns
   -------
   f_x: float, int, numpy.array
       value of cubic equation at x
   """
   f_x = a * x**3 + b *x**2 + c * x + d


   return (f_x)

def findRoot(tol, left, right, maxtries, f):
   i = left
   j = right

   signI = numpy.sign(f(i))
   signJ = numpy.sign(f(j))

   tries = 0

   if signI == 0:  # found root
       return i, tries

   if signJ == 0:  # found root
       return j, tries

   root = left  # start with left bound

   while abs(f(root)) > tol and tries < maxtries:  # exit if within tolerance or exceeded max tries
       tries += 1

       root = (i + j) / 2  # bisection
       sign = numpy.sign(f(root))
       if sign == 0:  # found root
           return j, tries

       if sign == signI:
           i = root  # set midpoint as left bracket
       else:
           j = root  # set midpoint as right bracket

   return root, tries  # found root


a = float(input("\nEnter the value of A: "))
b = float(input("Enter the value of B: "))
c = float(input("Enter the value of C: "))
d = float(input("Enter the value of D: "))

f = lambda x: cubic_eqn(x)

# SOURCE https://en.wikipedia.org/wiki/Properties_of_polynomial_roots#Based_on_the_Rouch%C3%A9_theorem
right = max(1.0, (abs(d) + abs(c) + abs(b)) / abs(a))  # Rouche's theorem for upper magnitude of roots
left = - right

maxtries = float(input("\nEnter the maximum number of tries: "))

if right < left:  # reorder left and right bounds
   temp = right
   right = left
   left = temp

print("\nLeft bound: " + str(left))
print("\nRight bound: " + str(right))

root, tries = findRoot(10E-6, left, right, maxtries, f)  # find roots

if tries >= maxtries:  # maximum tries reached
   print("\bMaximum tries exceeded - no root found.")
else:
   print("\nRoot approximated at x = " + str(root))
   print("f(x): " + str(f(root)))
   print("\nTries taken: " + str(tries))

