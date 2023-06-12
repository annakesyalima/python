def voto(ano):
    from datetime import date
    idade = date.today().year - n
    if idade < 18:
        print(f' com {idade} anos: NÃO VOTA')
    elif idade > 60:
        print(f'Com {idade} anos: VOTO OPCIONAL')
    elif idade >= 18 or idade < 60:
        print(f'Com {idade} anos: VOTO OBRIGATÓRIO')


n = int(input('Que ano você nasceu? '))
voto(n)