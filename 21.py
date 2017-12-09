from sympy.ntheory import divisors
v = []

def d(a):
    return sum(divisors(a)[:-1])

for a in range(10000):
    b = d(a)
    if a == d(b) and a != b:
        v += [a]

print sum(set(v))