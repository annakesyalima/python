def leiaInt(num):
    ok = False
    v = 0
    while True:
        n = str(input(num))
        if n.isnumeric():
            v = int(n)
            ok = True
        else:
            print('\033[1;31mERRO! Digite um número inteiro válido.\033[m')
        if ok:
            break
    return v


n = leiaInt('Digite um número: ')
print(f'Você acabou de digitar o número {n}')