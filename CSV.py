# CSV.py
#
# Save a list of amortized loan values for a loan to a file in CSV format.
#
# Muhammad Nauman
# UIN: 927008027
# ENGR 102-213
# October 28, 2018
#
# Lab 9b - 2

# Pre-processor
amt = float(input("What is the amount of the loan? "))
interest = float(input("What is the interest rate as a decimal (for example, if it's 7%, enter 0.07? "))
monthly = float(input("What is the amount being paid monthly? "))
name = input("What should the name of the file be? (be sure to use a .csv file extension) ")
acc_int = 0
amt_remaining = amt
monthly_int = interest/12

# Processor
with open(name, 'w') as o_f:
    o_f.write("Month, Interest Accrued ($), Amount Remaining ($)\n")
    o_f.write("0,0,0\n")
    for i in range(1,61):
        amt_remaining = (amt_remaining - monthly) * (1 + monthly_int)
        if amt_remaining >= 0:
            acc_int += monthly_int * amt_remaining
        else:
            o_f.write(str(i) + "," + str(acc_int) + ",0")
            exit()
        o_f.write(str(i) + "," + str(acc_int) + "," + str(amt_remaining) + "\n")

