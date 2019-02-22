# Data.py
#
# Find the average, minimum, and maximum of the entered numbers
#
# Muhammad Nauman
# UIN: 927008027
# 10-03-2018
# Engr 102-213
#
# Lab 6b-2

# Pre_processor
sum = 0
cnt = 0
x = int(input("Enter the value: "))
if x < 0:
    exit()
min = x
max = x

# Processor
while x > -1:       # Will stop if x is negative
    if x > max:     # Replaces x with max if x is the biggest value
        max = x
    if x < min:     # Replaces x with min if x is the smallest value
        min = x
    sum += x
    cnt += 1
    x = int(input("Enter the value: "))
avg = sum/cnt

# Post-processor
print("The maximum value is: " + str(max))
print("The minimum value is: " + str(min))
print("The average of all values is " + str(avg))
