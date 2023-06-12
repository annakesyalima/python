import random
import emoji

n1 = str(input('Qual a sua comida favorita? '))
n2 = str(input('Qual é o seu signo?'))
n3 = int(input('Quantos irmãos você tem?'))

list = ['Valentina', 'Luiza', 'Criança mau ator', 'Mãe carrasca', 'irmão creepy']




print('Analisando quem você é em Stupid Wife...')
print('Você é: {}'.format(random.choice(list)))
print(emoji.emojize(':thumbs_up:', language='alias'))
