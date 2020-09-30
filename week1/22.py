import math
a = float(input("Length of first side: "))
b = float(input("Length of second side: "))
c = float(input("Length of third side: "))
p = (a+b+c)/2
area = math.sqrt(p*(p-a)*(p-b)*(p-c))
print("Area of triangle: ", format(round(area, 2)))