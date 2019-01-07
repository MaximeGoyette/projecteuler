maximum = None

for a in xrange(1, 101):
    for b in xrange(1, 101):
        v = a**b
        ds = sum(map(int, str(v)))
        if maximum == None or ds > maximum:
            maximum = ds

print maximum