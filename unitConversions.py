# unitConversions.py
#
# Convert units using inputs from the user
#
# Muhammad Nauman
# UIN: 927008027
# September 10, 2018
# ENGR 102-213
#
# Lab 3A - 1

import math

# Pre-processor (1)
pounds = input("Give a weight in pounds: ")
one_pound_in_grams = 453.592
one_gram_to_newtons = 0.0098

# Processor (1)
newtons = float(pounds) * one_pound_in_grams * one_gram_to_newtons

# Post-processor (1)
print("The result in N is: " + str(newtons))
print()

# Pre-processor (2)
BTUs = input("Give energy in BTUs: ")
one_BTU_in_joules = 1055.06

# Processor (2)
energy = float(BTUs) * one_BTU_in_joules

# Post-processor (2)
print("The result is " + str(energy) + " joules")
print()

# Pre-processor (3)
pascals = input("Give pressure in Pascals: ")
one_pascal_in_mmHg = 0.00750063755

# Processor (3)
pressure = float(pascals) * one_pascal_in_mmHg

# Post-processor (3)
print("The result is: \n \t" + str(pressure) + " mmHg")
print()

# Pre-processor (4)
seconds_per_revolution = input("Give frequency in seconds per revolution: ")
revolutions_per_second = 1/float(seconds_per_revolution)

# Processor (4)
hertz = revolutions_per_second * 1

# Post-processor (4)
print("The frequency in hertz is " + str(hertz))
print()

# Pre-processor (5)
mph = input("Give speed in miles per hour: ")
mph_to_meters_per_second = 0.44704

# Processor (5)
speed = float(mph) * mph_to_meters_per_second

# Post-processor (5)
print("The result in meters per second is " + str(speed))
print()

# Pre-processor (6)
fahrenheit = input("Give temperature in fahrenheit: ")

# Processor (6)
celsius = (float(fahrenheit) - 32) / 1.8
celsius = round(celsius, 3)

# Post-processor (6)
print("The temperature in celsius is: " + str(celsius))
print()

# Pre-processor (7)
voltage = input("Give voltage in V: ")

# Processor (7)
power_gain = 20*math.log10(float(voltage))

# Post-processor (7)
print("The power gain is " + str(power_gain) + " dBV")
print()

# Pre-processor (8)
richter_value_one = input("Give first richter value: ")
richter_value_two = input("Give second richter value: ")
difference = abs(float(richter_value_one) - float(richter_value_two))

# Processor (8)
ratio = 10**difference

# Post-processor (8)
print("The ratio of energy released is " + str(ratio) + " to one.")
