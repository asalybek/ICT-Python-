num = int(input())
cnt = 0
for i in range(1, int(num / 2 + 1)):
    if (num - i) % i == 0:
        cnt += 1
print(cnt)
