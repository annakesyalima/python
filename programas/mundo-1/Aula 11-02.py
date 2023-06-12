#print('\033[1;40mHello world!\033[m')

nome = str(input('Qual o seu nome?')).strip()
cor = str(input('Qual a sua cor favorita?')).lower().strip()
cores = {'vermelho': '\033[1;31m', 'azul': '\033[1;36m', 'preto': '\033[1;30m'}
if cor == 'vermelho':
    print('Tenha um bom dia, {} {}'.format(cores['vermelho'], nome))
if cor == 'azul':
    print('Tenha um bom dia, {} {}'.format(cores['azul'], nome))
if cor == 'preto':
    print('Tenha um bom dia, {} {}'.format(cores['preto'], nome))
