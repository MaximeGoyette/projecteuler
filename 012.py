from sympy.ntheory import divisors

i = 1
while True:
    triangle = sum(range(i+1))
    n = divisors(triangle)
    if len(n) > 500:
        print triangle
        break
    i += 1