sales = [100000,120000,110000,130000,150000]

# march month sales

march_month_sales = sales[2]
print(march_month_sales)

# update may month sales as 105000

sales[4] = 105000
print(sales)

#dispaly all sales using index

print("---- using index ----")

for i in range(0,len(sales)):
    print(sales[i])

# display sales > 100000

print("---- sales more than 1lakh ----")

for amount in sales:
    if amount > 10000:
        print(amount)

