dados = {}
dados['nome'] = str(input('Nome do Jogador: '))
num = int(input(f'Quantas partidas {dados["nome"]} jogou?: '))
partidas = []
dados['gols'] = partidas
for c in range(0, num):
    partidas.append(int(input(f'Quantos gols na partida {c+1}: ')))
dados['total'] = sum(partidas)

print('-=' * 30)
print(dados)
print('-=' * 30)
for k, i in dados.items():
    print(f'O campo {k} tem o valor {i}')
print('-=' * 30)
print(f'O jogador {dados["nome"]} jogou {num} partidas.')
for p, g in enumerate(partidas):
    print(f"  => Na partida {p+1}, fez {g} gols.")
print(f'Foi um total de {dados["total"]} gols.')
print(f"O maior número de gols foi {max(partidas)} e o menor foi {min(partidas)}")