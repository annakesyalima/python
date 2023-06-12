"""n = str(input('Qual é o seu nome? '))
s = float(input('Qual é o seu salário atual? '))
d = int(input('Quantos dependentes você tem? '))
sn = 0
if d == 0:
    sn = s + (s * (5 / 100))
elif 1 <= d <= 3:
    sn = s + (s * (10 / 100))
elif 4 <= d <= 6:
    sn = s + (s * (15 / 100))
else:
    sn = s + (s * (18 / 100))
print(f'{n} por você ter {d} dependentes, seu novo salário é R$ {sn:.2f}')"""

n1 = float(input('Primeira nota: '))
n2 = float(input('Segunda nota: '))
media = (n1 + n2) / 2
print(f'Sua média é {media}.', end=' ')


