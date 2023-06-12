from Mundo3.Teste107.utilidades import moeda
from Mundo3.Teste107.utilidades import dado

p = dado.leiaDinheiro('Digite o preço: R$ ')
moeda.resumo(p, 10, 80)


print('ORBIGADA E VOLTE SEMPRE!'.center(30))
print('TESTE APROVADO'.ljust(30))
print('ATÉ A PROXIMA'.rjust(30))
print(f'{p}'.center(30))
