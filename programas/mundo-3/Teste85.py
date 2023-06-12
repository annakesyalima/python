total = [[], []]
n = 0
for v in range(0, 7):
    n = int(input(f'Digite o {v+1}º valor: '))
    if n % 2 == 0:
        total[0].append(n)
    elif n % 2 == 1:
        total[1].append(n)
print('-=' * 30)
total[0].sort()
print(f'Os valores pares digitados foram: {total[0]}')
total[1].sort()
print(f'Os valores ímpares digitados foram: {total[1]}')


