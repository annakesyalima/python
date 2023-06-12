list = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
s = maior = s3 = 0
pares = []
for l in range(0, 3):
    for c in range(0, 3):
        list[l][c] = int(input(f'Digite um valor para [{l}, {c}]: '))
        if list[l][c] % 2 == 0:
            s = s + list[l][c]
            pares.append(list[l][c])
print('-=' * 40)
for l in range(0, 3):
    for c in range(0, 3):
        print(f'[{list[l][c]:^7}]', end='')
    print()
print('-=' * 40)
print(f'Os números pares são: {pares}')
print(f'A soma dos valores pares é {s}.')
for l in range(0, 3):
    s3 = s3 + list[l][2]
print(f'A soma dos valores da 3ª coluna é {s3}.')
for c in range(0, 3):
    if c == 0:
        maior = list[1][c]
    elif list[1][c] > maior:
        maior = list[1][c]
print(f'O maior valor da 2ª linha é {maior}.')