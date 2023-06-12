list = []
while True:
    n = int(input('Digite um valor: '))
    if n not in list:
        list.append(n)
        print('Número adicionado com sucesso...')
    else:
        print('Valor duplicado, digite novamente...')
    r = str(input('Quer continuar? [S/N] '))
    if r in 'Nn':
        break
print('-=' * 30)
list.sort()
print(f'A sua lista foi {list}')
