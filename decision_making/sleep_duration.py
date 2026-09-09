sleep_duration = int(input("enter sleep duration : "))
if sleep_duration < 6 :
    print("speed deprived")
elif sleep_duration >= 6 and sleep_duration < 8:
    print("healthy sleep")
else:
    print("over sleeping")