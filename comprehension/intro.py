arr = [2,3,4,5,6,7]
squares = [num **2  for num in arr]
print(squares)

cube = [num **3   for num in arr]
print(cube)

add_five = [num + 5  for num in arr]
print(add_five)

evens = [num  for num in arr if num % 2 == 0]
print(evens)

odds = [num for num in arr if num % 2 != 0]
print(odds)

num_gt_5 = [num for num in arr if num > 5]
print(num_gt_5)