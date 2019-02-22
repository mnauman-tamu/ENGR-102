# interactingWithTheUser.py
#
# Work together to format a list of projects and dates
#
# Muhammad Nauman
# UIN: 927008027
# September 10, 2018
# ENGR 102-213
#
# Patrick Zhong
#
# Lab 3A - 2

projects = []
dates = []

for i in range(1, 5):
    projects.append(input("\nEnter the name of project %d: " % i))
    dates.append(input("Enter the due date for project %d: " % i))

print("----------------------------------------------------------------")
for i in range(0, 4):
    s = " " * max(32 - len(projects[i]), 5)
    print("Project %d:            " % (i+1) + projects[i] + s + dates[i])
print("----------------------------------------------------------------")


