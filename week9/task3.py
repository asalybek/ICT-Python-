# 1
# s = input()
# res = s
# for i in range(len(s)):
#     if s[i] == "A" or s[i] == "a" or s[i] == "O" or s[i] == "o" or s[i] == "Y" or s[i] == "y" or s[i] == "I" or \
#             s[i] == "i" or s[i] == "E" or s[i] == "e" or s[i] == "U" or s[i] == "u":
#         res = res.replace(s[i], '')
# res_new = res
# for i in range(len(res_new)):
#     res_new = res_new.replace(res[i], '.' + res[i])
# print(res_new.lower())

# 2
# s = input()
# arr = s.split("+")
# map_str = map(int, arr)
# list_of_integers = list(sorted(map_str))
# s_upd = ""
# for i in range(len(list_of_integers)):
#     s_upd += str(list_of_integers[i]) + "+"
# print(s_upd[: len(s_upd) - 1])

# 3
# s = input()
# print(s[0].upper() + s[1:])

# 4
# positions = input()
# if '0000000' in positions or '1111111' in positions:
#     print("YES")
# else:
#     print("NO")

# 5
# username = input()
# if len(set(username)) % 2 != 0:
#   print("IGNORE HIM!")
# else:
#   print("CHAT WITH HER!")

# 6
# upper = 0
# lower = 0
# s = input()
# res = ""
# for i in range(0, len(s)):
#     if s[i] >= 'a':
#         lower = lower + 1
#     else:
#         upper = upper + 1
#
# if upper > lower:
#     res = s.upper()
# else:
#     res = s.lower()
#
# print(res)

# 7
# n = int(input())
# s = input().lower()
# res = False
# for i in range(97, 123):
#     if chr(i) in s:
#         res = True
#     else:
#         res = False
# if res:
#     print("YES")
# else:
#     print("NO")

# 8
# s = input()
# t = input()
# s = "".join(reversed(s))
# if t == s:
#     print("YES")
# else:
#     print("NO")

# 9
# n = int(input())
# s = input()
# cnt_d = s.count('D')
# cnt_a = s.count('A')
# if cnt_a == cnt_d:
#     print("Friendship")
# elif cnt_d > cnt_a:
#     print("Danik")
# else:
#     print("Anton")

# 10
# s = input()
# if s.isupper():
#     print(s.lower())
# elif s.islower():
#     print(s.upper())
# elif s[0].lower() and s[1:].isupper():
#     print(s[0].capitalize() + s[1:].lower())
# else:
#     print(s)

# 11
# n = int(input())
# s = input()
# res = ""
# cnt_z = s.count('z')
# cnt_e = s.count('e')
# cnt_r = s.count('r')
# cnt_o = s.count('o')
# cnt_n = s.count('n')
# while cnt_n > 0 and cnt_o > 0 and cnt_e > 0:
#     res += "1 "
#     cnt_n -= 1
#     cnt_o -= 1
#     cnt_e -= 1
# while cnt_z > 0 and cnt_o > 0 and cnt_r > 0 and cnt_e > 0:
#     res += "0 "
#     cnt_z -= 1
#     cnt_o -= 1
#     cnt_e -= 1
#     cnt_r -= 1
# print(res[:len(res) - 1])

# 12
# n = int(input())
# s = input()
# cnt = 0
# for i in range(0, len(s) - 2):
#     if s[i] == 'x' and s[i + 1] == 'x' and s[i + 2] == 'x':
#         cnt += 1
# print(cnt)
