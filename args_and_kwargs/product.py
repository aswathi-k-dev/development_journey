def product(*args):
    result = 1
    for num in args:
        result = result * num
    return result

print(product(10,12))
print(product(10,12,20))



