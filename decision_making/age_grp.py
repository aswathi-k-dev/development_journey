age_grp = int(input("enter age : "))
if age_grp < 13 :
    print("child")
elif age_grp >=13 and age_grp <=19:
    print("teen")
elif age_grp >=20 and age_grp <=59:
    print("adult")
else:
    print("senior")
