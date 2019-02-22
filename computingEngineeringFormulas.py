# computingEngineeringFormulas.py
#
# Compute engineering formulas using user inputs
#
# Muhammad Nauman
# UIN: 927008027
# September 10, 2018
# ENGR 102-213
#
# Lab 3B - 1


# Pre-processor (1)
print("The energy radiated per unit surface area for a black body of a given temperature in Kelvin. Because the Stefan-"
      "Boltzmann constant is a universal constant, you should include this variable in your code in the appropriate "
      "units; you should not ask the user to input this value.")
SB_constant = 5.67e-8
surface_area = input("Surface area in m^2: ")
temperature = input("Temperature in K: ")

# Processor (1)
energy = SB_constant * float(surface_area) * (int(temperature)**4)

# Post-processor (1)
print("The energy radiated is " + str(energy) + " W.")


# Pre-processor (2)
print()
print("The kinetic energy of an object with mass in kg and velocity in m/s.")
mass = input("Mass in kg: ")
velocity = input("Velocity in m/s: ")

# Processor (2)
kinetic_energy = 0.5 * float(mass) * (int(velocity)**2)

# Post-processor (2)
print("The kinetic energy in Newtons is:")
print(kinetic_energy)
print()


# Pre-processor (3)
print("The Reynolds number of an object of a given length in ft, velocity in ft/s, and kinematic viscosity in ft2/s. ")
length = input("Length in ft: ")
velocity_3 = input("Velocity in ft/s: ")
print("Typical values of kinematic viscosity of air, water, and nitrogen at atmospheric temperature are "
      "1.57 x 10^-4 ft^2/s, 1.23 x 10^-5 ft^2/s, and 1.46 x 10^-4 ft^2/s, respectively.")
k_viscosity = input("Kinematic viscosity in ft^2/s: ")

# Processor (3)
R_number = float(velocity_3) * float(length) / float(k_viscosity)

# Post_processor (3)
print("The Reynolds number is: " + str(R_number))
print()

# Pre-processor (4)
print("The production rate of a well after a given number of days.")
init_rate = input("Initial production rate in barrels per day: ")
decline_rate = 1
hyperbolic_const = input("Hyperbolic constant (between 0.0 and 1.0): ")
time = input("Time in days: ")

# Processor (4)
prod_rate = float(init_rate)/((1 + float(hyperbolic_const)*decline_rate * float(time))**(1/float(hyperbolic_const)))
prod_rate_in_m3 = prod_rate * 1.38009805e-6

# Post-processor (4)
print("The Production rate in barrels per day is " + str(prod_rate))
print("The Production rate in m^3/s is " + str(prod_rate_in_m3))

