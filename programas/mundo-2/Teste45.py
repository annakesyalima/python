import random
import time
print('''Suas opções:
[ 0 ] PEDRA
[ 1 ] PAPEL
[ 2 ] TESOURA''')

e = int(input('Qual é a sua jogada? '))
list = ['PEDRA', 'PAPEL', 'TESOURA']
c = random.choice(list)

print('JO')
time.sleep(1)
print('KEN')
time.sleep(1)
print('PO')
time.sleep(1)
print('{:=^60}'.format(''))



if c == 'PEDRA': #PEDRA
    if e == 0:
        print('EMPATE. Jogue novamente!')
    elif e == 1:
        print('VOCê GANHOU!')
    elif e == 2:
        print('VOCÊ PERDEU!')
elif c == 'PAPEL':  #PAPEL
    if e == 0:
        print('VOCÊ PERDEU!')
    elif e == 1:
        print('EMPATE. Jogue novamente!')
    elif e == 2:
        print('VOCÊ GANHOU!')
elif c == 'TESOURA':  #TESOURA
    if e == 0:
        print('VOCÊ GANHOU!')
    elif e == 1:
        print('VOCÊ PERDEU!')
    elif e == 2:
        print('EMPATE. Jogue novamente!')



print('{:=^60}'.format(''))
print('O computador jogou {}'.format(c))
if e == 0:
    e = 'PEDRA'
elif e == 1:
    e = 'PAPEL'
else:
    e = 'TESOURA'
print('O jogador jogou {}'.format(e))
print('{:=^60}'.format(''))


