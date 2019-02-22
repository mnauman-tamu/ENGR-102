# 9.1 code.py
#
# Performs linear interpolation between an arbitrary number of given points (extension)
#
# Patrick Zhong
# Muhammad Nauman
# Daniel Huck
# Alexander Bogdan
# ENGR 102-213
#
# Lab 9, Activity 1

pointsQuant = int(input("How many points would you like to add?\n"))
points = []
matrix = []
i = 0
while i < pointsQuant:
    matrix = [float(input("Input a data point X value higher than the previous one\n")), float(input("Input a data point Y value\n"))]
    if len(points) == 0:
        points.append(matrix)
    elif max(point[0] for point in points) < matrix[0]:
        points.append(matrix)
    else:
        print("Try again")
        pointsQuant = pointsQuant + 1
    i += 1
x = float(input("Input desired X\n"))

# END INPUT
#####################

low = None
high = None
res = None

for p in points:
    if x == p[0]:
        res = p[1]
        break
    elif x < p[0]:
        high = p
        break
    low = p

if res is not None:
    print("One of the given points was found at the desired x-value. The y-value there is exactly " + str(res) + ".")
    exit(0)

if low is None or high is None:
    print("The given x-value (" + str(x) + ") is out of bounds. This is linear interpolation not extrapolation!")
    exit(0)

slope = (high[1] - low[1]) / (high[0] - low[0])
y = low[1] + slope * (x - low[0])

print("The linear interpolation yields " + str(y) + " as the estimated y-value at " + str(x) + ".")