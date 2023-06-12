from random import randint

print('\033[33mSOU SEU COMPUTADOR...')
print('Acabei de pensar em um número entre 0 e 10.')
print('Será que consegue adivinhar qual foi?\033[m')

palpite = 1
num = int(input('Qual é seu palpite? '))
comnum = randint(0, 10)
while num != comnum:
    palpite = palpite + 1
    if num < comnum:
        num = int(input('Mais...Tente mais uma vez: '))
    if num > comnum:
        num = int(input('Menos...Tente mais uma vez: '))



print('Parabéns!!! O computador pensou {} e você também pessou {}!'.format(comnum, num))
print('Você precisou de {} tentativas para acertar'.format(palpite))
