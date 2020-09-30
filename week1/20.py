p = int(input("Pressure: "))
v = int(input("Volume: "))
t = int(input("Temperature: "))
print("n(amount of gas in moles) = ", format(round((p*v)/(8314*t))))