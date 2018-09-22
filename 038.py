c_product = lambda i, n: int(''.join([str(i*x) for x in xrange(1, n+1)]))
is_pandigital = lambda n: sorted(str(n)) == ['1', '2', '3', '4', '5', '6', '7', '8', '9']

i, n, p = 2, 2, 0

maximum = 0

while True:

    n, p = 1, 0

    while p < 999999999:
        p = c_product(i, n)
        if p > maximum and is_pandigital(p):
            maximum = p
            print maximum

        n += 1

    i += 1
