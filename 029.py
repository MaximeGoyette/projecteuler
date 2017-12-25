serie = []

for a in xrange(2, 101):
    for b in xrange(2, 101):
        serie += [a**b]

print len(set(serie))