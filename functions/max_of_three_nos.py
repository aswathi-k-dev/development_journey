def max_of_three(num1,num2,num3):
    if num1>num2 and num1 > num3:
        print("num1 is maximum",num1)
    elif num2>num1 and num2>num3:
        print("num2 is maximum",num2)
    else:
        print("num3 is maximum",num3)
max_of_three(7,6,8)
max_of_three(8,9,12)
max_of_three(56,78,45)