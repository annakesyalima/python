# print('\033[30mAMOR')
# print('\033[4;30;41mEu amo a Keke\033[m')
# print('\033[7;38;47mEu também você!\033[m')
import random

cores = {'limpa': '\033[m', 'azul': '\033[36m'}
nome = ['sofia', 'nicolau', 'amoreira']
pick = random.choice(nome)

print('Bem vindes, {} {} {}'.format(cores['azul'], pick, cores['limpa']))

