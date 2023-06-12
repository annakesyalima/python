n = int(input('Digite um número qualquer : '))
r = n % 2

if r == 0:
    print('\033[1;33m Esse número é PAR!\033[n')
else:
    print('\033[1;34m Esse número é IMPAR!\033[m')