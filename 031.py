n = 0

for a in xrange(2):
    for b in xrange(3 - a*2):
        for c in xrange(5 - b*2):
            for d in xrange(11 - c*2):
                for e in xrange(21):
                    for f in xrange(41 - e*2):
                        for g in xrange(101):
                            for h in xrange(201 - g*2):
                                if sum([a*200, b*100, c*50, d*20, e*10, f*5, g*2, h*1]) == 200:
                                    n += 1
print n
