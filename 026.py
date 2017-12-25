rc = ['', '']

for i in range(2, 1000):
    v = []
    c = ''
    a = 10
    while a not in v:
        v += [a]
        c += str(a//i)
        a %= i
        a *= 10
    
    rc += [c[v.index(a):]]

rc = map(len, rc)

print rc.index(max(rc))