c = total = maior = menor = 0
escolha = 'S'
while escolha in 'Ss':
    num = int(input('Digite um número: '))
    escolha = str(input('Quer continuar? [S/N] ')).upper().strip()[0]
    c += 1
    total += num
    if c == 1:
        maior = num
        menor = num
    else:
        if num > maior:
            maior = num
        if num < menor:
            menor = num
print('Você digitou {} números e a média foi {:.2f}'.format(c, (total / c)))
print('O maior valor foi {} e o menor foi {}'.format(maior, menor))

