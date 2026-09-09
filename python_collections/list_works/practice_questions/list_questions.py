num = [1,4,6,9,12,25,24]

# divisible by 3

result = [n for n in num if n % 3]
print(result)

# no of elements in a list
 
print(len(num))

# largest element 

print(max(num))

# smallest element

print(min(num))

# sum of all elements

print(sum(num))

# average 
 
average = sum(num)/len(num)
print(average)

# even nos

result = [n for n in num if n % 2 ==0]
print(result)

# odd nos

result = [n for n in num if n % 2 !=0]
print(result)

# greater than 50

result = [n for n in num if n > 50]
print(result)

# less than 20

result = [n for n in num if n < 20]
print(result)

# prime nos

prime = []
for n in num:
    for i in range(2,n):
        if n % i == 0:
            break
    else:
        prime.append(n)
print(prime)

# negative nos

result = [n for n in num if n < 0]
print(result)







 
