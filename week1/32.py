arr = []
for i in range(3):
    a = int(input())
    arr.append(a)
sortedArr = [min(arr), sum(arr) - max(arr) - min(arr), max(arr)]
print(sortedArr)