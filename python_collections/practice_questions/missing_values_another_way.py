arr =[1,2,4,5,6]
arr.sort()
for p in range(0,len(arr)-1):
    c = p + 1
    difference = arr[c] - arr[p]
    if difference != 1:
        print(arr[p]+1,"is missing")
        break

