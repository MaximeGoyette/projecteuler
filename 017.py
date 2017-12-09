import inflect
p = inflect.engine()

print len(''.join([p.number_to_words(x) for x in xrange(1, 1001)]).replace('-', '').replace(' ', ''))