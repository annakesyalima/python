list = []
toda = []
m = 0
while True:
    list.append(str(input('Nome: ')))
    list.append(float(input('Nota 1: ')))
    list.append(float(input('Nota 2: ')))
    toda.append(list[:])
    list.clear()
    r = str(input('Quer continuar? [S/N] '))
    if r in 'Nn':
        break
print('-=' * 30)
print(f'{"No.":<4}{"NOME":<10}{"MÉDIA":>8}')
for i, d in enumerate(toda):
    print(f'{i:<4}{d[0]:<10}{(d[1] + d[2]) / 2:>8.1f}')
print('-=' * 30)
while True:
    opt = int(input('Mostrar notas de qual aluno? (999 interrompe):'))
    if opt == 999:
        print('FINALIZANDO...')
        break
    if opt <= len(toda) - 1:
        print(f'Nota de {toda[opt][0]} são {toda[opt][1]} e {toda[opt][2]}')
        print('-' * 30)
print('<<< VOLTE SEMPRE >>>')
