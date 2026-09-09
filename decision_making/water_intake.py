water_intake = int(input("enter water in litres : "))
if water_intake < 2:
    print("dhydrated")
elif water_intake >=2 and water_intake <=3:
    print("adequate")
else:
    print("excess")