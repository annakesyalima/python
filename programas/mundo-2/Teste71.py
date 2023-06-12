v = int(input('Quanto você quer sacar? R$'))
t = v
b = 50
c = 0
while True:
    if t >= b:
        t = t - b
        c = c + 1
    else:
        if c > 0:
            print(f'Você sacou {c} cédulas de {b} reais')
        if b == 50:
            b = 20
        elif b == 20:
            b = 5
        elif b == 5:
            b = 1
        c = 0
        if t == 0:
            break