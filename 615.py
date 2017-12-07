from sympy.ntheory import factorint

n = 0
i = 1
v = {}
while True:
    f = factorint(i)
    fs = sum([f[x] for x in f])
    if fs not in v:
        v[fs] = 0
    v[fs] += 1
    if any([v[x]>=1000000 for x in v]):
        print f
        print fs
        df = 1000000 - fs
        print ((2**df)*reduce(lambda a, b: a*b, [x**f[x] for x in f]))%123454321
        break
    i += 1