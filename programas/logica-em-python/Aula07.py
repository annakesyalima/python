from datetime import date
p = str(input('Tenho dinheiro? [S/N] '))
if p in "Ss":
    print('Vou viajar!')
elif p in "Nn":
    print('Vou ficar em casa! ')
print('-=' * 30)

ano = int(input('Em que ano você nasceu? '))
idade = date.today().year - ano
print(f'Em {ano}, você tem {idade} anos.')
if idade >= 21:
    print('Você já é maior de idade.')
else:
    print(f'Você ainda é menor de idade. Faltam {21 - idade} para você ser de maior!')
print('-=' * 30)
n = int(input('Digite um número: '))
if n % 2 == 0:
    print(f'O número {n} é PAR!')
elif n % 2 == 1:
    print(f'O número {n} é ÍMPAR!')
print('-=' * 30)
peso = int(input('Qual é o seu peso? (Kg) '))
alt = float(input('Qual é a sua altura? () '))
imc = peso / (alt * alt)
if 25 >= imc >= 18.5:
    print(f'O seu IMD é {imc:.2f} é voçê está com o PESO IDEAL!')
elif imc > 25:
    print(f'O seu IMC é {imc:.2f} é você está ACIMA DO PESO!')
else:
    print(f'O seu IMC é {imc:.2f} é você está ABAIXO DO PESO!')