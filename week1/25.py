def number_of_digits(n):
    count = 0
    while n > 0:
        count = count + 1
        n = n // 10
    return count


seconds = int(input())
minutes = 0
hours = 0
days = 0
if seconds > 60:
    minutes = int(seconds / 60)
    seconds = seconds % 60
    if minutes > 60:
        hours = int(minutes / 60)
        minutes = minutes % 60
        if hours > 24:
            days = int(hours / 24)
            hours = hours % 24
if number_of_digits(seconds) == 1 or seconds == 0:
    seconds = "0" + str(seconds)
if number_of_digits(minutes) == 1 or minutes == 0:
    minutes = "0" + str(minutes)
if number_of_digits(hours) == 1 or hours == 0:
    hours = "0" + str(hours)
if number_of_digits(days) == 1 or hours == 0:
    days = "0" + str(days)
print(str(days) + ":" + str(hours) + ":" + str(minutes) + ":" + str(seconds))
