n = int(input('Digite um número: '))
ct = 0
for c in range(1, n+1):
    if n % c == 0:
        print('\033[34m', end=' ')
        ct = ct + 1
    else:
        print('\033[31m', end=' ')
    print(c, end=' ')
print('\n\033[mO número {} foi divisível {} vezes'.format(n, ct))
if ct == 2:
    print('É PRIMO!')
else:
    print('NÃO É PRIMO!')

