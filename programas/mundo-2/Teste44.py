print('{:=^40}'.format(' LOJAS LIMA '))

p = float(input('Qual o valor da sua compra? (R$): '))
print('''\033[1;33mFORMAS DE PAGAMENTO
[ 1 ] à vista dinheiro/cheque
[ 2 ] à vista cartão
[ 3 ] 2x no cartão
[ 4 ] 3x ou mais no cartão\033[m''')

op = int(input('Qual é a opção? '))

if op == 1:
    pf = p - (p * 10 / 100)
    print('\033[1;32mSua compra de R${} vai custar R${} no final'.format(p, pf))
elif op == 2:
    pf = p - (p * 5 / 100)
    print('\033[1;32mSua compra de R${} vai custar R${} no final'.format(p, pf))
elif op == 3 or 4:
    v = int(input('Quantas vezes que parcelar? '))
    if v == 2:
        print('\033[1;32mSua compra vai custar R${}'.format(p))
    else:
        pf = p + (p * 20 / 100)
        print('\033[1;32mSua compra de R${} vai custar R${}'.format(p, pf))


