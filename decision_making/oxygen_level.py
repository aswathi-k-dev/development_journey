oxygen_level= int(input("enter oxygen level :"))
if oxygen_level < 60 :
    print("low")
elif oxygen_level >= 60 and oxygen_level < 100:
    print("normal")
else:
    print("critical")