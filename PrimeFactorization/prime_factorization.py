# Decomposes a positive integer into its prime factors
def factorize(num):
    assert num > 0, 'number should be positive'
    res = []
    divisor = 2
    while num != 1:
        while num % divisor == 0:
            res.append(divisor)
            num //= divisor
        divisor += 1
    return res

num = int(input('Enter a positive integer: '))
factors = factorize(num)
print(f'The prime factors of {num} is: ', end='')
for factor in factors[:-1]:
    print(f'{factor} * ', end='')
print(f'{factors[-1]}')
