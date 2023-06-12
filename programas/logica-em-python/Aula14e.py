import random

list = []

for c in range(0, 3):
    t = str(input('Digite um time: '))
    list.append(t)
print('-=' * 30)
for i in list:
    for b in list:
        if i != b:
            print(f'{i:<10}  x {b:>10}')

