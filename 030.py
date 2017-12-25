n = 2 

total = 0

while True:
    if n == sum(map(lambda x: int(x)**5, str(n))):
        total += n
    n += 1
    print total