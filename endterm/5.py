n = int(input())
sum1 = 0
sum2 = 0
sum3 = 0
while n > 0:
    a, b, c = input().split(" ")
    sum1 += int(a)
    sum2 += int(b)
    sum3 += int(c)
    n -= 1

if sum1 == 0 and sum2 == 0 and sum3 == 0:
    print("YES")
else:
    print("NO")

