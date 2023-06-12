tabela = 'América-MG', 'Athletico-PR', 'Atlético-MG', 'Bahia', 'Botafogo', 'Bragantino', 'Corinthians','Coritiba', 'Cruzeiro', 'Cuiabá', 'Flamengo', 'Fluminense','Fortaleza', 'Goiás', 'Grêmio', 'Internacional', 'Palmeiras', 'Santos', 'São Paulo', 'Vasco'

print(f'Os 5 primeiros são {tabela [0:5]}')
print('-=' * 50)
print(f'Os 4 últimos são {tabela[-4:]}')
print('-=' * 50)
print(f' Os times em ordem alfabética são {sorted(tabela)}')
print('-=' * 50)
print(f'Fortaleza está no {tabela.index("Fortaleza")+1}º lugar')