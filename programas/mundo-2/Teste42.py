t1 = int(input('Primeiro segmento: '))
t2 = int(input('Segundo segmento: '))
t3 = int(input('Terceiro segmento: '))


if t1 + t2 > t3 and t1 + t3 > t2 and t2 + t3 > t1:
    print('É possível formar um triângulo!!!', end=' ')
    if t1 == t2 and t2 == t3:
        print('Esse triângulo é equilátero')
    elif t1 != t2 and t1 != t3 and t2 != t3 and t3 != t1:
        print('Esse triângulo é escaleno')
    elif t1 == t2 and t1 != t3 or t2 == t3 and t2 != t1 or t3 == t1 and t3 != t2:
        print ('Esse triângulo é isósceles')
else:
    print('Não é possível formar um triângulo com esses segmentos!')