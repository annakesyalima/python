list = [ ]

maior = menor = 0
for c in range(0, 5):
    list.append(int(input(f'Digite o número na posoção {c}: ')))
    if c == 0:
        maior = menor = list[c]
    else:
        if list[c] > maior:
            maior = list[c]
        if list[c] < menor:
            menor = list[c]
print(f'Você digitou os valores {list}')

print(f'O maior número foi o {maior} e ele está na posições ', end=' ')
for i, v in enumerate(list):
    if v == maior:
        print(f'{i}...', end='')
print(f'\nO menor número foi o {menor} e ele está nas posições ', end=' ')
for i, v in enumerate(list):
    if v == menor:
        print(f'{i}...', end='')
print()

# solução minha que quase funcionou
"""maior = menor = f = l = 0

for p, c in enumerate(list):
    if p == 0:
        maior = c
        menor = c
    else:
        if c > maior:
            maior = c

        if c < menor:
            menor = c
            if c == maior:
                f = p
            if c == menor:
                l = p"""