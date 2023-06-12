import random

n = str(input('Digite seu nome completo: ')).strip()

print('Analisando o seu nome...')
print('Seu nome em maiúsculo é {}'.format(n.upper()))
print('Seu nome em minúsculo é {}'.format(n.lower()))
print('Seu nome tem ao todo {}'.format(len(n) - n.count(' ')))
#print('Seu primeiro nome tem {} letras'.format(n.find(' ')))

s = n.split()
print('Seu primeiro nome é {} e ele tem {} letras'.format(s[0], len(s[0])))
x = ['gay', 'hétero']
y = ['bonito', 'feio', 'pegável', 'mais ou menos']
print('Sua sexualidade é {}'.format(random.choice(x)))
print('O que as pessoas pensam de você: {}'.format(random.choice(y)))