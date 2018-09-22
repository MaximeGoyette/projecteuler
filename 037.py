from gmpy2 import next_prime, is_prime

n = next_prime(7)

truncate = lambda n, right: [int(str(n)[0 if right else i:len(str(n)) - (i if right else 0)]) for i in range(len(str(n)))]

answers = []

while True:
    if all([is_prime(x) for x in truncate(n, True)]) and all([is_prime(x) for x in truncate(n, False)]):
        answers.append(n)
        print(len(answers), sum(answers))
    
    n = next_prime(n)
