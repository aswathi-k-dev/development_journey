def is_divisible_by_three(num):
    result = True
    if num % 3 == 0:
        result = True
    else:
        result = False

    return result

assert is_divisible_by_three(9) == True,"testcase 1 failed"
assert is_divisible_by_three(16) == False,"testcase 2 failed"