import math
# Define an angle to compute
x = 45. * math.pi / 180

# Set up a loop variable
TOL = 1.e-060
error = 1.

summit = 0
n = 0

while math.fabs(error) > TOL:
    print("Iteration number: " + str(n))
    new_term = (-1)**n * x**(2 * n) / math.factorial(2 * n)
    summit += new_term
    n += 1

    error = new_term

print("Cosine x is " + str(summit))
print("Math module gives " + str(math.cos(x)))
