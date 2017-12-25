a = 1001

total = 1

for x in xrange(1, a//2 + 1):
    d1 = (2*x + 1)**2
    d2 = d1 - 2*x
    d3 = d2 - 2*x
    d4 = d3 - 2*x
    total += d1 + d2 + d3 + d4

print total