# weather.py
#
# Read in weather data of 3 years and perform calculations on it
#
# Muhammad Nauman
# UIN: 927008027
# ENGR 102-213
# October 28, 2018
#
# Lab 9b - 3

# Pre-processor
header = []
date = []
temp_hi = []
temp_avg = []
temp_lo = []
DP_hi = []
DP_avg = []
DP_lo = []
humidity_hi = []
humidity_avg = []
humidity_lo = []
pressure_hi = []
pressure_avg = []
pressure_lo = []
precip = []

# Processor
with open('WeatherDataWindows.csv', 'r') as t_d:
    for line in t_d:
        line = line.strip().split(',')
        if line[0][0].isalpha():
            header.append(line)
        else:
           date.append(line[0])
           temp_hi.append(float(line[1]))
           temp_avg.append(float(line[2]))
           temp_lo.append(float(line[3]))
           DP_hi.append(float(line[4]))
           DP_avg.append(float(line[5]))
           DP_lo.append(float(line[6]))
           humidity_hi.append(float(line[7]))
           humidity_avg.append(float(line[8]))
           humidity_lo.append(float(line[9]))
           pressure_hi.append(float(line[10]))
           pressure_avg.append(float(line[11]))
           pressure_lo.append(float(line[12]))
           precip.append(float(line[13]))

    max_temp = temp_hi[0]
    for i in temp_hi:
        if i > max_temp:
            max_temp = i

    min_temp = temp_lo[0]
    for j in temp_lo:
        if j < min_temp:
            min_temp = j

    avg_precip = 0
    for k in precip:
        avg_precip += k
    avg_precip /= len(precip)

    hu = 0
    for l in humidity_hi:
        if l > 90:
            hu += 1
    hu /= len(humidity_hi)
    hu *= 100

    july_max_temp = []
    for m in date:
        if m[0:4] == "5/25":
            july_max_temp.append(date.index(m))
    july_temp_hi = temp_hi[july_max_temp[0]]
    for n in july_max_temp:
        if temp_hi[n] > july_temp_hi:
            july_temp_hi = temp_hi[n]

    july_temp_lo = temp_lo[july_max_temp[0]]
    for n in july_max_temp:
        if temp_lo[n] < july_temp_lo:
            july_temp_lo = temp_lo[n]

    july_avg = 0
    july_avg_index = []
    for o in date:
        if o[0] == "5":
            july_avg_index.append(date.index(o))
    for p in july_avg_index:
        july_avg += temp_hi[p]
    july_avg /= len(july_avg_index)

# Post-processor
print("The highest temperature(F) recorded was: " + str(max_temp))
print("The highest temperature(F) recorded was: " + str(min_temp))
print("The average precipitation(in.) was: " + str(avg_precip))
print("The percent of days when the humidity was above 90% was: " + str(hu) + "%")
print("The maximum temperature reached on July 25 of all years was: " + str(july_temp_hi) + " F")
print("The minimum temperature reached on July 25 of all years was: " + str(july_temp_lo) + " F")
print("The average of high temperatures for July of all three years was: " + str(july_avg) + " F")
