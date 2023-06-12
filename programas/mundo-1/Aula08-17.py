import math
n1 = float(input('Digite o comprimento do cateto oposto'))
n2 = float(input('Digite o comprimento do cateto adjacente'))
h = math.hypot(n1, n2)

print('A hipotenusa do triângulo é {:.2f}'.format(h))
