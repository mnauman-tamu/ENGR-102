# temperature.py
#
# Read in a file containing temperatures in celsius and output a file converting these temperatures to fahrenheit.
#
# Muhammad Nauman
# UIN: 927008027
# ENGR 102-213
# October 28, 2018
#
# Lab 9b - 1

# Pre-processor
fahrenheit = []

# Processor
with open('celsius.dat', 'r') as t_d:
    for line in t_d:
        line = line.strip().split(',')
        if line[0][0].isdigit():
            for value in line:
                line = (1.8*int(value))+32
                fahrenheit.append(line)

# Post-processor
with open("fahrenheit.out", 'w') as o_f:
    o_f.write("Temperature (F)\n")
    for i in fahrenheit:
        o_f.write(str(i))
        o_f.write("\n")
