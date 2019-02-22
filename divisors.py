# divisors.py
#
# For numbers from 2 to 100, print a series of lines reporting all of the divisors of those number
#
# Muhammad Nauman
# UIN: 927008027
# 10-03-2018
# Engr 102-213
#
# Lab 6b-2

for i in range(2, 101):         # Iterates from 2 to 100
    print("The divisors of " + str(i) + " are :")
    for n in range(2, i+1):     # Goes from 2 to i
        if i % n == 0:          # to find all the divisors
            print(n)


