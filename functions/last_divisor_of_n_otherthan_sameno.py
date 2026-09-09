num = int(input("enter number : "))
for i in range(num-1,1,-1):
    if num % i == 0:
        print(i)
        break
