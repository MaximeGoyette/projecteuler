from gmpy2 import next_prime
from itertools import cycle
from progressbar import progressbar
from time import time

t0 = time()

p = set()

n = 2

while n < 1000000:
    p.add(n)
    n = next_prime(n)

digits_rot = lambda n: [int(str(n)[-i:] + str(n)[:-i]) for i in range(len(str(n)))]

p = [x for x in p if all([y in p for y in digits_rot(x)])]

t = time() - t0

print(len(p))
print('Solved in {} seconds'.format(t))