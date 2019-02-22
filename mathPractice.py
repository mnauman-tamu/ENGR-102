# mathPractice.py
#
# Write a short math program
#
# Muhammad Nauman
# UIN: 927008027
# September 19, 2018
# ENGR 102-213
#
# Lab 4B - 2

import random

for i in range(3):
    a = random.randint(1, 20)
    b = random.randint(1, 20)

    if a - b > 0:
        print(str(a) + " - " + str(b) + " = ")
    else:
        print(str(b) + " - " + str(a) + " = ")
