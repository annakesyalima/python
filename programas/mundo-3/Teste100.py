from random import randint

list = [randint(0, 9), randint(0, 9), randint(0, 9), randint(0, 9), randint(0, 9)]
soma = 0


def pick():
    print(f'Sorteando 5 valores na lista: {list} PRONTO!')

def soma():
    soma = 0
    for n in list:
        if n % 2 == 0:
            soma += n
    print(f'Somando os valores pares de {list}, temos {soma}')


pick()
soma()