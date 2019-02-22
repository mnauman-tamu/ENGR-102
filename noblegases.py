# Noble Gases
#
# Calculates density of a given gas at a given pressure and temperature
#
# Patrick Zhong
# Muhammad Nauman
# Daniel Huck
# Alexander Bogdan
# ENGR 102-213
#
# Lab 7, Activity 2: Noble Gases

gases = {
    "hydrogen": ("H", 1, 1.008, 20.271),
    "helium": ("He", 2, 4.0026, 4.222),
    "neon": ('Ne', 10, 20.180, 27.1),
    "argon": ('Ar', 18, 39.948, 87.3),
    "krypton": ('Kr', 36, 83.798, 119.7),
    "xenon": ('Xe', 54, 131.29, 165),
    "radon": ('Rn', 86, 222, 211.4),
}

airDens = 1.225  # kg / m^3

name = ""
while name not in gases:
    name = input("Enter the chemical name: ").lower()
    if name not in gases:
        print("Invalid chemical name.")

pressure = float(input("Enter the temperature in degrees Kelvin: "))
temp = float(input("Enter the pressure in atmospheres: "))

gas = gases[name]
density = gas[2] * pressure / (temp * 0.08206)  # g / L
density *= 1/1000 * 0.001  # kg / m^3

if density > 10 * airDens:
    print("The gas at these conditions does not behave as an ideal gas.")
else:
    print("Chemical name: " + name)
    print("Chemical symbol: " + gas[0])
    print("Density: " + str(density) + " kg/m^3")
    print("Density: " + str(density * 2.20462 * 0.3048**3) + " lb/ft^3")
    print("Boiling point: " + str(gas[3]) + " degrees Kelvin")
    print("Boiling point: " + str(gas[3] - 273.15) + " degrees Celsius")
    print("Boiling point: " + str(gas[3] * 1.8) + " degrees Rankine")
    print("Boiling point: " + str((gas[3] - 273.15) * 9/5 + 32) + " degrees Fahrenheit")
