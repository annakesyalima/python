print('\033[31m-=' * 12)
print('Sequência de Fibonacci')
print('-=' * 12)

num = int(input('\033[33mQuantos termos você quer mostrar? '))
t1 = 0
t2 = 1
print('-=' * 12)
print('\033[34m{} > {}'.format(t1, t2), end='')
c = 3
while c <= num:
    t3 = t1 + t2
    print(' > {}'.format(t3), end='')
    t1 = t2
    t2 = t3
    c = c + 1


print(' > FIM')


n = int(input('Quantos termos? '))
t1 = 0
t2 = 1
print('{} - {}'.format(t1, t2), end='')
c = 3
while c <= n:
    t3 = t1 + t2
    print(' - {}'.format(t3), end='')
    t1 = t2
    t2 = t3
    c = c + 1
