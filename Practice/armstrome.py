number = 153
n = number
rem = 0
sum = 0

while n > 0:
    rem = n%10
    sum = sum + rem*rem*rem
    n = n // 10

if sum == number:
    print("yes this no. is armstrome")
else:
    print("not armstrome")