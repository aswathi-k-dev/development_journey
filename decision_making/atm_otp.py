""" LOGIN SYSTEM WITH OTP AND PASSWORD"""

db_password = "aswathii"

db_otp = 3456

password =input("enter the password :" )

if password == db_password:

    otp = int(input("enter the otp :"))

    if otp == db_otp:

        print("Login successfull")

    else:

        print("Incorrect Otp")

else:

    print("invalid password")
