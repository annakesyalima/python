#help(int)
#print(int.__doc__)

def contador(i, f, p):
    """
     -> Faz uma contagem e mostra na tela.
    :param i: início da contagem
    :param f: fim da contagem
    :param p: passo da contagem
    :return: sem retorno
    """
    c = i
    while c <= f:
        print(c, end=' ')
        c += p
    print('FIM!')

def soma(a=0, b=0, c=0):
    s = a + b + c
    print(f'A soma vale {s}')

print('-=' * 30)
contador(0, 100, 20)
#help(contador)
#print(contador.__doc__)
soma(3, 5, 7)
soma(9, 2)
soma(2)
soma()
soma(c=4, a=5)

print('-=' * 30)
def teste():
    print(f'Na função teste, n vale {n}')

n = 2
print(f'No programa principal, n vale {n}')
teste()
print('-=' * 30)
# ESCOPO DE VARIÁVEL

def conte():
    a = 4 #ESCOPO LOCAL
    print(f'O A dentro vale {a}')

conte()
a = 9 #ESCOPO GLOBAL
print(f'O A fora vale {a}')
print('-=' * 30)

#USANDO A VARIÁVEL GLOBAL LOCALMENTE

def t(b):
    global x
    x = 5
    b += 4
    c = 2
    print(f'Agora x vale, {x}, B vale {b}, e C vale {c}')


x = 28
t(2)
print(f'O X fora vale {x}')
print('-=' * 30)

#RETORNO DE VALORES
def plus(k=0, z=0, y=0):
    p = k + z + y
    return p

p1 = plus(10, 4, 5)
p2 = plus(10, 7)
p3 = plus(5)
print(f'Os resultados foram {p1}, {p2} e {p3}')
print('-=' * 30)

def par(m=0):
    if m % 2 == 0:
        return True
    else:
        return False

mum = int(input('Digite um número: '))
if par(mum):
    print('É par!')
else:
    print('É impar!')