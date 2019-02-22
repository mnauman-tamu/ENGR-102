# myCosine.py
#
# compute cos(x) from Maclauren series
#
# Muhammad Nauman
# UIN: 927008027
# September 3, 2018
# ENGR 102-213
#

import math

# Pre-processor

x = 45.0 * math.pi / 180.
n_terms = 4

# Processor

# initialize a variable to contain the sum
cos_term = 0.

# Write out the contribution from the nth term:
for i in range(n_terms):
    n = i
    cos_term += (-1)**n * x**(2 * n) / math.factorial(2 * n)

# compute from math module
cos_ans = math.cos(x)

# Post-processor - output results
print("Cosine " + str(x) + " in radians from " + str(n_terms) + " terms of Maclauren expansion = ")
print(cos_term)
print()

print("Cosine x from math module =")
print(cos_ans)
print()
