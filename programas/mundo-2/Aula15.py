from time import sleep
from emoji import emojize
c = 0
while True:
    c = c + 1
    print(emojize(':sushi:' * c))
    sleep(1)
    if c == 1:
        break
print("I'm full!")


n = s = cont = 0
m = 1
while True:
    n = int(input('Digite um número: '))
    if n == 999:
        break
    s += n
    cont += 1
    m *= n
#print('A soma de todos os números é {}'.format(s))
print(f'A soma é {s}')
print(f'Os números foram {cont}')
print(f'A multiplicação deles é {m}')