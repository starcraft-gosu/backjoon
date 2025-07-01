import random
file = 'input.txt'

N, M = 100000, 100000

with open(file, 'w') as f:
    f.write(f'{N}\n')
    for _ in range(N):
        a = random.randint(-2^31, 2^31)
        f.write(f'{a} ')
    f.write(M)
    for _ in range(M):
        b = random.randint(-2^31, 2^31)
        f.write(f'{b} ')
