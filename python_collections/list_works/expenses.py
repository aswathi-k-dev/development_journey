expenses = [12000,11000,15000,16000,13000,17000]
       #       0    1      2     3     4     5

march_month_exp = expenses[0]
print(march_month_exp)

# update jan month exp as 15000

expenses[0] = 15000
print(expenses)

# using index

print("--------- using index ----------")

for i in range(0,len(expenses)):
    print(expenses[i])

# using in

print("---------- using in ---------------")

for amount in expenses:
    print(amount)