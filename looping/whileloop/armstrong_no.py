num = int(input("enter number :"))
original_num = num
count = len(str(num))
total = 0
while (num != 0):
    digit = num % 10
    exponent = digit ** count
    total = total +exponent
    num = num // 10
if total == original_num:
    print("armstrong number")
else:
    print("not an armstrong number")