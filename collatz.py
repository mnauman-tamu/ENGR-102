# collatz.py
#
# Compute the collatz sequence
#
# Muhammad Nauman
# UIN: 927008027
# 10-03-2018
# Engr 102-213
#
# Lab 6b-1

# Pre-processor
x = int(input("Enter a positive integer: "))
count = 0
print(x)

# Processor
while not x == 1:   # Will keep repeating until x hits 1
    if x % 2 == 0:  # Checks if x is even and divide x by 2 if its even
        x = x/2
    else:           # If x is not even, then it's odd. x is reset to 3*x+1
        x = (3 * x) + 1
    count += 1
    print(x)

# Post-processor
print("It took " + str(count) + " iterations.")
