from random import randint
jogador = 'P'
c = 1
print(f'-=' * 10)
print('JOGO PAR OU IMPAR')
print('-=' * 10)

computador = randint(0, 10)

while True:
    num = int(input('Diga um valor: '))
    jogador = str(input('Par ou Ímpar? [P/I]')).upper().strip()[0]
    if computador % 2 == 0 and num % 2 == 0 and jogador in 'Ii':
        break
    if computador % 2 == 0 and num % 2 == 1 and jogador in 'Pp':
        break
    if computador % 2 == 1 and num % 2 == 0 and jogador in 'Pp':
        break
    if computador % 2 == 1 and num % 2 == 1 and jogador in 'Ii':
        break
    print(f'Você jogou {num} e o computador jogou {computador}.')
    if computador % 2 == 0 and num % 2 == 0 and jogador in 'Pp':
        print('Você VENCEU!')
        print('Vamos jogar novamente...')
    elif computador % 2 == 0 and num % 2 == 1 and jogador in 'Ii':
        print('Você VENCEU!')
        print('Vamos jogar novamente...')
    elif computador % 2 == 1 and num % 2 == 0 and jogador in 'Ii':
        print('Você VENCEU!')
        print('Vamos jogar novamente...')
    elif computador % 2 == 1 and num % 2 == 1 and jogador in 'Pp':
        print('Você VENCEU!')
        print('Vamos jogar novamente...')
    print(f'Você jogou {num} e o computador jogou {computador}.')
    c = c + 1



print('Você PERDEU!')
print(f'GAME OVER! Você venceu {c} vezes.')