from time import sleep

soma = maior = menor = 0

"""c = int(input('Até quanto você quer contar? '))
s = int(input('De quanto em quanto você quer contar? '))
for n in range(1, c+1, s):
    print(f"\033[0;32m{n}\033[m", end=' ')
    soma = soma + n
    sleep(0.5)
print(f'\nA soma de todos os números mostrados é \033[0;32m{soma}')"""

for x in range(0, 5):
    n = int(input('Digite um valor: '))
    soma = soma + n
    if x == 0:
        maior = n
        menor = n
    else:
        if n > maior:
            maior = n
        if n < menor:
            menor = n
print(f'A soma de todos os valores digitados é {soma}')
print(f'O maior número foi {maior} e o menor foi {menor}')