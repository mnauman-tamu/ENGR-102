# Quiz_Week5.py
#
# Contract time and delay penalties
#
# Muhammad Nauman
# UIN: 927008027
# Engr 102-213
# September 24 2018
#
# Week 5 Quiz

# Pre-processor
duration = int(input("Enter the contractual project duration in days: "))
delay = int(input("Enter the number of days the contractor is behind schedule: "))
changeOrder = input("Was there a change order [type Y for yes or N for no]: ")
estDuration = duration + delay

# Processor
if changeOrder == "Y":
    estDuration = estDuration + 5
penalty = delay*10000

# Post-processor
print("The original project duration: " + str(duration))
print("The present estimated project duration: " + str(estDuration))
if penalty > 0:
    print("The contractor is accumulating penalties. The present estimate of the penalties is: " + str(penalty))
else:
    print("The contractor is on budget.")
