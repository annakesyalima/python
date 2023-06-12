from datetime import date

a = int(input('Ano de nascimento: '))
atual = date.today().year
idade = atual - a
alista = 18 - idade
atraso = idade - 18
deveria = atual - atraso

print('Quem nasceu em {} tem {} em {}.'.format(a, idade, atual))

if idade < 18:
    print('Ainda faltam {} anos para o alistamento'.format(alista))
elif idade > 18:
    print('Você já deveria ter se alistado há {} anos.'.format(atraso))
    print('Seu alistamento foi em {}.'.format(deveria))
else:
    print('Você tem que se alistar IMEDIATAMENTE!')