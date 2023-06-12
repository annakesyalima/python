import random

n1 = str(input('primeiro aluno: '))
n2 = str(input('segundo aluno: '))
n3 = str(input('terceiro aluno: '))

lista = [n1, n2, n3]
escolhido = random.choice(lista)

print('O escolhido foi {}'.format(escolhido))