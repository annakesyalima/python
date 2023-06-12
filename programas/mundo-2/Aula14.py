n = 1
par = impar = 0

while n != 0:
    n = int(input('Digite um valor: '))
    if n != 0:
        if n % 2 == 0:
            par = par + 1
        else:
            impar = impar + 1


print('Tem \033[31m{}\033[m pares e \033[34m{} impares'.format(par, impar))
print('FIM')


