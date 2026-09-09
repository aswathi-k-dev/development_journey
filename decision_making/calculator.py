num_1 = int(input("enter number 1: "))
num_2 = int(input("enter number 2: "))
operator = input("enter operator : + , - , * , / ")
match operator:
    case "+":
        print("addition:",num_1 +num_2)
    case "-":
        print("subtraction:",num_1 -num_2)
    case "*":
        print("multiplication:",num_1 * num_2)
    case "/":
        print("division:",num_1 /num_2)
    case _:
        print("invalid")

        


