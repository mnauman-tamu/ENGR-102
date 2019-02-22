# ComparingArrayValues.py
#
# This program attempts to complete part one of lab_07 and receive a grade of 100
#
# Patrick Zhong
# Muhammad Nauman
# Daniel Huck
# Alexander Bogdan
#
# October 8th, 2018
# ENGR 102-213

print("Negative values will be treated as ending the list")
WidgetNumber = 0
ArrayOfWidgetDays = []


while WidgetNumber >= 0:
    WidgetNumber = float(input("How many widgets did you make today?\n"))
    if WidgetNumber >= 0:
        ArrayOfWidgetDays.append(WidgetNumber)

NumberOfLoops = 1
IncreaseArray = []
print("")
while NumberOfLoops < len(ArrayOfWidgetDays):
    IncreaseArray = []
    Iterations = 0
    TimesNoChange = 0
    while NumberOfLoops + Iterations + 1 <= len(ArrayOfWidgetDays):
        IncreaseArray.append(float(bool(ArrayOfWidgetDays[Iterations+NumberOfLoops] - ArrayOfWidgetDays[Iterations] >= 0)))
        if bool(ArrayOfWidgetDays[Iterations+NumberOfLoops] - ArrayOfWidgetDays[Iterations] == 0):
            TimesNoChange = TimesNoChange + 1
        Iterations = Iterations + 1
    PercentIncrease = 100*((sum(IncreaseArray)-TimesNoChange)/Iterations)
    PercentDecrease = 100*((Iterations-sum(IncreaseArray))/Iterations)
    PercentIncrease = format(PercentIncrease, '.1f')
    PercentDecrease = format(PercentDecrease, '.1f')
    print("For " + str(NumberOfLoops) + " day intervals there was a " + str(PercentIncrease) + "% increase and a " + str(PercentDecrease) + "% decrease")
    NumberOfLoops = NumberOfLoops+1
print("Maximum production rate was " + str(max(ArrayOfWidgetDays)) + " per day")
print("Minimum production rate was " + str(min(ArrayOfWidgetDays)) + " per day")
print("Average production rate was " + str(sum(ArrayOfWidgetDays)/len(ArrayOfWidgetDays)) + " per day")
