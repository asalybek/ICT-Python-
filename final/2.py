n = int(input())
ans = 0
maxi = 0
for i in range(1, n + 1):
    here = n
    stp = 0
    for j in range(i):
        check = (i - j) * (j + 1)
        if here - check > 0:
            stp += 1
            here -= check
        else:
            break
    if stp > maxi:
        maxi = stp
        ans = i
if n == 1:
    print(1)
else:
    print(ans)
