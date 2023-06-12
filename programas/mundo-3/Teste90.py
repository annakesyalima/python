diario = {}
diario['nome'] = str(input('Nome: '))
diario['nota'] = float(input(f'Média do {diario["nome"]}: '))
if diario['nota'] <= 7:
    diario['situação'] = 'Reprovado'
elif diario['nota'] < 7:
    diario['situação'] = 'Recuperação'
else:
    diario['situação'] = 'Aprovação'
print('-=' * 40)
for k, v in diario.items():
    print(f'  - {k} é igual a {v}')
