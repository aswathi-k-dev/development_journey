num = int(input("enter the no to find factorial: "))

i = 1
product = 1

while(i <= num):
     product  = product * i
     i = i + 1
print(f"factorial of {num} = {product}")
