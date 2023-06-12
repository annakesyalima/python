tupla = ('luz', 'amity', 'eda', 'hooty',
         'willow', 'gus', 'callob', 'baacha',
         'kikimora','lulu','king', 'belos', 'collector')


for nome in tupla:
    print(f'\nNo nome {nome.upper()} temos as vogais', end=" ")
    for letra in nome:
        if letra in 'aeiou':
            print(letra.upper(), end=' ')
