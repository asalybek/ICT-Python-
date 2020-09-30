num = int(input("4-digit number: "))
num = str(num)
arr = []
for i in num:
    arr.append(int(i))
print("Sum of digits: ", sum(arr))
