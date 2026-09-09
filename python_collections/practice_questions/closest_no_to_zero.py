# closest num to zero

arr = [-3,-2,-1,2,3,4]
closest_to_zero = arr[0]
for num in arr:
    if abs(num) < abs(closest_to_zero):
        closest_to_zero = num
print(closest_to_zero)

