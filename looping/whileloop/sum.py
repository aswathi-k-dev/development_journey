num = int(input("enter the no: "))
sum = 0
while (num != 0):
    digit = num % 10
    sum = sum + digit
    num = num // 10
print(sum)
