""" ATM WITHDRAWAL"""

db_pin = 1234
db_balance = 6000
pin = int(input("enter the pin :" ))
if pin == db_pin:
    amount = int(input("enter the amount :"))
    if amount<=db_balance:
        print("withdrawal successfull")
    else:
        print("insufficient balance")
else:
    print("invalid pin")

    