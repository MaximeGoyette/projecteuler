from gmpy2 import is_prime
from itertools import permutations

current_number = 0

replacements = map(str, range(10))
seen = set()

while True:
    if current_number in seen:
        current_number += 1
        continue


    s = str(current_number)
    for a in xrange(1, len(s)):
        b = len(s) - a
        base_mask = '.'*a + '_'*b

        for mask in set(permutations(base_mask)):
            base_number = ''.join([s[i] if x=='.' else '_' for i, x in enumerate(mask)])

            primes = set()

            for c in replacements:
                candidate_number = int(base_number.replace('_', c))

                seen.add(candidate_number)

                if is_prime(candidate_number):
                    primes.add(candidate_number)

            if len(primes) >= 8 and all(len(str(list(primes)[0])) == len(str(x)) for x in primes):
                print min(primes)
                exit(0)
    
    current_number += 1  