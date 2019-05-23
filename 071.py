from fractions import Fraction

d = 1000000

target = 3.0/7
diff = 1
answer = None

for i in xrange(d - 1, 0, -1):
    val = int(target*i)/float(i)
    c_diff = target - val
    if c_diff != 0 and c_diff < diff:
        diff = c_diff
        answer = Fraction(int(target*i), i).numerator

print answer