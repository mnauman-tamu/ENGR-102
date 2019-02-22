# chemEq
#
# Write a program to find the number of atoms of a specific element in a molecule
#
# Muhammad Nauman
# UIN: 927008027
# September 19, 2018
# ENGR 102-213
#
# Lab 4B - 5

# Pre-processor
A = input("Enter the chemical formula for the molecule (Type subscripts as normal numbers): ")
sym = input("Enter the symbol of the element you want to find the atoms of: ")

# Processor
index = A.find(sym)
length = len(sym)
if index + length >= len(A):
    print("There is only one atom of " + sym + " in the molecule " + A)
elif A[index + length].isdigit():
    print("There are ", end='')
    print(A[index + length], end='')
    for i in range(1, (len(A) - index - 1)):
        if A[index + length + i].isdigit():
            print(A[index + length + i], end='')
        else:
            break
    print(" atoms of " + sym + " in the molecule " + A)
else:
    print("There is only one atom of " + sym + " in the molecule " + A)
