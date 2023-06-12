#print('\033[1;33m My name is Bob!\033[m')

v = float(input('Qual é a velocidade atual do carro? '))
m = (v - 80) * 7

if v <= 80:
    print('\033[1;33m Tenha um bom dia! Dirija com segurança!\033[m')
if v >= 81:
    print('\033[1;31m MULTADO! Você excedeu o limite permitido que é de 80Km/k')
    print('\033[1;31m Você deve pagar uma multa de \033[4;32mR${:.2f}'.format(m))