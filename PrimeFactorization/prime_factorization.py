import sys

# Decomposes a positive integer into its prime factors
def factorize(num):
    assert num > 1, 'number should be greater than 1'
    res = []
    divisor = 2
    while num != 1:
        while num % divisor == 0:
            res.append(divisor)
            num //= divisor
        divisor += 1
    return res


if len(sys.argv) == 1:
    nums = [int(input('Enter a positive integer: '))]
else:
    nums = []
    for i in range(1, len(sys.argv)):
        nums.append(int(sys.argv[i]))

for num in nums:
    factors = factorize(num)
    print(f'The prime factors of {num} is: ', end='')
    for factor in factors[:-1]:
        print(f'{factor} * ', end='')
    print(f'{factors[-1]}')
