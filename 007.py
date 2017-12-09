from sympy import nextprime
n = 2
for x in range(10000):
    n = nextprime(n)
print n