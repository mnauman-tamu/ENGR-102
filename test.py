# test.py
#
# Tests whether the writing and reading functions work correctly
#
# Muhammad Nauman
# UIN: 927008027
# 10/29/2018
# ENGR 102-213
#
# Lab 10b - 2

import files

ans = files.reader("WeatherDataWindows.csv", 1)
print(ans)

header = []
temp_hi = []
with open('WeatherDataWindows.csv', 'r') as t_d:
    for line in t_d:
        line = line.strip().split(',')
        if line[0][0].isalpha():
            header.append(line)
        else:
           temp_hi.append(float(line[1]))

    max_temp = temp_hi[0]
    for i in temp_hi:
        if i > max_temp:
            max_temp = i

    print("The highest temperature(F) recorded was: " + str(max_temp))


ans = files.writer(ans[0], ans[1], "Test.csv")

header = []
temp_hi = []
with open('Test.csv', 'r') as t_d:
    for line in t_d:
        line = line.strip().split(',')
        if line[0][0].isalpha():
            header.append(line)
        else:
           temp_hi.append(float(line[1]))

    max_temp = temp_hi[0]
    for i in temp_hi:
        if i > max_temp:
            max_temp = i

    print("The highest temperature(F) recorded was: " + str(max_temp))

