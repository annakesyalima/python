import random
import time

print('Vou pensar em um número entre 0 e 5')
n = int(input('Tente advinhar: '))
print('-=-' * 20)
print('PROCESSANDO...')
time.sleep(3)

list = [0, 1, 2, 3, 4, 5]
think = random.choice(list)

if n == think:
    print('VOCÊ VENCEU!')
else:
    print('Não foi dessa vez! Meu número foi {}'.format(think))

if n > 5:
    print('VOCÊ ESTÁ JOGANDO ERRADO!')
if n < 0:
    print('VOCÊ ESTÁ JOGANDO ERRADO!')

