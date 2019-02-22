# interpolationProgram.py
#
# compute distance from Mars
#
# Muhammad Nauman
# UIN: 927008027
# September 4, 2018
# ENGR 102-213
#
# Lab 2 - C1

import math

# Pre-processor
true_distance = 64000000
true_days = 304
speed = true_distance/true_days

# Processor
days = 1
distance = speed * days

# Post-processor
print(distance)
