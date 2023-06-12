n1 = int(input('Início: '))
n2 = int(input('Fim: '))
s = 1
if n2 < n1:
    s = s - 2
if s == 1:
    n2 = n2 + 1
if s == -1:
    n2 = n2 - 1
for c in range(n1, n2, s):
    print(f'{c}', end=' ')
print('Fim')