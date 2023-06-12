dados = {'nome': 'Kesya', 'idade': 29, 'sexo': 'F'}
print(dados['nome'])
print(dados.values())
print(dados.keys())
print(dados.items())
dados['peso'] = 58
del dados['sexo']
for k, v in dados.items():
    print(f'O {k} é {v}')

estado = {}
brasil = []
for c in range(0, 3):
    estado['uf'] = str(input('Estado: '))
    estado['sigla'] = str(input('Sigla: '))
    brasil.append(estado.copy())

for e in brasil:
    print(e)