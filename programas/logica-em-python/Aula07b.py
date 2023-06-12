from datetime import date
"""print('-' * 30)
print('DEPARTAMENTO DE TRANSITO'.center(30))
print('-' * 30)
nasc = int(input('ANO DO NASCIMENTO (YYYY): '))
idade = date.today().year - nasc
print('STATUS'.center(30))
print(f'IDADE:      {idade} anos')
if idade >= 18:
    print('APTO A TIRAR A CARTEIRA')
else:
    print('AINDA NÃO PODE TIRAR A CARTEIRA')"""

n1 = float(input('Primeira Nota: '))
n2 = float(input('Segunda Nota: '))
media = (n1 + n2) / 2
print(f'A sua média foi: {media}')
if media >= 7:
    print('Aluno aprovado!')
else:
    print('\033[31mAluno REPROVADO!')