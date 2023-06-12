from random import randint

itens = ('Casquinha de Sardinha', 'Peixe assado', 'Feijoada', 'Porco assado', 'Falafel', 'Soja')
almoco = randint(0, 5)
print('Hoje vamos almoçar {}'.format(itens[almoco]))