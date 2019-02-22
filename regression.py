# regression.py
#
# Find the best-fit line through the data
#
# Muhammad Nauman
# UIN: 927008027
# Oct 12 2018
# ENGR 102-213
#
# Lab 7b - 2

import numpy as np
from scipy import stats
import matplotlib.pyplot as plt

# Pre-processor
resistance = np.array([761, 817, 874, 917, 1018])
temperature = np.array([20.0, 31.5, 50.0, 71.8, 91.3])

# Processor
resistancemean = np.mean(resistance)
temperaturemean = np.mean(temperature)

temperaturesum = np.sum(temperature)
resistancesum = np.sum(resistance)
temperaturesumsqrd = np.sum(temperature**2)
tempresmult = np.dot(temperature, resistance)

m = (tempresmult - (temperaturesum*resistancemean))/(temperaturesumsqrd - (temperaturesum*temperaturemean))
b = resistancemean - (m*temperaturemean)

plt.plot(temperature, resistance, 'ro')
plt.plot(temperature, m*temperature+b)
plt.ylabel("Resistance (ohms)")
plt.xlabel("Temperature (C)")
plt.show()

# Post-processor
print("The m value is: " + str(m))
print("The b value is: " + str(b))
