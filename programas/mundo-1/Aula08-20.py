import random

n1 = str(input('primeiro aluno: '))
n2 = str(input('segundo aluno: '))
n3 = str(input('terceiro aluno: '))
list = [n1, n2, n3]
random.shuffle(list)
print('A ordem será: ')
print(list)