"""a = 2
b = 3
c = 5

print(False or True)
print(True and True)
print(not (a==b) or (c>a))
print((3 > 1) and (1 == 2))"""

l1 = int(input('Digite o primeiro lado: '))
l2 = int(input('Digite o segundo lado: '))
l3 = int(input('Digite o terceiro lado: '))
if (l1 == l2) and (l2 == l3):
    print('É um triagulo Equilátero')
if (l1 != l2) and (l2 != l3) and (l1 != l3):
    print('É um triângulo escaleno')
if (l1 < l2 + l3) and (l2 < l1 + l3) and (l3 < l1 + l2):
    print('Pode ser um triângilo!')
else:
    print('Não pode ser um triângilo!')