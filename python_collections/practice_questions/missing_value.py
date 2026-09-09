arr = [1,2,3,4,6]
max_num = max(arr)
total = 0
for num in range(1,max_num + 1):
    total+=num
curr_arr_sum = sum(arr)
difference = total - curr_arr_sum
print(difference)

