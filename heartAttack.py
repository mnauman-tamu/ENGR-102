# heartAttack.py
#
# Create a program that will report someone’s 10-year risk, or likelihood, of a heart attack
#
# Muhammad Nauman
# UIN: 927008027
# Engr 102-213
# September 26 2018
#
# Lab 5B

# Pre-processor
gender = input("Enter your gender (M for male/ F for female): ")
M = 0
F = 0
points = 0
if gender == 'M':
    M = 1
else:
    F = 1
age = int(input("Enter your age: "))
cholesterol = int(input("What is your cholesterol? "))
smoker = int(input("Are you a smoker (1 for yes/ 0 for no): "))
HDL = int(input("What is your HDL? "))
BP = int(input("Enter your Systolic BP: "))
treated = int(input("Is it treated (1 for yes/ 0 for no): "))

# Processor
if 20 <= age <= 34:
    points += (M*-9) + (F*-7)
    if 160 <= cholesterol <= 199:
        points += 4
    elif 200 <= cholesterol <= 239:
        points += (M*7) + (F*8)
    elif 240 <= cholesterol <= 279:
        points += (M*9) + (F*11)
    elif cholesterol >= 280:
        points += (M*11) + (F*13)
    if smoker == 1:
        points += (M*8) + (F*9)
elif 35 <= age <= 39:
    points += (M*-4) + (F*-3)
    if 160 <= cholesterol <= 199:
        points += 4
    elif 200 <= cholesterol <= 239:
        points += (M*7) + (F*8)
    elif 240 <= cholesterol <= 279:
        points += (M*9) + (F*11)
    elif cholesterol >= 280:
        points += (M*11) + (F*13)
    if smoker == 1:
        points += (M*8) + (F*9)
elif 40 <= age <= 44:
    points += 0
    if 160 <= cholesterol <= 199:
        points += 3
    elif 200 <= cholesterol <= 239:
        points += (M*5) + (F*6)
    elif 240 <= cholesterol <= 279:
        points += (M*6) + (F*8)
    elif cholesterol >= 280:
        points += (M*8) + (F*10)
    if smoker == 1:
        points += (M*5) + (F*7)
elif 45 <= age <= 49:
    points += 3
    if 160 <= cholesterol <= 199:
        points += 3
    elif 200 <= cholesterol <= 239:
        points += (M*5) + (F*6)
    elif 240 <= cholesterol <= 279:
        points += (M*6) + (F*8)
    elif cholesterol >= 280:
        points += (M*8) + (F*10)
    if smoker == 1:
        points += (M*5) + (F*7)
elif 50 <= age <= 54:
    points += 6
    if 160 <= cholesterol <= 199:
        points += 2
    elif 200 <= cholesterol <= 239:
        points += (M*3) + (F*4)
    elif 240 <= cholesterol <= 279:
        points += (M*4) + (F*5)
    elif cholesterol >= 280:
        points += (M*5) + (F*7)
    if smoker == 1:
        points += (M*3) + (F*4)
elif 55 <= age <= 59:
    points += 8
    if 160 <= cholesterol <= 199:
        points += 2
    elif 200 <= cholesterol <= 239:
        points += (M*3) + (F*4)
    elif 240 <= cholesterol <= 279:
        points += (M*4) + (F*5)
    elif cholesterol >= 280:
        points += (M*5) + (F*7)
    if smoker == 1:
        points += (M * 3) + (F * 4)
elif 60 <= age <= 64:
    points += 10
    if 160 <= cholesterol <= 199:
        points += 1
    elif 200 <= cholesterol <= 239:
        points += (M*1) + (F*2)
    elif 240 <= cholesterol <= 279:
        points += (M*2) + (F*3)
    elif cholesterol >= 280:
        points += (M*3) + (F*4)
    if smoker == 1:
        points += (M*1) + (F*2)
