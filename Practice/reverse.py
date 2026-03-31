number = 178987456312
n = number
sum = 0
rem = 0

while n > 0:
    rem = n%10
    sum = (sum*10) + rem
    n = n // 10
print("numbers reverse is",sum)