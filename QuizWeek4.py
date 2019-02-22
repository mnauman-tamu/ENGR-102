# QuizWeek4.py
#
# Computing and printing an average of grades.
#
# Muhammad Nauman
# UIN: 927008027
# September 17, 2018
# ENGR 102-213
#
# Quiz Week 4

# Pre-processor
name = input("What is your name: ")
test1 = float(input("What did you get on your first test: "))
test2 = float(input("What did you get on your second test: "))
test3 = float(input("What did you get on your third test: "))

# Processor
avg = (test1 + test2 + test3)/3

# Post-processor
print(str(name) + ", your average on the three tests is " + str(avg))
