s = float(input('Qual é o salário do Funcionário? R$ '))
p = s + (s * 15/100)
g = s + (s * 10/100)

if s >= 1250:
    print('O seu salário de R${} agora é R${}'.format(s, g))
else:
    print('O seu salário de R${} agora é de R${}'.format(s, p))
