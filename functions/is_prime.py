def is_prime(number):
    is_prime = True
    for i in range(2, number):
        if number % i == 0:
            is_prime = False
            break
    else:
        print(is_prime)
is_prime(5)

