angle_1 = int(input("enter angle1 :"))

angle_2 = int(input("enter angle2 :"))

angle_3 = int(input("enter angle3 :"))

if angle_1 > 0 and angle_2 > 0 and angle_3 > 0:
   if angle_1 + angle_2 + angle_3 == 180:
    print("triangle can be created")
   else:
    print("cannot create a triangle")
else:
  print("values are less than 0")


    
    
