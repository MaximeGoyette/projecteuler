v = []
for n in xrange(1000000):
    i = 1
    while n > 1:
        i += 1
        if n%2==0:
            n /= 2
        else:
            n = 3*n + 1
    v += [i]
print v.index(max(v))
