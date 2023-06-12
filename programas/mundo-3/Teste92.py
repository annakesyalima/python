from datetime import date
dados = {}
while True:
    dados['nome'] = str(input('Nome: '))
    nasc = int(input('Ano de Nascimento: '))
    dados['idade'] = date.today().year - nasc
    dados['CTPS'] = int(input('Carteira de Trabalho (0 não tem): '))
    if dados['CTPS'] == 0:
        break
    dados['contratação'] = int(input('Ano de Contratação: '))
    dados['salário'] = float(input('Salário: '))
    dados['aposentadoria'] = dados['idade'] + ((dados['contratação'] + 35) - date.today().year)
    break
print('-=' * 30)
for k, v in dados.items():
    print(f'  - {k} tem o valor {v}')


