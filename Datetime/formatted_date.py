import datetime
today = datetime.date.today()

formated = today.strftime("%d-%m-%y")
print("formated date:",formated)