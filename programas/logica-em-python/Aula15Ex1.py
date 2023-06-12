list = [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]

for l in range(0, 4):
    for c in range(0, 4):
        list[l][c] = int(input(f'Digite um número para a posição[{l}][{c}]: '))

while True:
    r = int(input("""
    [1] Mostrar a Matriz
    [2] Diagonal Principal
    [3] Triangulo Superior
    [4] Triagulo Inferior
    [5] Sair
    : """))
    if r == 1:
        for l in range(0, 4):
            for c in range(0, 4):
                print(f'[{list[l][c]:^7}]', end='')
            print()
    if r == 2:
        for l in range(0, 4):
            for c in range(0, 4):
                if l != c:
                    list[l][c] = ' '
                print(f'[{list[l][c]:^7}]', end='')
            print()
    if r == 3:
        for l in range(0, 4):
            for c in range(0, 4):
                if l == c or l > c:
                    list[l][c] = ' '
                print(f'[{list[l][c]:^7}]', end='')
            print()
    if r == 4:
        for l in range(0, 4):
            for c in range(0, 4):
                if l == c or l < c:
                    list[l][c] = ' '
                print(f'[{list[l][c]:^7}]', end='')
            print()
    if r == 5:
        break


print('Obrigada!')