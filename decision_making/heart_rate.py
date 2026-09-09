""""heart rate"""

heart_rate= int(input("enter heart rate :"))
if heart_rate < 60 :
    print("low")
elif heart_rate >= 60 and heart_rate < 100:
    print("normal")
elif heart_rate >=100:
    print("high")