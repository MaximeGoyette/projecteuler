a = [1, 2]

while a[-1] <= 4000000:
    a += [a[-2] + a[-1]]

print sum([x for x in a if x%2==0])