energy_score = int(input("enter energy score: "))
if energy_score < 3:
    print("low")
elif energy_score >= 4 and energy_score <=7:
    print("moderate")
else:
    print("high")