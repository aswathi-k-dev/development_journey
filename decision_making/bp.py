"""blood_pressure"""

bp = int(input("enter blood pressure :"))
if bp < 120 :
    print("normal")
elif bp >= 120 and bp <= 129:
    print("elevated")
elif bp >=130 and bp <= 139:
    print("high bp stage 1")
else:
    print("high bp stage 2")