from sympy.ntheory import factorint

n = 0
i = 10000000000000000000000000000000000000000000000000000000000000000000000000000000
while True:
    f = factorint(i)
    fs = sum([f[x] for x in f])
    print fs
    if fs >= 1000000:
        n += 1
        print n
    if n >= 1000000:
        print i%123454321
        break
    i += 1