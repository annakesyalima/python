s = 0
ct = 0
for c in range(1, 7):
    n = int(input('Digite um número: '))
    if n % 2 == 0:
        s = s + n
        ct = ct + 1
print('Você digitou {} número pares e a soma deles é {}'.format(ct, s))



