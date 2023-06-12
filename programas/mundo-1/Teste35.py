import time
print('ANALISADOR DE TRIÂNGULO')

r1 = float(input('Digite o primeiro comprimento: '))
r2 = float(input('Digite o segundo comprimento: '))
r3 = float(input('Digite o terceiro comprimento: '))

print('PROCESSANDO...')
time.sleep(3)

if r1 + r2 > r3 and r1 + r3 > r2 and r2 + r3 > r1:
    print('\033[33mOs três segmentos de reta FORMAM UM TRIÂNGULO\033[m')
else:
    print('\033[31mOs três segmentos de reta NÃO FORMAM UM TRIÂNGULO\033[m')
