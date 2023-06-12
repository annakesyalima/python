print('SEQUENCIA DE FIBONACCI')
n1 = 0
n2 = 1
print(n1, n2, end=' ')
for c in range(1, 14):
    n3 = n1 + n2
    print(n3, end=' ')
    n1 = n2
    n2 = n3
print('FIM')
print('-=' * 30)
print('ANALISADOR DE VALORES')
s = div5 = n = somapar = 0
for c in range(1, 6):
    valor = int(input(f'Digite o {c}º valor: '))
    s = s + valor
    if valor % 2 == 0:
        somapar = somapar + valor
    if valor % 5 == 0:
        div5 = div5 + 1
    if valor == 0:
        n = n + 1
media = s / c
print(f'A soma entre os valores é {s}')
print(f'A média entre os valores é {media}')
print(f'Ao todo, existem {div5} valores divisivéis por 5')
print(f'Valores nulos: {n}')
print(f'A soma dos valores pares é {somapar}')

