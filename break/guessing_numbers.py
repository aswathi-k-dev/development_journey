from random import randint

secret_number = randint(1,10)

for i in range(1,6):

    num = int(input("enter the number:"))

    if num == secret_number:

        print("CONGRATULATIONS 🤩")

        break

else:

    print("BAD LUCK 🥲")

    

