"""" blood sugar"""

blood_sugar_level = int(input("enter the blood sugar: "))
if blood_sugar_level < 100:
    print("normal")
elif blood_sugar_level >= 100 and blood_sugar_level <= 125:
    print("prediabetes")
else:
    print("diabetes")