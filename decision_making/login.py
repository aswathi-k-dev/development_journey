db_username = "aswathii"

db_password = 2006

user_name = input("enter username :")

if user_name == db_username:

    password = int(input("enter password :"))

    if password == db_password:

        print("LOGIN SUCCESFULL")

    else:

        print("invalid password")
else:
    
    print("invalid username")

