t = float(input("Temperature: "))
s = float(input("Speed of the wind: "))
wci = 0
if t <= 10 and s > 4.8:
    wci = float(13.12 + 0.6215 * t - 11.37 * pow(s, 0.16) + 0.3965 * t * pow(s, 0.16))
    print("Wind chill index(WCI): ", wci)
    exit()
if t > 10:
    print("In given temperature wci can not be calculated.")
    exit()
if s <= 4.8:
    print("In given speed wci can not be calculated.")
    exit()
else:
    print("In given temperature and speed wci can not be calculated.")