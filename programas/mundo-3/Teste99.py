from time import sleep

def cont(* n):
    tam = len(n)
    mai = max(n)
    print('-=' * 30)
    print('Analisando os valores passados...')
    print(f'{n} Foram informados {tam} valores ao todo.')
    print(f'O maior valor informado foi {mai}.')

def maior(* n):
    cont = maior = 0
    print('-=' * 30)
    print('Analisando os números...')
    for valor in n:
        print(valor, end='  ')
        sleep(0.3)
        if cont == 0:
            maior = valor
        else:
            if valor > maior:
                maior = valor
        cont += 1
    print(f'Foram informados {cont} valores ao todo.')
    print(f'O maior valor informado foi {maior}.')


maior(2, 3, 4, 9, 1, 7)
maior(4, 7, 0)
maior(9)
maior()

