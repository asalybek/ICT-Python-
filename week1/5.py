oneOrLess = int(input("# of containers holding one liter or less: "))
moreThanOne = int(input("# of containers holding more than one liter: "))
print("Refund that will be received: " + format(round(oneOrLess*0.1 + moreThanOne*0.25, 2)) + " $")
