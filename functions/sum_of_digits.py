def sum_of_digits(number):
    sum = 0
    while (number != 0):
        digit = number % 10
        sum = sum + digit
        number = number // 10
    print(sum)

sum_of_digits(1234)
sum_of_digits(3214)
sum_of_digits(3456)


