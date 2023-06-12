nome = []
nota1 = []
nota2 = []
media = []

for c in range(1, 5):
    n = str(input('Nome: '))
    nome.append(n)
    n1 = int(input('Primeira nota: '))
    nota1.append(n1)
    n2 = int(input('Segunda nota: '))
    nota2.append(n2)
    m = (n1 + n2) / 2
    media.append(m)

for i in nome:
    for j in media:
        print(f'{i}  \t{j}')