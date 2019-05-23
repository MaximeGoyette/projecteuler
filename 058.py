from gmpy2 import is_prime

p = 1
a = 0
b = 1
i = 2
while True:
    for _ in xrange(4):
        p = p + i
        a += int(is_prime(p))
        b += 1
    if float(a)/b < 0.1:
        break
    i += 2

print i + 1