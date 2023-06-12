print('-=' * 10)
print('LOJA ECONOMICA')
print('-=' * 10)
t = caro = barato = cont = 0
probarato = ' '

while True:
    produto = str(input('Nome do produto: '))
    valor = float(input('Preço: R$ '))
    t = t + valor
    cont = cont + 1
    c = ' '
    while c not in 'SN':
        c = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if valor >= 1000:
        caro = caro + 1
    if cont == 1:
        barato = valor
        probarato = produto
    else:
        if valor < barato:
            barato = valor
            probarato = produto
    #if cont == 1 or valor < barato: [PODE SER FEITO ASSIM TAMBÉM]
        #barato = valor
        #probarato = produto
    if c == 'N':
        break
print(f'O total das compras foi R$ {t:.2f}')
print(f'Temos {caro} produto custando mais de R$1000 reais')
print(f'O produto mais barato foi {probarato} de R$ {barato:.2f}')