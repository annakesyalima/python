list = []
for c in range(0, 5):
    n = int(input('Digite um valor: '))
    if c == 0 or n > list[-1]:
        list.append(n)
        print('Número adicionado no final da lista')
    else:
        pos = 0
        while pos < len(list):
            if n <= list[pos]:
                list.insert(pos, n)
                print(f'Número adicionado na posição {pos}')
                break
            pos += 1



print('-=' * 30)
print(f'Os valores digitados em ordem foram: {list}')

