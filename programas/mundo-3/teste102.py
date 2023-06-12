def fatorial(n, show=False):
    """
    -> Calcula o Fatorial de um número
    :param n: O número a ser calculado
    :param show: (opcional) Mostrar ou não mostrar
    :return: O valor do Fatorial  de um número n
    """
    r = 1
    for c in range(n, 0, -1):
        if show:
            print(c, end=' ')
            if c > 1:
                print(' x ', end=' ')
            else:
                print(' = ', end=' ')
        r *= c
    return r



print(fatorial(5, True))
print(fatorial(9, False))
print(fatorial(2, True))