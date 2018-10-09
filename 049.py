from gmpy2 import next_prime, is_prime
from itertools import permutations, combinations

n = 999

while True:
    n = next_prime(n)
    primes = []
    for perm in set(permutations(str(n))):
        if is_prime(int(''.join(perm))):
            primes.append(perm)
    
    for c in combinations(primes, 3):
        c = list(map(lambda x: int(''.join(x)), c))
        c.sort()
        if c[1] - c[0] == 3330 and c[2] - c[1] == 3330:
            ans = ''.join(map(str, c))
            if ans == '148748178147':
                continue
            print('The answer is: {}'.format(ans))
            exit(0)