from Mundo3.Teste107.utilidades import moeda


def leiaDinheiro(msg):
    valido = False
    while not valido:
        entrada = str(input(msg)).strip().replace(',', '.')
        if entrada.isalpha() or entrada == '':
            print(f'\033[0;31mERRO: "{entrada}" não é um preço válido\033[m')
        else:
            valido = True
            return float(entrada)
