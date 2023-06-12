def soma(a=0, b=0):
    s = a + b
    return s

def ParouImpar(n):
    if n % 2 == 0:
        return f'{n} é PAR'
    else:
        return f'{n} é IMPAR'

def fac(n):
    f = 1
    for c in range(n, 0, -1):
        f = f * c
    return f'O fatorial de {n} é {f}'

print(soma(10, 19))
print(ParouImpar(3))
x = int(input('Digite um número: '))
print(fac(x))