print("Given duration - ")
days = int(input("Days: "))
hours = int(input("Hours: "))
minutes = int(input("Minutes: "))
seconds = int(input("Seconds: "))
durationInSeconds = (days*24*60*60) + (hours*60*60) + (minutes*60) + seconds
print("Duration converted to seconds: ", durationInSeconds)