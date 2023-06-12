n1 = int(input('Primeiro valor: '))
n2 = int(input('Segundo valor: '))

print("""
         [ 1 ] somar
         [ 2 ] multiplicar
         [ 3 ] maior
         [ 4 ] novos números
         [ 5 ] sair do programa""")

op = int(input('>>>>> Qual é a sua opção? '))
while op != 5:
    if op == 1:
        s = n1 + n2
        print('A soma entre {} + {} é {}'. format(n1, n2, s))
    if op == 2:
        m = n1 * n2
        print('A multiplicação entre {} e {} é {}'.format(n1, n2, m))
    if op == 3:
        print('O maior número entre {} e {} é {}'.format(n1, n2, max(n1, n2)))
    if op == 4:
        n1 = int(input('Primeiro número: '))
        n2 = int(input('Segundo número: '))
    op = int(input('>>>>> Qual é a sua opção?'))
    if op > 5:
        op = int(input('Opção inválida. Digite a opção novamente: '))

print('FIM')
