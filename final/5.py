n = int(input())
arr = []
for i in range(n):
    arr.append([int(i) for i in input().split()])
for i in arr:
    if i[0] % i[1] == 0:
        print("YES")
    else:
        print("NO")
