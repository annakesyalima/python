def area(l, c):
    a = l * c
    print(f'A área de um terreno {l}x{c} é de {a}m².')


def lin():
    print('-=' * 30)


print('           CONTROLE DE TERRENOS           ')
lin()
l = float(input('LARGURA (m): '))
c = float(input('COMPRIMENTO (m): '))
area(l, c)
lin()

