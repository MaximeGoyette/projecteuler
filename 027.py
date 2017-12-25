from sympy.ntheory import isprime

numbahs = [1] + [x for x in xrange(1001) if isprime(x)]

series = []

for a in map(lambda x: -x, numbahs) + numbahs:
    for b in numbahs:
        n = 0
        while isprime(n**2 + a*n + b):
            n += 1
        series += [((a, b), n)]

best = sorted(series, key=lambda x: x[1], reverse=True)[0]

print reduce(lambda x, y: x*y, best[0])