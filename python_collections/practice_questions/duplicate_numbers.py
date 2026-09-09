arr = [10,1,15,16,11,10,12,11]
duplicates = set()
for num in arr:
    if arr.count(num) > 1 :
        duplicates.add(num)
print(duplicates)


