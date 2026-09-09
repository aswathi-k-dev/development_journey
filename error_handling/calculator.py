num1 = int(input("enter num1: "))
num2 = int(input("enter num2: "))
try:
    operation = input("select operation + - * / ")
    result = 0
    if operation == "+" :
        result = num1 + num2
    elif operation == "-":
        result = num1 - num2
    elif operation == "*":
        result = num1 * num2
    elif operation == "/":
        result = num1 /num2
    else:
        print("invalid")
except Exception as e:
    print(e)
else:
    print(result)
    
        
    





    