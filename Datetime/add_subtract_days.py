import datetime
today = datetime.date.today()
future = today + datetime.timedelta(days=10)
past = today - datetime.timedelta(days=10)

print("date after 10 days is",future)
print("date before 10 days from today is ",past)
print("daye today is",today)

