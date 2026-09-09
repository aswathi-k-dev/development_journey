num = int(input("enter the no: "))
while (num != 0):
    digit = num % 10
    cube = digit ** 3
    print(cube)
    num = num // 10

