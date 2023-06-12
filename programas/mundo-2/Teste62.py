print('\033[34mGerador de PA')
print('-=' * 10)
p = int(input('\033[mPrimeiro termo: '))
r = int(input('Razão: '))
n = p
c = 1
total = 0
mais = 10
while mais != 0:
    total = total + mais
    while c <= total:
        print(n, end=" > ")
        n = n + r
        c = c + 1
    print('PAUSA')
    mais = (int(input('Quantos termos você quer mostrar a mais? ')))

print(' > FIM')
print('Progressão finalizada com {} termos mostrados'.format(total))


