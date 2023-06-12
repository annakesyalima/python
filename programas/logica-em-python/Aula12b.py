def soma(a=0, b=0):
    a = int(input('Escreve o primeiro valor: '))
    b = int(input('Escreva o segundo valor: '))
    print(f'A soma de {a} e {b} é igual à {a+b}')


soma()

def ParouImpar(v=0):
    if v % 2 == 0:
        print(f'O número {v} é PAR')
    elif v % 2 == 1:
        print(f'O número {v} é IMPAR')


n = int(input('Digite um número: '))
ParouImpar(n)