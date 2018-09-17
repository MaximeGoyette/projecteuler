from progressbar import progressbar

def find_solutions(p):
    sols = set()
    for a in xrange(1, p):
        for b in xrange(1, p):
            c = p - a - b
            if a**2 + b**2 == c**2:
                sols.add(frozenset([a, b, c]))
    return sols

print sorted([(len(find_solutions(p)), p) for p in progressbar(xrange(1, 1001))])[-1][1]
