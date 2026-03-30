import datetime

d = datetime.datetime.now()

print("current hour is",d)

print(d.year)
print(d.month)
print(d.day)
print(d.hour)
print(d.minute)
print(d.second)
print(d.microsecond)
print(d.strftime("%Y-%M-%D %H:%M:%S"))          #%Y = year   ,  %m = month  ,  %d = day  ,  %H = hour  ,  %M  = minute  ,  %s = second
print(d.strftime("%A, %B %d, %Y"))          #%A = day(monday)  ,  %B = month name    ,  %d = day    ,  %Y = year
print(d.min)
print(d.max)