list = []
nome = []
prova = [[], [], []]

for c in range(1, 6):
    nt = str(input(f'Questão {c}: '))
    list.append(nt)

for i in range(0, 3):
    n = str(input('Nome: '))
    nome.append(n)
    for c in range(1, 6):
        na = str(input(f'Questão {c}: '))
        list[i].append(na)


print(list)
print(nome)
print(prova)