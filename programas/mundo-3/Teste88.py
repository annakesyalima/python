from time import sleep
import random
list = []
jogo = []
print('-=' * 40)
print('        JOGO DA MEGA SENA       ')
print('-=' * 40)
n = int(input('Quandos jogos você quer que eu sorteie?: '))
t = 1
while t <= n:
    c = 0
    while True:
        num = random.randint(1, 60)
        if num not in list:
            list.append(num)
            c = c + 1
        if c >= 6:
            break
    list.sort()
    jogo.append(list[:])
    list.clear()
    t = t + 1
print('-=' * 3, f'SORTEANDO {n} JOGOS', '-=' * 3)
for i, l in enumerate(jogo):
    print(f'O jogo {i+1}: {l}')
    sleep(0.5)
print('-=' * 3,  '  BOA SORTE  '  , '-=' * 3)
