print('--' * 10)
print('CADASTRO DE PESSOAS')
print('--' * 10)
totalmaior = 0
totalhomem = 0
totalmenina = 0

while True:
    idade = int(input('Idade: '))
    sexo = ' '
    while sexo not in 'MF':
        sexo = str(input('Sexo: [M / F]: ')).strip().upper()[0]
    if idade >= 18:
        totalmaior = totalmaior + 1
    if sexo == 'M':
        totalhomem = totalhomem + 1
    if sexo == 'F' and idade < 20:
        totalmenina = totalmenina + 1
    cont = ' '
    while cont not in 'SN':
        cont = str(input('Quer continuar? [S / N]: ')).strip().upper()[0]
    if cont == 'N':
        break
print(f'Total de pessoas com mais de 18 anos: {totalmaior}.')
print(f'Ao todo temos {totalhomem} homens cadastrados.')
print(f'E temos {totalmenina} mulheres com menos de 20 anos.')


