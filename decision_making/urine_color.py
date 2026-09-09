urine_color = int(input("enter level : "))
if urine_color < 3:
    print("well hydrated")
elif urine_color > 4 and urine_color <=6:
    print("mild dehydration")
else:
    print("severe")