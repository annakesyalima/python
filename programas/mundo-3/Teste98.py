from time import sleep

def cont1():
    print('Contagem de 1 até 10 de 1 em 1: ')
    for c in range(1, 11):
        print(c, end=' ')
        sleep(0.5)
    print('FIM!')

def cont2():
    print('Contagem de 10 até 0 de 2 em 2: ')
    for e in range(10, -1, -2):
        print(e, end=' ')
        sleep(0.5)
    print('FIM!')

def cont3():
    x = int(input('Início: '))
    y = int(input('Fim: '))
    z = int(input('Passo: '))
    print(f'Contagem de {x} até {y} de {z} em {z}')
    for i in range(x, y-1, z):
        print(i, end=' ')
        sleep(0.5)
    print('FIM!')

def lin():
    print('-=' * 30)


#PROGRAMA PRINCIPAL
lin()
cont1()
lin()
cont2()
lin()
cont3()
lin()
