# booleanOperators.py
#
# Compute boolean operations
#
# Muhammad Nauman
# UIN: 927008027
# September 17, 2018
# ENGR 102-213
#
# Lab 4B - 1

import math

# Pre-processor

a = input("Should a be True or False: ")
if a == "True" or "true":
    a = True
else:
    a = False

b = input("Should b be True or False: ")
if b == "True" or "true":
    b = True
else:
    b = False

c = input("Should c be True or False: ")
if c == "True" or "true":
    c = True
else:
    c = False

# Processor
guess = input("Guess whether a and b and c is True or False: ")
ans = a and b and c
print("The answer is " + str(ans))
if guess == str(ans):
    print("Congrats! You got it right.")
else:
    print("Wrong guess")
print()

guess = input("Guess whether a or b or c is true or false: ")
ans = a or b or c
print("The answer is " + str(ans))
if guess == str(ans):
    print("Congrats! You got it right.")
else:
    print("Wrong guess")
print()

guess = (input("Guess whether (not (a and not b) or (not c and b)) and (not b) or (not a and b and not c) or (a and not"
               " b) is true or false: "))
ans = (not (a and not b) or (not c and b)) and (not b) or (not a and b and not c) or (a and not b)
print("The answer is " + str(ans))
if guess == str(ans):
    print("Congrats! You got it right.")
else:
    print("Wrong guess")
print()

guess = input("Guess whether (not ((b or not c) and (not a or not c))) or (not (c or not (b and c))) or (a and not c) "
              "and (not a or (a and b and c) or (a and ((b and not c) or (not b)))) is true or false: ")
ans = (not ((b or not c) and (not a or not c))) or (not (c or not (b and c))) or (a and not c) and (not a or (a and b and c) or (a and ((b and not c) or (not b))))
print("The answer is " + str(ans))
if guess == str(ans):
    print("Congrats! You got it right.")
else:
    print("Wrong guess")
print()

# 1.2
guess = input("Guess whether (a or b) and (not(a and b)) is True or False: ")
ans = (a or b) and (not(a and b))
print("The answer is " + str(ans))
if guess == str(ans):
    print("Congrats! You got it right.")
else:
    print("Wrong guess")
print()

guess = input("Guess whether (a and not b and not c) or (not a and b and not c) or (not a and not b and c) or (a and b "
              "and not c) or (a and not b and c) or (not a and b and c) is True or False: ")
ans = (a and not b and not c) or (not a and b and not c) or (not a and not b and c) or (a and b and not c) or (a and not b and c) or (not a and b and c)
print("The answer is " + str(ans))
if guess == str(ans):
    print("Congrats! You got it right.")
else:
    print("Wrong guess")
print()

# 1.3
guess = input("Guess whether not b or not a and not c is True or False: ")
ans = not b or not a and not c
print("The answer is " + str(ans))
if guess == str(ans):
    print("Congrats! You got it right.")
else:
    print("Wrong guess")
print()

guess = input("Guess whether not b and c or a is True or False: ")
ans = not b and c or a
print("The answer is " + str(ans))
if guess == str(ans):
    print("Congrats! You got it right.")
else:
    print("Wrong guess")
print()
