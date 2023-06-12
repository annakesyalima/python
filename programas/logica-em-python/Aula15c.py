list = [[1, 0, 0], [0, 1, 0], [0, 0, 1]]
print('-=' * 40)
for l in range(0, 3):
    for c in range(0, 3):
        print(f'[{list[l][c]:^7}]', end='')
    print()

list = [[1, 0, 1], [0, 1, 0], [0, 0, 1]]
print('-=' * 30)
for l in range(0, 3):
    for c in range(0, 3):
        print(f'[{list[l][c]:^7}]', end='')
    print()