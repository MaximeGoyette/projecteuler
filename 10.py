from sympy import nextprime
n = 2
a = []
while n < 2000000:
    a += [n]
    n = nextprime(n)
print sum(a)