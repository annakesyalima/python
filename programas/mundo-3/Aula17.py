list = ['sofia', 'nicolau','amoreira']
list[2] = 'lima'
list.append('amoreira')
del list[1]
list.sort()
print(list)
list.sort(reverse=True)
print(list)
list.insert(0, 'Mrs')
print(list)
if 'Mrs' in list:
    list.remove('Mrs')
else:
    print('não é casada ')
print(list)
print(f'Esse nome tem {len(list)} elementos')

print('-=' * 30)

valores = []
valores.append(5)
valores.append(9)
valores.append(1)
valores.append(0)
print(valores)
for c, v in enumerate(valores):
    print(f'O valor {v} está na posição {c+1}')
valores.sort()
print(valores)
for c, v in enumerate(valores):
    print(f'agora, o valor {v} está na posição {c+1}')

num = []
for cont in range(0, 4):
    num.append(int(input('Digite um número de 0 à 5: ')))
num.sort()
for n in num:
    print(n, end='')
c = num[:]
c[0] = 1
print(c)