def mostraLinha():
    print('-=' * 40)


def emogi():
    print(':D')


def person(p):
    print('-=' * 30)
    print(f'Meu personagem favorito é {p}')
    print('-=' * 30)

def soma(a, b):
    print(f'A = {a} e B = {b}')
    s = a + b
    print(f'A soma de A + B é {s}')

def contador(* n):
    tam = len(n)
    so = sum(n)
    print(f'Recebi os valores {n} e são ao todo {tam} números e somando todos é igual a {so}')

def dobra(l):
    pos = 0
    while pos < len(l):
        l[pos] *= 2
        pos += 1




valores = [2, 3, 6, 7, 8, 9]
dobra(valores)
print(valores)
mostraLinha()
print("I'm learning functions!")
mostraLinha()
emogi(), emogi(), emogi()
person(' AMITY ')
soma(10, 14)
soma(1, 5)
contador(9, 8, 8, 6, 4, 9, 2, 4)
contador(0, 2, 4)
contador(1)