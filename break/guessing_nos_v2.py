from random import randint
secret_number = randint(1,10)

for i in range(1,6):

    num = int(input("guess the number :"))

    if num == secret_number:

        print("CONGRATULATIONS 🤩")

        break

    elif num < secret_number:

        print("too low")

    elif num > secret_number:
        print("TOO HIGH")


else:

    print("BAD LUCK 🥲")
