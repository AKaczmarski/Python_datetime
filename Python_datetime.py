import datetime

now = datetime.datetime.now()
print(now)
print(now.ctime())

month = str(now.month)
day = str(now.day)
year = str(now.year)
hour = str(now.hour)
minute = str(now.minute)
second = str(now.second)

print(day + "." + month + "." + year + "    " + hour + ":" + minute + ":" + second)

print("Press Enter to close the program...")
input()
