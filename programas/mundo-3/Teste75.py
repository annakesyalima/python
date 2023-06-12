tupla = (int(input('Digite o 1º número: ')),
        int(input('Digite o 2º número: ')),
        int(input('Digite o 3º número: ')),
        int(input('Digite o 4º número: ')))

print(f'Os valores digitados são: {tupla}')
print(f'O valor 9 apareceu {tupla.count(9)} vezes')
if 3 in tupla:
        print(f'O valor 3 apareceu na {tupla.index(3) + 1}ª posição')
else:
        print('O valor 3 não apareceu')
print('Os valores pares foram ',end='')
for n in tupla:
        if n % 2 == 0:
                print(n, end=' ')