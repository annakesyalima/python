list = ['B1', 'B2', 'B3', 'B4', 'B5', 'B6', 'B7', 'B8', 'B9', 'B10']
print('CADEIRAS DISPONÍVEIS: ')
print(list)
while True:
    c = str(input("Reservar a cadeira: ")).strip().upper()
    if c in list:
            print(f'Cadeira {c} RESERVADA!')
    else:
        print('ERRO: Cadeira já reservada!')
        c = str(input("Reservar a cadeira: ")).strip().upper()
    list.remove(c)
    print('-=' * 30)
    print('CADEIRAS AINDA DISPONÍVEIS: ')
    print(list)
    r = str(input('Quer reservar outra? [S/N] '))
    if r in 'Nn':
        break

print('BOM FILME!')