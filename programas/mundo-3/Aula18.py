data = list()
for c in range(0, 4):
    data.append(input('Digite um nome: '))

print(f'Os nomes digitados são {data}')
novo = list()
novo.append(data[:])

hexisles = [['luz', 13], ['amity', 14], ['willon', 14], ['gus', 10], ['Bump', 162]]
print(hexisles[1][0])
for p in hexisles:
    print(f'{p[0]} tem {p[1]} anos de idade')

test = []
test.append('Anna')
test.append(29)
test.append('streetsmart')
group = []
group.append(test[:])
test[2] = 'criatividade'
group.append(test[:])
print(group)


crew = []
data = []
maior = menor = 0

for c in range(0, 3):
    data.append(str(input('Nome: ')))
    data.append(int(input('Idade: ')))
    crew.append(data[:])
    data.clear()

for p in crew:
    if p[1] >= 18:
        print(f'{p[0]} é maior de idade')
        maior += 1
    else:
        print(f'{p[0]} é menor de idade')
        menor += 1
print(f'Na equipe existem {maior} pessoas maiores de idade e {menor} menores de idade')
