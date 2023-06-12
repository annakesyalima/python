num = c = s = maior = menor = 0

while True:
    num = int(input('Digite um valor [999 para parar]: '))
    if num == 999:
        break
    if c == 0:
        maior = num
        menor = num
    else:
        if num > maior:
            maior = num
        if num < menor:
            menor = num
    s += num
    c += 1


print(f'Você digitou {c} números e a soma deles é {s}')
print(f'O maior número foi {maior} e o menor foi {menor}')