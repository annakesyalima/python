"""from math import sqrt, ceil
import random
import emoji

n = random.randint(1, 10)
r = sqrt(n)
k = ['fall', 'summer', 'winter', 'spring']
c = random.choice(k)
print('A raiz de {} é igual a {:.1f}'.format(n, ceil(r)))
print(c)
print(emoji.emojize(':sun::yellow_heart::sparkles::fire::dog:'))
"""
"""n1 = 5 % 2
print(n1)
print(pow(4, 3))
print('=' * 50)"""


'''nome = str(input('Qual é o seu nome: '))
print('Prazer {:^30}!'.format(nome))
print('Prazer {:>30}!'.format(nome))
print('Prazer {:<30}!'.format(nome))
print('Prazer{:|^30}'.format(nome))'''

"""n1 = int(input('Primeiro: '))
n2 = int(input('Segundo: '))
print(n1 + n2)
print(n1 - n2)
print(n1 * n2)
print(n1 / n2)
print(n1 ** n2)
print(n1 // n2)
print(n1 % n2)"""

total = 0
from time import sleep
for c in range(0, 3):
    if c % 2 == 0:
        total = total + c
print(total)
sleep(1)
print('BUMMMM')
