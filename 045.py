from sympy import *

memo = {
    3: {},
    5: {},
    6: {}
}

triangles = set()
pentagonals = set()
hexagonals = set()

def triangle(n):
    if not n in memo[3]:
        memo[3][n] = n*(n+1)//2
        triangles.add(memo[3][n])
    return memo[3][n]

def pentagonal(n):
    if not n in memo[5]:
        memo[5][n] = n*(3*n-1)//2
        pentagonals.add(memo[5][n])
    return memo[5][n]

def hexagonal(n):
    if not n in memo[6]:
        memo[6][n] = n*(2*n-1)
        hexagonals.add(memo[6][n])
    return memo[6][n]

n = 1

while True:
    if triangle(n) in pentagonals and triangle(n) in hexagonals:
        print triangle(n)

    if pentagonal(n) in triangles and pentagonal(n) in hexagonals:
        print pentagonal(n)

    if hexagonal(n) in triangles and hexagonal(n) in pentagonals:
        print hexagonal(n)

    n += 1