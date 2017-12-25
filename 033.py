v = []

for x in range(10, 100):
    for y in range(10, 100):
        a = filter(lambda a: not a in str(y), str(x))
        b = filter(lambda a: not a in str(x), str(y))
        a = a if ''.join(a) != '' else ['0']
        b = b if ''.join(b) != '' else ['0']
        try:
            if float(''.join(a)) / float(''.join(b)) == float(x)/y and int(''.join(a)) != x and int(''.join(b)) != y and str(x)[-1] != '0' and str(y)[-1] != '0' and (y, x) not in v:
                v.append((x, y))
        except:
            pass

from fractions import Fraction

print Fraction(reduce(lambda x, y: x*y, [x[0] for x in v]), reduce(lambda x, y: x*y, [x[1] for x in v]))