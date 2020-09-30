import math
radius = float(input("Radius: "))
height = float(input("Height: "))
volume = math.pi*pow(radius, 2)*height
print("Volume of a cylinder: ", format(round(volume, 1)))