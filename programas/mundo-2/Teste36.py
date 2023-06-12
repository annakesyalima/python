import time
v = float(input('Qual o valor da casa que você quer comprar? '))
s = float(input('Qual o seu salário? '))
a = int(input('Em quantos anos você quer pagar essa casa? '))
print('Analisando as informações...')
time.sleep(3)

p = v / (a * 12)

print('Para pagar uma casa de R${} em {} anos a prestação será de R${:.2f}'.format(v, a, p))

if p > s / (30/ 100):
    print('\033[1;31mSinto muito, o seu empréstimo foi negado!')
elif p == s / (30/ 100):
    print('\033[1;33mO seu empréstimo foi aprovado, mas você precisa aumentar a sua renda!')
else:
    print('\033[1;32mParabéns, seu empréstimo foi aprovado!')

