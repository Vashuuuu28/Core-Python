import datetime
dob = datetime.date(2007,1,28)
today = datetime.date.today()

age = today.year - dob.year #age
born_day = dob.strftime("%A")  #day which is born
print("age is",age)
print("day of birth is",born_day)