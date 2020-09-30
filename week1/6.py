initialCost = int(input("The cost of a meal ordered:"))
tip = initialCost*0.18
tax = initialCost*0.2
print("Tip amount: " + format(round(tip, 2)))
print("Tax amount: " + format(round(tax, 2)))
print("Grand total: " + format(round(tip+tax+initialCost, 2)) + " $")