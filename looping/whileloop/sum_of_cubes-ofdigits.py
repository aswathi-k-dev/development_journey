num = int(input("enter the no: "))
sum = 0
while (num != 0):
    digit = num % 10
    cube = digit ** 3
    sum = cube + sum
    num = num // 10
print(sum)