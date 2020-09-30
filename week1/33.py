num = int(input("Number of loaves: "))
initialPrice = 3.49
dayOldPrice = initialPrice - initialPrice*0.6
print("Regular price of bread: ", format(round(initialPrice*num, 2)), "$")
print("Discount: ", format(round(initialPrice*num - dayOldPrice*num, 2)), "$")
print("Total price: ", format(round(num*dayOldPrice, 2)), "$")
