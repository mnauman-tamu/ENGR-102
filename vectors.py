# vectors.py
#
# Do mathematical operations of vectors of arbitrary dimensions
#
# Muhammad Nauman
# UIN: 927008027
# Oct 12 2018
# ENGR 102-213
#
# Lab 7b - 4

import math
import numpy as np

# Pre-processor
dimensions = int(input("Enter the dimensions of the vector: "))
vector1 = []
vector2 = []
mag1 = 0
mag2 = 0
sum = []
dif = []
mult = 0

# Processor
for i in range(dimensions):
    element = int(input("Enter the #" + str(i+1) + " element of the first vector: "))
    vector1.append(element)
print()
for i in range(dimensions):
    element = int(input("Enter the #" + str(i+1) + " element of the second vector: "))
    vector2.append(element)

for num in vector1:
    mag1 += num**2
for num in vector2:
    mag2 += num**2
mag1 = math.sqrt(mag1)
mag2 = math.sqrt(mag2)

for j in range(dimensions):
    sum.append(vector1[j]+vector2[j])

for k in range(dimensions):
    dif.append(vector1[k]-vector2[k])

for l in range(dimensions):
    mult += (vector1[l]*vector2[l])

v1np = np.array(vector1)

v2np = np.array(vector2)

magnitude1 = np.linalg.norm(v1np)

magnitude2 = np.linalg.norm(v2np)

sumnp = np.add(v1np, v2np)

difnp = np.subtract(v1np, v2np)

dotnp = np.dot(v1np, v2np)

# Post-processor
print()
print("Vector 1: " + str(vector1))
print("Vector 2: " + str(vector2))
print("The magnitude of vector 1 is: " + str(mag1))
print("The magnitude of vector 2 is: " + str(mag2))
print("The sum of the 2 vectors is: " + str(sum))
print("The difference of the 2 vectors is: " + str(dif))
print("The dot product of the 2 vectors is: " + str(mult))
print()
print("Using np.array we get the following: ")
print("Vector 1: " + str(v1np))
print("Vector 2: " + str(v2np))
print("The magnitude of vector 1 is: " + str(magnitude1))
print("The magnitude of vector 2 is: " + str(magnitude2))
print("The sum of the 2 vectors is: " + str(sumnp))
print("The difference of the 2 vectors is: " + str(difnp))
print("The dot product of the 2 vectors is: " + str(dotnp))
