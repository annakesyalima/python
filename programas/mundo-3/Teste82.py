list = []
par = []
impar = []
while True:
    list.append(int(input('Digite um valor: ')))
    r = str(input('Deseja continuar? [S/N]: '))
    if r in 'Nn':
        break
for i, v in enumerate(list):
    if v % 2 == 0:
        par.append(v)
    elif v % 2 == 1:
        impar.append(v)
print(f'A lista completa é {list}')
print(f'Os números pares são {par}')
print(f'Os números impares são {impar}')