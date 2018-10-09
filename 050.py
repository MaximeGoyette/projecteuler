from gmpy2 import next_prime, is_prime

total = 0
n = 0
ans = 0

while total < 100:
    n = next_prime(n)
    total += n

print(total - n)