n = 1

def valid(n):
    return set(str(n)) == set(str(2*n)) == set(str(3*n)) == set(str(4*n)) == set(str(5*n)) == set(str(6*n))

while not valid(n):
    n += 1

print n