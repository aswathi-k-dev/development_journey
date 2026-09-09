def is_amstrong_number(number):
    original_number = number
    count = len(str(number))
    total = 0
    while (number != 0):
        digit = number % 10
        exponent = digit ** count
        total = total + exponent
        number = number // 10
    if total == original_number:
        print("armstrong number")
    else:
        print("not an armstrong number")
is_amstrong_number(123)
is_amstrong_number(153)
    