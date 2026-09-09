status_code_num = int(input("enter status code num: 2,3,4,5 "))
match status_code_num:
    case 2:
        print("succes")
    case 3:
        print("redirect")
    case 4:
        print("client error")
    case 5:
        print("server error")
    case _:
        print("invalid")