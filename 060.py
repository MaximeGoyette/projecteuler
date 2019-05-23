from gmpy2 import next_prime, is_prime
from itertools import combinations

a = b = c = d = e = 2

memo_next_prime = {}
def optimized_next_prime(n):
    if not n in memo_next_prime:
        memo_next_prime[n] = next_prime(n)
    return memo_next_prime[n]

def validate(*inputs):
    for com in combinations(inputs, 2):
        if not is_prime(int(''.join(map(str, com)))) or not is_prime(int(''.join(map(str, com[::-1])))):
            return False
    return True

while True:

    print a

    if validate(a, b, c, d, e):
        print a, b, c, d, e
        print a + b + c + d + e
        exit(0)

    b = 2
    while b < a:
        if validate(a, b, c, d, e):
            print a, b, c, d, e
            print a + b + c + d + e
            exit(0)

        b = optimized_next_prime(b)

        c = 2
        while c < b:
            if validate(a, b, c, d, e):
                print a, b, c, d, e
                print a + b + c + d + e
                exit(0)

            c = optimized_next_prime(c)

            d = 2
            while d < c:
                if validate(a, b, c, d, e):
                    print a, b, c, d, e
                    print a + b + c + d + e
                    exit(0)

                d = optimized_next_prime(d)

                e = 2
                while e < d:
                    if validate(a, b, c, d, e):
                        print a, b, c, d, e
                        print a + b + c + d + e
                        exit(0)
                    e = optimized_next_prime(e)


    a = optimized_next_prime(a)