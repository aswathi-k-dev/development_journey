screen_time_in_hrs = int(input("enter screen time : "))
if screen_time_in_hrs < 2:
    print("healthy")
elif screen_time_in_hrs >=2 and screen_time_in_hrs <=5:
    print("moderate")
else:
    print("excessive")