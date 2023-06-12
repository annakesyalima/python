def metade(n=0, formato=False):
    res = n / 2
    return res if formato is False else moeda(res)


def dobro(n=0, formato=False):
    res = n * 2
    return res if formato is False else moeda(res)


def aumentar(n=0, p1=0, formato=False):
    res = n + (n * (p1 / 100))
    return res if formato is False else moeda(res)


def diminuir(n=0, p2=0, formato=False):
    res = n - (n * (p2 / 100))
    return res if formato is False else moeda(res)

def moeda(n=0, dinheiro='R$'):
    return f'{dinheiro}{n:.2f}'.replace('.', ',')


def resumo(n=0, p1=10, p2=5):
    print('-' * 30)
    print('RESUMO DO VALOR'.center(30))
    print('-' * 30)
    print(f'Preço analisado: \t\t{moeda(n)}')
    print(f'A metade do preço é: \t{moeda(metade(n))} ')
    print(f'O dobro do preço é: \t{moeda(dobro(n))}')
    print(f'O aumento de {p1}% é \t\t{moeda(aumentar(n, p1))}')
    print(f'O descoto de {p2}% é \t\t{moeda(diminuir(n, p2))}')
    print('-' * 30)

