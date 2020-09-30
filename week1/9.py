def two_decimal_places(n):
    return format(round(n, 2))


initialMoney = float(input("Deposited money: "))
firstYear = initialMoney*1.04
secondYear = firstYear*1.04
thirdYear = secondYear*1.04
print("1st Year: " + two_decimal_places(firstYear))
print("2nd Year: " + two_decimal_places(secondYear))
print("3rd Year: " + two_decimal_places(thirdYear))



