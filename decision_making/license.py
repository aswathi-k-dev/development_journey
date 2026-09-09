age = int(input("enter age :"))
if age > 18:
    test = input("yes/no :")
    if test == "yes":
        print("license approved")
    else:
        print("test not cleared")
else:
    print("not eligible due to age")