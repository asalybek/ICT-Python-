n = int(input())
arr = [int(i) for i in input().split()]
arr.sort()
cnt = 0
for i in range(0, n - 1):
    if arr[i+1]-arr[i] > 1:
        cnt += arr[i+1]-arr[i]-1
print(cnt)
