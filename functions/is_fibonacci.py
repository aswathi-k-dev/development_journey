def is_fibonacci(num):
    first = 0
    second = 1
    next = 1
    while(next <= num):
        next = first + second
        if next == num:
            print("true")
            break

        first = second
        second = next
    else:
        print("false")

is_fibonacci(24)
is_fibonacci(8)
is_fibonacci(13)