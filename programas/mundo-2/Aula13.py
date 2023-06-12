for c in range(0, 6):
    print('Toy boat')
print('kiss')

for c in range(6, 0, -1):
    print(c)

for c in range(0, 7, 2):
    print(c)

n = int(input('Digite um número para a contagem:'))
for c in range(0, n+1):
    print(c)

i = int(input('Início:'))
f = int(input('Final:'))
p = int(input('Passo:'))
for c in range(i, f+1, p):
    print(c)

for c in range(0, 3):
    n = int(input('Digite um valor: '))

s = 0
for c in range(0, 4):
    n = int(input('Digite um número: '))
    s = s + n
    #s += n
print('A soma de todos os valores é {}'.format(s))