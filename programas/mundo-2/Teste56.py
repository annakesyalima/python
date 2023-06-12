somaidade = 0
homemvelho = 0
nomevelho = ''
numeromulher = 0

for p in range(1, 5):
    print("----- {}ª PESSOA -----".format(p))
    nome = str(input('Nome: '))
    idade = int(input('Idade: '))
    sexo = str(input('Sexo [M/F]: ')).upper()
    somaidade = somaidade + idade
    media = somaidade / p
    if p == 1 and sexo in 'M':
        homemvelho = idade
        nomevelho = nome
    if sexo in 'M' and idade > homemvelho:
        homemvelho = idade
        nomevelho = nome
    if sexo in 'F' and idade < 20:
        numeromulher = numeromulher + 1


print('A média de idade do grupo é de {} anos'.format(media))
print('O homem mais velho tem {} anos e se chama {}'.format(homemvelho, nomevelho))
print('Ao todo são {} mulheres com menos de 20 anos'.format(numeromulher))


