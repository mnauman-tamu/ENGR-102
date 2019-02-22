# formattedPrinting.py
#
# Write a mad-lib
#
# Muhammad Nauman
# UIN: 927008027
# September 10, 2018
# ENGR 102-213
#
# Lab 3A - 3

print("\n \tI was " + input("Give your age: ") + " years old when the first storm hit. The storm was of category " +
      str((int(input("Give a positive number:")) % 5) + 1) + ". The storm took the following things from the "
      "backyard:\n \t" + input("Name two things commonly found in a backyard (separated by a comma):") + ", and Paddy\'"
      "s jumping rope. Paddy is my younger brother who was " + input("Give a number between 6 and your age: ") +
      " years old. It has been " + str(int(input("Give a positive integer: ")) % 20) + " years since the storm struck.")
