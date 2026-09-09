x1 = int(input("enter x1: "))
y1 = int(input("enter y1: "))

x2 = int(input("enter x2: "))
y2= int(input("enter y2: "))

x3 = int(input("enter x3: "))
y3 = int(input("enter y3: "))

slope_1 = (y2 - y1)/(x2 - x1)
slope_2 = (y3 - y2)/(x3 - x2)

if slope_1 == slope_2:
    print("points are in straight line")
else:
    print("points are not in straight line")
