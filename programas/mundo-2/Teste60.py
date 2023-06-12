num = int(input('Digite um número para \ncalcular o seu Fatorial: '))
c = num
r = 1
print('Calculando {}! '.format(num))
while c > 0:
    print('{} '.format(c), end='')
    print('x ' if c > 1 else '=', end='')
    r = r * c
    c = c - 1


print(' {}'.format(r))


f = 1
for v in range(1, num+1):
    f = f * v
print('\n {}! é igual a {}'.format(num, f))