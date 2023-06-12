print('-' * 50)
print('{:^50}'.format('LISTAGEM DE PREÇOS'))
print(f'{"LISTAGEM DE PREÇOS":^50}')
print('-' * 50)
tupla = ('Lápis', 2.50, 'Caneta', 3.00, 'Caderno', 11.99, 'Estójio',
        5.80, 'Mochia', 45.00, 'Livro', 30.00, 'Borracha', 0.99)
for n in range(0, len(tupla)):
    if n % 2 == 0:
        print(f'{tupla[n]:.<42}', end='')
    else:
        print(f'R${tupla[n]:>6.2f}')
print('-' * 50)

mercado = ('apples', 12, 'laranja', 5, 'coco', 2.5,
           'mamão', 4.5, 'colve', 2.50, 'coentro', 1.50)

for item in range(0, len(mercado)):
    if item % 2 == 0:
        print(f'{mercado[item]:.<30}', end='')
    else:
        print(f'R${mercado[item]:>7.2f}')
print('-' * 50)