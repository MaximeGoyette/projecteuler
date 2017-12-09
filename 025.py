a = [1, 1]

while len(str(a[-1])) < 1000:
    a += [a[-2] + a[-1]]

print len(a)