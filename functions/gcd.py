def gcd(num):
    gcd = 1
    for i in range(1,num):
        if num % i == 0:
            gcd = i
    print(gcd)
gcd(6)
