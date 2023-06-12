list = []
while True:
    n = int(input('Digite um valor para a lista: '))
    list.append(n)
    r = str(input('Deseja continuar? [S/N]: '))
    if r in 'Nn':
        break
print('-=' * 30)
print(f'A lista contém {len(list)} elementos')
list.sort(reverse=True)
print(f'A lista digitada em ordem decrescente é {list}')
if 5 in list:
    print('O número 5 está na lista')
else:
    print('O número 5 não está na lista')
