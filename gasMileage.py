# gasMileage.py
#
# compute mileage and cost per mile
#
# Muhammad Nauman
# UIN: 927008027
# September 5, 2018
# ENGR 102-213
#
# Lab 2b - A

import math

# Pre-processor
miles = 0
gallon = 0
cost = 0
avg_mileage = 0
avg_cpm = 0
total_cost = 0
cost_in_1918 = 39.42
percentage = 0

# Processor
miles = 106.5
gallon = 5.02
cost = 11.5
mileage = miles/gallon
cost_per_mile = cost/miles
avg_mileage += mileage
avg_cpm += cost_per_mile
total_cost += cost

miles = 171.6
gallon = 6.50
cost = 18.14
mileage = miles/gallon
cost_per_mile = cost/miles
avg_mileage += mileage
avg_cpm += cost_per_mile
total_cost += cost

miles = 125.2
gallon = 5.26
cost = 13.94
mileage = miles/gallon
cost_per_mile = cost/miles
avg_mileage += mileage
avg_cpm += cost_per_mile
total_cost += cost

miles = 251.6
gallon = 8.85
cost = 25.58
mileage = miles/gallon
cost_per_mile = cost/miles
avg_mileage += mileage
avg_cpm += cost_per_mile
total_cost += cost

miles = 150.6
gallon = 5.09
cost = 12.47
mileage = miles/gallon
cost_per_mile = cost/miles
avg_mileage += mileage
avg_cpm += cost_per_mile
total_cost += cost

percentage = ((total_cost-cost_in_1918)/cost_in_1918)*100
avg_mileage /= 5
avg_cpm /= 5

# Post-processor
print("The average mileage is " + str(avg_mileage))
print("The average cost per mile is " + str(avg_cpm))
print("The cost of gas has increased by " + str(percentage) + "%")
print("The gas prices were the highest in 2012")
