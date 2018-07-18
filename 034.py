from math import factorial

def is_factorial_number(n):
    return n == sum([factorial(int(x)) for x in str(n)])

total = 0
i = 3

while True:
    if is_factorial_number(i):
        total += i
        print total
    i += 1