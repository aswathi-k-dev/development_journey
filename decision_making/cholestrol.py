cholestrol = int(input("enter cholestrol level : "))
if cholestrol < 200 :
    print("desirable")
elif cholestrol >=200 and cholestrol <=239:
    print("borderline")
else:
    print("high")