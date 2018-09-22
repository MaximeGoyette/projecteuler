is_palindromic = lambda n: str(n) == str(n)[::-1]

print(sum([n for n in range(1000000) if is_palindromic(n) and is_palindromic(bin(n)[2:])]))