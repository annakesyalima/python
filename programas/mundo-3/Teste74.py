import random

tupla = (random.randint(0, 9), random.randint(0, 9), random.randint(0, 9), random.randint(0, 9), random.randint(0, 9))
print('Os valores soteados foram: ', end='')
for n in tupla:
    print(f'\033[34m{n}\033[m', end=' ')

print(f'\nO maior número da tupla é {max(tupla)} e o menor é {min(tupla)}')