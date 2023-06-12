list = []
tot = 0
for c in range(0, 7):
    list.append(int(input('Digite um valor: ')))
print('Os números pares na lista são: ', end='')
for c in list:
    if c % 2 == 0:
        tot = tot + 1
        print(c, end=' ')
print(f'\nO total de partes são {tot}')