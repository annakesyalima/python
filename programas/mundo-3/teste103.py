def validação(j, g):
    if j in ' ':
        j = '<<desconhecido>>'
    if g.isnumeric():
        g = int(g)
    else:
        g = 0
    return f'O jogador {j} fez {g} gols no campeonato.'


#Programa Principal
jogador = str(input('Nome do Jogador: '))
gols = str(input('Número de Gols: '))
print(validação(jogador, gols))


def ficha(jog='<desconhecido>', gol=0):
    print(f'O jogador {jog} fez {gol} gols no campeonato.')

n = str(input('Nome do jogador: '))
go = str(input('Número de gols: '))
if go.isnumeric():
    go = int(go)
else:
    g = 0
if n.strip() == '':
    ficha(gol=go)
else:
    ficha(n, go)