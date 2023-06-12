print('{:=^40}'.format('='))
print(('10 TERMOS DE UMA PA'))
print('{:=^40}'.format('='))

p = int(input('Primeiro termo: '))
r = int(input('Razão: '))
for c in range(1, 11):
    pg = p + (c - 1) * r
    print(pg, end=' > ')
print('ACABOU')