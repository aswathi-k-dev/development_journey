def cd(num1,num2):
    num = 1
    gcd = 1
    while (num <= num1 and num <= num2 ):
        if (num1 % num == 0 and num2 % num ==0):
            gcd = num
            print(gcd)
        num = num +1    
cd(12,6)