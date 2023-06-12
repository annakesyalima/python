n1 = int(input('Primeiro valor: '))
n2 = int(input('Segundo valor: '))
n3 = int(input('Terceiro valor: '))

list = [n1, n2, n3]
M = max(list)
m = min(list)

print('\033[1;32mO maior número é {}\033[m e o \033[1;31mmenor número é {}'.format(M,m))
