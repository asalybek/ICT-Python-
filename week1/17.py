m = float(input("Mass of water: "))
t = float(input("Temperature of water: "))
q = m*4186*t
electricity = q*1/3600000*8.9
print("q = ", format(round(q)), "Jl")
print("Electricity costs = ", format(round(electricity)), "cents")
