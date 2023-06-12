import math

a = int(input('Qual é o ângulo? '))
s = math.sin(a)
c = math.cos(a)
t = math.tan(a)

print('O seno é {:.2f}, \n o cosseno é {:.2f}, \n e a tangente é {:.2f}'.format(s, c, t))
