def is_distint_num(year):
    if len(set(str(year))) == 4:
        return True
    return False


year = int(input())
while True:
    year += 1
    if is_distint_num(year):
        print(year)
        exit()
