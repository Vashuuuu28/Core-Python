import datetime

today = datetime.date.today()
future = today + datetime.timedelta(days = 10)
past = today - datetime.timedelta(days = 10)

print(today)
print(future)
print(past)