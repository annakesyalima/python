time = []
jogador = {}
gols = []
while True:
    gols.clear()
    jogador.clear()
    jogador['nome'] = str(input('Nome do jogador: '))
    n = int(input(f'Quantas partidas {jogador["nome"]} jogou? '))
    for c in range(0, n):
        gols.append(int(input(f'Quantos gols na partida {c+1}? ')))
    jogador['gols'] = gols[:]
    jogador['total'] = sum(gols)
    time.append(jogador.copy())
    r = str(input(f'Quer continuar? [S/N] ')).upper()[0]
    if r == 'N':
        break
print('-=' * 30)
print('cod', end=' ')
for i in jogador.keys():
    print(f'{i:<15}', end='')
print()
for j, g in enumerate(time):
    print(f'{j:>3}', end=' ')
    for d in g.values():
        print(f'{str(d):<15}', end='')
    print()
print('-=' * 30)
while True:
    m = int(input('Mostrar dados de qual jogador? [999 para parar] '))
    if m == 999:
        break
    if m >= len(time):
        print(f'ERRO! Não existe jogador com o código {m}')
    else:
        print(f'   - - LEVANTAMENTO DO JOGADOR {time[m]["nome"]}: ')
        for i, x in enumerate(time[m]['gols']):
            print(f'    No jogo {i+1} fez {x} gols.')
    print('-=' * 40)
print('<< VOLTE SEMPRE!  >>')
