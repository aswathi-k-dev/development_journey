exercise_in_minutes = int(input("enter minutes : "))
if exercise_in_minutes < 30:
    print("insufficient")
elif exercise_in_minutes >=30 and exercise_in_minutes <=60:
    print("good")
else:
    print("intense")