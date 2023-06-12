p = int(input('Qual é seu peso? (Kg): '))
a = float(input('Qual é sua altura? (m): '))

imc = p / (a ** 2)

print('O seu IMC é de {:.2f},'.format(imc), end=' ')

if imc < 18.5:
    print('\033[1;31mVocê está ABAIXO DO PESO')
elif 18.3 <= imc < 25:
    print('\033[1;34mVocê está no PESO IDEAL')
elif 25 <= imc < 30:
    print('\033[1;31mVocê está com SOBREPESO')
elif 30 <= imc < 40:
    print('\033[1;31mVocê está com OBESIDADE')
else:
    print('\033[1;31mVocê está com OBESIDADE MÓRBIDA')