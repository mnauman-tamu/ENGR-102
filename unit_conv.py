# unit_conv.py
#
# A program to convert among a wide range of units.
#
# S. Socolofsky
# ENGR 102
# October 2018

# Pre-processor:  Get Input Data ---------------------------------------------

# Describe program and give user instructions
print('Program unit_conv.py')
print('\nConvert among a wide array of units.')
print('\nInstructions: ')
print('-------------')
print('    Inputs must be in fundamental MKS or FPS units')
print('    Enter input as a number followed by fundmental unit abbreviations')
print('    Separate input number and each unit by a space')
print('    Use "/" to separate the numerator from the denominator for a' +
      '\n        mixed set of units.\n')
print('    For example, type:  12.45 ft / s^2\n')

# Ask user to input a number and a unit
in_val = input('Enter a number and a unit:  ')

# Build a dictionary of basic units in MKS.  Let the MKS unit be the key to
# the dictionary.  The dictionary entry is a list that contains the
# corresponding FPS unit and the conversion factor from MKS to FPS.
mks_units = {'m' : ['ft',  3.28084],
             'kg' : ['lbm', 2.20462],
             's' : ['s', 1.0],
             'N' : ['lbf', 20.224809],
            }

# Build the inverse dictionary that goes from FPS to MKS
fps_units = {}     # Create an empty dictionary
for unit in mks_units:
    fps_units[mks_units[unit][0]] = [unit, 1. / mks_units[unit][1]]

# Tests for pre-processor
print('\nYou entered: ', in_val)
print('The conversion factor from m to ft is', mks_units['m'][1])
print('The conversion factor from ft to m is', fps_units['ft'][1])
print('The FPS unit corresponding to m is', mks_units['m'][0])
