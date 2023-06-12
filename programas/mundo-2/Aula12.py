import time
import emoji
import random

list = ['sushi', 'hamburguer', 'pão', 'picanha']
c = random.choice(list)
print('Quero comer {}'.format(c))
print('Deixa eu ver...')
time.sleep(3)


if c == 'sushi':
    print('Vamos pedir! \U0001f363')
elif c == 'pão' or c == 'picanha':
    print('Pense no chinchin \U0001f4b8')
elif c == 'hamburguer':
    print('\033[1;31mVamos no Hents')
else:
    print('Vamos comer em casa!')

