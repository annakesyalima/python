h = m = 0
while True:
    sexo = str(input('Qual sexo? [F/M]')).strip().upper()[0]
    idade = int(input('Qual idade: '))
    cor = int(input("""[1] Preto
                       [2] Castanho
                       [3] Loiro
                       [4] Ruivo"""))
    if sexo in 'M' and cor == 2:
        h = h + 1
    if sexo in 'F' and cor == 3:
        m = m + 1
    resp = str(input('Quer continuar? [S/N]')).upper()[0]
    if resp in 'N':
        break
print(f'Total de homens com mais de 18 anos e cabelos castanhos: {h}')
print(f'Total de mulheres entre 25 e 30 anos e cabelos loiros: {m}')

