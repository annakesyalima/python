maior = 0
pesado = ''
def titulo(msg):
    print('-' * 30)
    print(msg.center(30))
    print(f'O maior Peso até agora é {maior} Kg')
    print('-' * 30)

for c in range(1, 6):
    titulo("DETECTOR DE PESSADO")
    nome = str(input("Digite o nome: "))
    peso = int(input(f'Digite o peso de {nome}: '))
    if c == 1:
        maior = peso
        pesado = nome
    else:
        if peso > maior:
            maior = peso
            pesado = nome
print('-' * 30 )
print(f'O maior peso é de {pesado} com {maior}KG')