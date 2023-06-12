d = float(input('Qual a distância da sua viagem? '))
c = d * 0.5
l = d * 0.45

if d <= 200:
    print('\033[33mA sua viagem custa R${:.2f}'.format(c))
else:
    print('\033[32mA sua viagem custa R${:.2f}'.format(l))
