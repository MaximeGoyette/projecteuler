print max([[x*y for y in xrange(100, 1000) if str(x*y)==str(x*y)[::-1]] for x in xrange(100, 1000)])