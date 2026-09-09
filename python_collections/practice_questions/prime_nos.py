arr = [3,7,4,9,10,11,12,13]
prime_numbers = []
for num in arr:
    for i in range(2,num):
        if num % i == 0:
            break
    else:
        prime_numbers.append(num)
print(prime_numbers)