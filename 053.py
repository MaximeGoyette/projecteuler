from math import factorial

nCr = lambda n, r: factorial(n)/(factorial(r)*factorial(n - r))

total = 0

for n in xrange(1, 101):
    for r in xrange(1, n + 1):
        if nCr(n, r) > 1000000:
            total += 1

print total