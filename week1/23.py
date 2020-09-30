import math
s = float(input("Length of polygon's side: "))
n = float(input("# of sides: "))
area = n*pow(s, 2)/4*math.tan(math.pi/n)
print("Area of polygon: ", format(round(area, 2)))