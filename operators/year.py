year = int(input("enter year :"))
is_leap_year = year % 100 != 0 and year % 4 ==0
print(is_leap_year)