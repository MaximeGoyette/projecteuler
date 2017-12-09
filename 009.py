from sympy.solvers import solve
from sympy import Symbol
b = Symbol('b')
for a in range(1, 999):
    e = solve(a**2 + b**2 - (1000-a-b)**2, b)[0]
    if e.is_integer:
        print reduce(lambda x, y: x*y, [a, e, (1000-a-e)])
        break