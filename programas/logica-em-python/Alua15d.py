list = [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]
s = maior = 0
p = 1

for l in range(0, 4):
    for c in range(0, 4):
        list[l][c] = int(input(f'Digite um valor para [{l}, {c}]: '))
        if l == c:
            s += list[l][c]

for c in range(0, 4):
    p = p * list[1][c]

for l in range(0, 4):
    if l == 0:
        list[l][3] = maior
    else:
        maior = list[l][3]


print('-=' * 40)
for l in range(0, 4):
    for c in range(0, 4):
        print(f'[{list[l][c]:^7}]', end='')
    print()
print('-=' * 40)
print(f'- A soma dos valores da diagonal princial é {s}')
print(f'- O produto da segunda linha é {p}')
print(f'- O maior número da coluna 3 é {maior}')