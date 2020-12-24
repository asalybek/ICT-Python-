n = int(input())
s = input()
s_to_f = 0
f_to_s = 0

prev = s[0]
for curr in s[1:]:
    if prev == 'S' and curr == 'F':
        s_to_f += 1
    elif prev == 'F' and curr == 'S':
        f_to_s += 1
    prev = curr

if s_to_f > f_to_s:
    print("YES")
else:
    print("NO")
