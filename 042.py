from sympy import Symbol, Eq
from sympy.solvers import solve

a = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

sample = 'SKY'

s = lambda w: sum([a.index(l) + 1 for l in w])

def solve(w):
    x = Symbol('x')
    print(solve([Eq(x, 3), ]))
    

print(solve(sample))