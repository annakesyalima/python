list1 = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

for l in range(0, 3):
    for c in range(0, 3):
        list1[l][c] = int(input(f'Digite um valor para [{l}, {c}]: '))
print('-=' * 40)
for l in range(0, 3):
    for c in range(0, 3):
        print(f'[{list1[l][c]:^7}]', end='')
    print()
