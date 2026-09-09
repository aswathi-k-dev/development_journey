num_1= int(input("enter number: "))
num_2 = int(input("enter number: "))
i = 1
gcd = 1
while (i<= num_1 and i <= num_2):
    if num_1 % i == 0 and num_2 % i == 0:
        gcd = i
    i = i + 1
print(gcd)

