year = int(input("enter year :"))
if year %100!=0 and year %4==0:
    print("year is not divisible by 100 and divisible by 4")
else:
    print("year is  divisible by 100 and not divisible by4")
