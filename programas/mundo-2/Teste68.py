from random import randint
c = 0

while True:
    jogador = int(input('Escolha um número: '))
    computador = randint(0, 10)
    total = jogador + computador
    escolha = ' '
    while escolha not in 'PI':
        escolha = str(input('Par ou Ímpar? [P / I]: ')).strip().upper()[0]
    print(f'Você jogou {jogador} e o computador jogou {computador}. Total de {total}', end=' ')
    print('DEU PAR' if total % 2 == 0 else 'DEU ÍMPAR')
    if escolha == 'P':
        if total % 2 == 0:
            print('VOCÊ VENCEU')
            c += 1
        else:
            print('VOCÊ PERDEU!')
            break
    elif escolha == 'I':
        if total % 2 == 1:
            print('VOCÊ VENCEU!')
            c += 1
        else:
            print('VOCÊ PERDEU!')
            break
    print('Vamos jogar novamente...')
print(f'GAME OVER! Você venceu {c} vezes!')
