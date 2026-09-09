steps = int(input("enter steps: "))
if steps < 5000:
    print("sedentary")
elif steps < 10000:
    print("moderately active")
else:
    print("active")
