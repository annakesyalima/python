soC = []
tot = 0
for c in range(1, 4):
    nome = str(input('Digite um nome: ')).upper().strip()
    if nome[0] in 'C':
        tot = tot + 1
        soC.append(nome)

for c in soC:
    print(c)
print(f'Foi um total de {tot} pessoas com C')