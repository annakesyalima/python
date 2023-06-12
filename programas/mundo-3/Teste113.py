def leiaInt(n):
    while True:
        try:
            n = int(input('\033[mDigite um número Inteiro: '))
        except (ValueError, TypeError):
            print('\033[31mERRO: por favor, digite um número inteiro válido.')
        except Exception as erro:
            print(f'\033[31mO erro encontrado foi {erro.__cause__}')
            continue
        except KeyboardInterrupt:
            print('\033[31mO usuário preferiu não informar os dados.')
            return 0
        else:
            return n

def leiaReal(n):
    while True:
        try:
            n = float(input('\033[mDigite um número Real: '))
        except (ValueError, TypeError):
            print('\033[31mERRO: por favor, digite um número real válido.')
        except Exception as erro:
            print(f'\033[31mO erro encontrado foi {erro.__cause__}')
            continue
        except KeyboardInterrupt:
            print('\033[31mO usuário preferiu não informar os dados.')
            return 0
        else:
            return n



num = leiaInt('Digite um valor inteiro: ')
num2 = leiaReal(('Digite um valor real: '))
print(f'O valor inteiro foi {num} e o real foi {num2}')