elif 65 <= age <= 69:
    points += (M*11) + (F*12)
    if 160 <= cholesterol <= 199:
        points += 1
    elif 200 <= cholesterol <= 239:
        points += (M*1) + (F*2)
    elif 240 <= cholesterol <= 279:
        points += (M*2) + (F*3)
    elif cholesterol >= 280:
        points += (M*3) + (F*4)
    if smoker == 1:
        points += (M*1) + (F*2)
elif 70 <= age <= 74:
    points += (M*12) + (F*14)
    if 160 <= cholesterol <= 199:
        points += (F*1)
    elif 200 <= cholesterol <= 239:
        points += (F*1)
    elif 240 <= cholesterol <= 279:
        points += (M*1) + (F*2)
    elif cholesterol >= 280:
        points += (M*1) + (F*2)
    if smoker == 1:
        points += 1
elif 75 <= age <= 79:
    points += (M*13) + (F*16)
    if 160 <= cholesterol <= 199:
        points += (F*1)
    elif 200 <= cholesterol <= 239:
        points += (F*1)
    elif 240 <= cholesterol <= 279:
        points += (M*1) + (F*2)
    elif cholesterol >= 280:
        points += (M*1) + (F*2)
    if smoker == 1:
        points += 1

if HDL >= 60:
    points -= 1
elif 40 <= HDL <= 49:
    points += 1
elif HDL < 40:
    points += 2

if 120 <= BP <= 129:
    points += ((M*0) + (M*treated)) + ((F*1) + (F*2*treated))
elif 130 <= BP <= 139:
    points += ((M*1) + (M*treated)) + ((F*2) + (F*2*treated))
elif 140 <= BP <= 159:
    points += ((M*1) + (M*treated)) + ((F*3) + (F*2*treated))
elif BP >= 160:
    points += ((M*2) + (M*treated)) + ((F*4) + (F*2*treated))

# Post-processor
if (points < 0 and M == 1) or (points < 9 and F == 1):
    print("You have less than 1% 10-year risk of a heart attack.")
elif (points < 5 and M == 1) or (points < 13 and F == 1):
    print("You have a 1% 10-year risk of a heart attack.")
elif (points < 7 and M == 1) or (points < 15 and F == 1):
    print("You have a 2% 10-year risk of a heart attack.")
elif (points == 7 and M == 1) or (points == 15 and F == 1):
    print("You have a 3% 10-year risk of a heart attack.")
elif (points == 8 and M == 1) or (points == 16 and F == 1):
    print("You have a 4% 10-year risk of a heart attack.")
elif (points == 9 and M == 1) or (points == 17 and F == 1):
    print("You have a 5% 10-year risk of a heart attack.")
elif (points == 10 and M == 1) or (points == 18 and F == 1):
    print("You have a 6% 10-year risk of a heart attack.")
elif (points == 11 and M == 1) or (points == 19 and F == 1):
    print("You have a 8% 10-year risk of a heart attack.")
elif points == 12 and M == 1:
    print("You have a 10% 10-year risk of a heart attack.")
elif points == 13 and M == 1:
    print("You have a 12% 10-year risk of a heart attack.")
elif points == 14 and M == 1:
    print("You have a 16% 10-year risk of a heart attack.")
elif points == 15 and M == 1:
    print("You have a 20% 10-year risk of a heart attack.")
elif points == 16 and M == 1:
    print("You have a 25% 10-year risk of a heart attack.")
elif points >= 17 and M == 1:
    print("You have a 30% or more 10-year risk of a heart attack.")
elif points == 20 and F == 1:
    print("You have an 11% 10-year risk of a heart attack.")
elif points == 21 and F == 1:
    print("You have a 14% 10-year risk of a heart attack.")
elif points == 22 and F == 1:
    print("You have a 17% 10-year risk of a heart attack.")
elif points == 23 and F == 1:
    print("You have a 22% 10-year risk of a heart attack.")
elif points == 24 and F == 1:
    print("You have a 27% 10-year risk of a heart attack.")
elif points >= 25 and F == 1:
    print("You have a 30% or more 10-year risk of a heart attack.")


