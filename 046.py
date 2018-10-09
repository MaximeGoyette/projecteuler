from gmpy2 import is_prime, next_prime

def next_odd_composite(n):
    n += 1
    while n%2==0 or is_prime(n):
        n += 1
    return n


def is_valid(n):
    p = 0

    while True:
        p = next_prime(p)
        d = n - p

        if d < 2:
            return False

        r = (float(d)/2)**0.5

        if r == int(r):
            return True

    return False


if __name__ == '__main__':
    n = 4
    while True:
        n = next_odd_composite(n)
        if not is_valid(n):
            print('The answer is: {}'.format(n))
            exit(0)