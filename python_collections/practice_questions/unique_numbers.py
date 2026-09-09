arr = [10,1,15,16,11,10,12,11]
unique_numbers = []
for num in arr:
    if arr.count(num) == 1:
        unique_numbers.append(num)
print(unique_numbers)