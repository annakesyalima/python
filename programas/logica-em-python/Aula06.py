from datetime import date
from emoji import emojize
nasc = int(input('Qual é o ano do seu nascimento? '))
idade = date.today().year - nasc
print(f'Você precisa colocar {idade} velas no seu bolo', emojize(":birthday_cake:"))

print('_=' * 30)
print('Vou viajar e preciso trocar real para dólar.')
real = float(input('Quanto dinheiro você tem, cláudia? '))
dolar = real / 5.07
print(f'Você vai levar {dolar:.2f} dólares para os EUA.')

print('_=' * 30)
print('Cheguei nos EUA, mas aqui tá 100 Fahrenheit, quando isso dá em Celsius?')
f = int(input('Qual é a temperatura em Fahrenheit? '))
c = (f - 32) / 1.80
print(f'{f}º em Fahrenheit é igual à {c:.2f}º em Celsius!')

print('_=' * 30)
print('Comprei muita coisa nos EUA, agora tenho que pagar imposto')
m = float(input('Quanto de dinheiro você gastou nessas coisas? '))
tax = m * 60 / 100
print(f'Você vai ter que pagar R${tax:.2f} de imposto')

print('-=' * 30)
print('Preciso de dinheiro, vou pegar um empréstimo!')
din = float(input('Quanto você quer de emprestimo? '))
par = int(input('Quantas vezes você quer parcelar esse emprestimo? '))
total = din * 20 / 100
totpar = total / par
print(f'Seu empréstimo de R${din:.2f} pago em {par} vezes vai custar R${totpar:.2f} por mês')