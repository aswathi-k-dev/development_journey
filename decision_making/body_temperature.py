body_temp = int(input("enter body temperature :"))
if body_temp < 36:
    print("low")
elif body_temp >=36 and body_temp < 38:
    print("normal")
else:
    print("fever")