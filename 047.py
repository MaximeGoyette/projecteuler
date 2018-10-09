from sympy import factorint

n = 0
streak = []

while True:
    n += 1
    unique_f = list(factorint(n))

    if len(unique_f) == 4:
        streak.append(n)
        if len(streak) >= 4:
            print('The answer is: {}'.format(streak[0]))
            exit(0)

    else:
        streak = []
