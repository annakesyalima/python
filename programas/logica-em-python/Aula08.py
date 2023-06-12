"""d = int(input("Quanto dinheiro você tem? "))
if d >= 10000:
    print('Partiu Itália!')
elif d >= 5000:
    print('Partiu Jeri de novo!')
else:
    print('chateada, vou ficar me casa!')
print('-=' * 30)

n1 = float(input('Qual a primeira nota do aluno? '))
n2 = float(input('Qual a segunda nota do aluno? '))
media = (n1 + n2) / 2
if media > 7:
    print('Aluno aprovado com sucesso!')
elif 5 < media < 7:
    print('Aluno em recuperação!')
else:
    print('Aluno reprovado!')
print('-=' * 30)
peso = float(input('Qual é o seu peso? '))
alt = float(input('Qual é a sua altura? '))
imc = peso / (alt * alt)
print(f'O seu IMC é: {imc:.1f}.', end=' ')
if imc <= 17:
    print('Você está Muito abaixo do peso!')
elif 17 <= imc <= 18.5:
    print('Você está Abaixo do peso!')
elif 18.5 <= imc <= 25:
    print('Você está no Peso ideal!')
elif 25 <= imc <= 30:
    print('Você está com Sobrepeso!')
elif 30 <= imc <= 35:
    print('Você está com Obesidade!')
elif 35 <= imc <= 40:
    print('Você está com Obesidade Severa!')
else:
    print('Você está com Obesidade Mórbida!')"""

print('CRINÇA ESPERANÇA'.center(40))
print(""" 
          [1] - para doar R$ 10 
          [2] - para doar R$ 25
          [3] - para doar R$ 50
          [4] - para doar Outros Valores
          [5] - para cancelar""")
d = int(input('Quanto você quer doar? '))
v = 0

if d == 1:
    v = 10
elif d == 2:
    v = 25
elif d == 3:
    v = 50
elif d == 4:
    v = int(input('Quando você quer doar? '))
elif d == 5:
    v = 0
print('-=' * 30)
print(f'A sua doação foi de R${v}')

