# 1
# x1 = int(input())
# y1 = int(input())
# x2 = int(input())
# y2 = int(input())
#
# if (x1 - x2) * (y1 - y2) == 0:
#     print("YES")
# else:
#     print("NO")

# 2
# a = int(input())
# b = int(input())
# a1 = int(input())
# b1 = int(input())
# if (abs(a - a1) == 1 or a == a1) and (abs(b - b1) == 1 or b == b1):
#     print("YES")
# else:
#     print("NO")

# 3
# x1 = int(input())
# y1 = int(input())
# x2 = int(input())
# y2 = int(input())
# if abs(x1 - x2) == abs(y1 - y2):
#     print("YES")
# else:
#     print("NO")

# 4
# a = int(input())
# b = int(input())
# a1 = int(input())
# b1 = int(input())
# if ((a1 - a) * (b1 - b) == 0) or (abs(a - a1) == abs(b - b1)):
#     print("YES")
# else:
#     print("NO")

# 5
# x1 = int(input())
# y1 = int(input())
# x2 = int(input())
# y2 = int(input())
# if abs(x2 - x1) + abs(y2 - y1) == 3:
#     print("YES")
# else:
#     print("NO")

# 6
# n = int(input())
# m = int(input())
# k = int(input())
# if (k % n == 0 or k % m == 0) and k < n * m:
#     print("YES")
# else:
#     print("NO")

# 7
# n = int(input())
# m = int(input())
# x = int(input())
# y = int(input())
# dist_x, dist_y = 0, 0
# if n > m:
#     dist_x = min(abs(n - y), y)
#     dist_y = min(abs(m - x), x)
# else:
#     dist_x = min(abs(m - y), y)
#     dist_y = min(abs(n - x), x)
#
# print(min(dist_x, dist_y))

# 8
# a = int(input())
# b = int(input())
# c = int(input())
# arr = [a, b, c]
# arr.sort()
# for i in arr:
#     print(i, end=" ")

# 9
# a1 = float(input())
# b1 = float(input())
# c1 = float(input())
# a2 = float(input())
# b2 = float(input())
# c2 = float(input())
# if (a1 == a2) and (b1 == b2) and (c1 == c2):
#     print("Boxes are equal")
# elif (a1 >= a2) and (b1 >= b2) and(c1 >= c2):
#     print("The first box is larger than the second one")
# elif (a1 <= a2) and (b1 <= b2) and (c1 <= c2):
#     print("The first box is smaller than the second one")
# else:
#     print("Boxes are incomparable")


# 10
# n = int(input())
# for i in range(1, n):
#     if i*i <= n:
#         print(i*i, end=" ")

# 11
# num = int(input())
# i = 2
# while i <= num:
#     i = i + 1
#     if num % i == 0:
#         print(i)
#         break

# 12
# n = int(input())
# prod = 1
# for i in range(1, n):
#     prod = prod*2
#     if prod <= n:
#         print(prod, end=" ")

# 13
# num = int(input())
# summa = 0
# if num != 0:
#     summa = num
# else:
#     exit()
# while num != 0:
#     num = int(input())
#     summa = summa + num
#
# print(summa)

# 14
# a = int(input())
# arr = []
# if a != 0:
#     arr = [a]
# else:
#     exit()
# while a != 0:
#     a = int(input())
#     arr.append(a)
# maxi = max(arr)
# cnt = 0
# for i in arr:
#     if i == maxi:
#         cnt = cnt + 1
# print(cnt)

# 15
# n = int(input())
# count = 1
# fib0 = 0
# fib1 = 1
# fib_n = 1
# while fib_n < n:
#     fib_n = fib0 + fib1
#     fib0 = fib1
#     fib1 = fib_n
#     count = count + 1
# if fib_n == n:
#     print(count)
# else:
#     print(-1)

# 16
# a = int(input())
# arr = []
# if a != 0:
#     arr = [a]
# else:
#     exit()
# while a != 0:
#     a = int(input())
#     arr.append(a)
# cnt = 0
# for i in range(1, len(arr) - 1):
#     if arr[i - 1] < arr[i] > arr[i + 1]:
#         cnt = cnt + 1
# print(cnt)

# 17
# n = int(input())
# arr = input().split()
# print(len(set(arr)))

# 18
# n = int(input())
# arr = input().split()
# arr2 = [arr[n-1]]
# for i in range(0, n-1):
#     arr2.append(arr[i])
# for i in arr2:
#     print(i, end=" ")

# 19
# n = int(input())
# arr = []
# for i in range(n):
#     a = int(input())
#     arr.append(a)
# arr2 = set(arr)
# print(len(arr) - len(arr2))
