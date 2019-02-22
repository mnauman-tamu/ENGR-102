# UserDefinedFunction.py
#
# This program attempts to complete part one of lab_10 and receive a grade of 100
# This program help user understand interest rates and money lending
#
# Alexander M Bogdan
# Patrick Zhong
# Muhammad Nauman
# Daniel Huck
# November 5, 2018
# ENGR 102-213

import numpy as np
import matplotlib.pyplot as plt


P = float(input("Monthly payment\n"))
N = int(input("Number of payments\n"))

SpaceMax = np.linspace(0, N, 100)
InterestArray = np.array([.05, .10, .15])
for Interest in InterestArray:
    print("Amount borrowed at interest " + str(Interest) + " is " + str(P*(((1+Interest)**N-1)/(Interest*(1+Interest)**N))))

IMax = float(input("Monthly interest max\n"))
IMin = float(input("Monthly interest min\n"))


def maximum(x): return P*(((1+IMax)**x-1)/(IMax*(1+IMax)**x))


def minimum(x): return P*(((1+IMin)**x-1)/(IMin*(1+IMin)**x))


MainPlot = plt.plot(SpaceMax, minimum(SpaceMax), 'g', SpaceMax, maximum(SpaceMax), 'r')
plt.show(MainPlot)

ExpectedInterest = float(input("What interest do you expect?"))

A = P*(((1+ExpectedInterest)**N-1)/(ExpectedInterest*(1+ExpectedInterest)**N))
print("Amount borrowed (A):" + str(A))
print("Total paid (NP): " + str(N*P))
print("Life of loan (g): " + str((N*P - A)/A))
