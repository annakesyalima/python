import time


n1 = int(input('Primeiro número: '))
n2 = int(input('Segundo número: '))

print('\033[1;31mPROCESSANDO...')
time.sleep(2)

if n1 > n2:
    print('\033[1;32mO PRIMEIRO valor é maior')
elif n2 > n1:
    print('\033[1;33mO SEGUNDO valor é maior')
elif n1 == n2:
    print('\033[1;34mO dois valores são IGUAIS!')