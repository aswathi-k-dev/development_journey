atm_pin = 4563

for i in range(1,4):

    pin = int(input("enter the pin :"))

    if pin == atm_pin:

        print("UNLOCKED")

        break
else:

    print("BLOCKED")