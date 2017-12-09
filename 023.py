from sympy.ntheory import divisors
from itertools import combinations_with_replacement

def is_abundant(n):
    return sum(divisors(n)[:-1]) > n

a = []
for n in range(28123+1):
    if is_abundant(n):
        a += [n]

t = range(1, 28123+1)
a = [sum(x) for x in combinations_with_replacement(a, 2)]
    

print sum(set(t) - set(a))
