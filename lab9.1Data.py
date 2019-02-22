# Lab9.1Data.py
#
# Saves data to a file for interpolation
#
# Patrick Zhong
# Muhammad Nauman
# Daniel Huck
# Alexander Bogdan
# ENGR 102-213
#
# Lab 9, Activity 1

name = input("Enter the file name: ")
with open(name, 'w') as output_file:

    ind_var_header = input("What does the independent variable represent (Put units separated by a space with in "
                           "between the number and unit [e.g. Pressure in kPa]): ")
    ind_var = []
    dep_var_num = int(input("How many dependent variables are there (Enter an integer): "))
    dep_var_header = []
    dep_var = []
    for i in range(dep_var_num):
        d_v = input("What does the #" + str(i+1) + " dependent variable represent (Put units separated by a space with "
                    "in between the number and unit [e.g. Pressure in kPa]): ")
        dep_var_header.append(d_v)
    num = int(input("How many points would you like to add (Enter an integer)? "))
    for i in range(num):
        ind_var.append(input("Enter the dependent value higher than the previous one: "))
        dep_var_list = []
        for j in range(dep_var_num):
            dep_var_list.append(input("Enter the #" + str(j+1) + " dependent variable: "))
        dep_var.append(dep_var_list)
    output_file.write(ind_var_header + '\t')
    output_file.write('\t'.join(dep_var_header) + '\n')
    for k in range(num):
        output_file.write(str(ind_var[k]) + '\t')
        for l in range(dep_var_num):
            output_file.write(str(dep_var[k][l]) + '\t')
        output_file.write('\n')
