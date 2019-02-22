# InterpolationFunctions.py
#
# Attempts to complete part 2 of lab 11 and receive a grade of 100.
#
# Alexander Bogdan
# Patrick Zhong
# Muhammad Nauman
# Daniel Huck
# ENGR 102-213
#
# Lab 9, Activity 2

from scipy import interpolate
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

File = pd.read_csv('H2O_TempSat.csv')
File.columns = File.iloc[2]
File = File.reindex(File.index.drop(0))
File = File.reindex(File.index.drop(1))
File = File.reindex(File.index.drop(51))
File = File.dropna(axis='columns')

FileNp = File.values
FileNp = FileNp.astype(np.float)

Deg_C = FileNp[:, 0]

MPa = FileNp[:, 1]
MPaF = interpolate.interp1d(Deg_C, MPa)

Vf = FileNp[:, 2]
VfF = interpolate.interp1d(Deg_C, Vf)

Vg = FileNp[:, 3]
VgF = interpolate.interp1d(Deg_C, Vg)

Uf = FileNp[:, 4]
UfF = interpolate.interp1d(Deg_C, Uf)

Ug = FileNp[:, 5]
UgF = interpolate.interp1d(Deg_C, Ug)

Hf = FileNp[:, 6]
HfF = interpolate.interp1d(Deg_C, Hf)

HfG = FileNp[:, 7]
HfGF = interpolate.interp1d(Deg_C, HfG)

Hg = FileNp[:, 8]
HgF = interpolate.interp1d(Deg_C, Hg)

Sf = FileNp[:, 9]
SfF = interpolate.interp1d(Deg_C, Sf)

SfG = FileNp[:, 10]
SfGF = interpolate.interp1d(Deg_C, SfG)

Sg = FileNp[:, 11]
SgF = interpolate.interp1d(Deg_C, Sg)


def interpolationstuff(x):
    return {'MPa': float(MPaF(x)), 'Vf': float(VfF(x)), 'Vg': float(VgF(x)),
            'Uf': float(UfF(x)), 'Ug': float(UgF(x)), 'Hf': float(HfF(x)), 'HfG': float(HfGF(x)),
            'Hg': float(HgF(x)), 'Sf': float(SfF(x)), 'SfG': float(SfGF(x)), 'Sg': float(SgF(x))}


TempValue = -42
Results = 0
while not (1 < TempValue < 373):
    TempValue = float(input("Input a temperature value between 1 and 373, has to be between"))
    Results = interpolationstuff(TempValue)

print(Results)
print("The pressure is " + str(9.86923 * Results['MPa']) + " atm")
print("The fluid density is " + str(1/Results['Vf']) + " kg/m3")

Temps = np.arange(5, 35)

plt.plot(Temps, MPaF(Temps))
plt.ylabel('Pressure in Mpa')
plt.xlabel('Celsius')
plt.show()
