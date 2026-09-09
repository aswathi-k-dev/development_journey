calories = int(input("enter calorie: "))
if calories < 1500:
    print("low")
elif calories > 1500 and calories < 2500:
    print("balnced")
else:
    print("excess")