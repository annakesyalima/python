nome = str(input('Digite uma frase: ')).strip().upper()
palavra = nome.split()
junto = ''.join(palavra)
inverso = junto[::-1]

"""inverso = ''
for nome in range(len(junto) -1, -1, -1):
    inverso = inverso + junto[nome]"""
print('O inverso de {} é {}'.format(junto, inverso))

if junto == inverso:
    print('é um PALÍNDROMO!')
else:
    print('não é um PALÍNDROMO!')