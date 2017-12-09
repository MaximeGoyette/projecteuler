from itertools import permutations

print ''.join([str(x) for x in list(permutations(range(10)))[999999]])