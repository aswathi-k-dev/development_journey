arr = [2,4,5,6,8]
target = 9
for num1 in arr:
    for num2 in arr:
        total = num1 + num2
        if target == total and num1 != num2:
            print(num1,num2)
            break

# anotherway

arr = [2,4,5,6,8]
target = 9

for n in arr:
    difference = target - n
    if difference in arr and difference != n:
        print(n,difference)
        break
