list = [[], [], []]
for c in range(0, 5):
    n = str(input('Digite uma fruta: '))
    p = int(input('Onde quer colocar a fruta: 0, 1 ,2: '))
    list[p].append(n)
for i in list:
    print(i)