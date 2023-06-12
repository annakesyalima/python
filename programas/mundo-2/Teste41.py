from datetime import date
nas = int(input('Digite o ano de nascimento do atleta: '))
atual = date.today().year
idade = atual - nas
print('O atleta tem {} anos'.format(idade))

if idade <= 9:
    print('A categoria do atelata é MIRIM')
elif idade <= 14:
    print('A categoria do atelata é INFANTIL')
elif idade <= 19:
    print('A categoria do atelta é JUNIOR')
elif idade <= 25:
    print('A categoria do atleta é SÊNIOR')
else:
    print('A categoria do atleta é MASTER')