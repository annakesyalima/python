""""print('\033[1;30;42m~~' * 20)
print(' SISTEMA DE AJUDA PyHELP')
print('~~' * 20)
while True:
    r = str(input('\033[mFunção ou Biblioteca > '))
    if r.upper() in 'FIM':
        break
    print(f'\033[0;37;40m', end='')
    print(help(r))
print('\033[0;30;41mATÉ LOGO')"""

from time import sleep
c = ('\033[m',         # 0 - sem cores
     '\033[0;30;41m',   # 1 - vermelho
     '\033[0;30;42m',   # 2 - verde
     '\033[0;30;44m',   # 3 - azul
     '\033[0;37;40m'      # 4 - branco
    )

def ajuda(com):
    titulo(f'Acessando o manual do comando {com} ', 3)
    print(c[4], end='')
    help(com)
    sleep(2)

def titulo(msg, cor=0):
    tam = len(msg) + 4
    print(c[cor], end='')
    print('~' * tam)
    print(f'  {msg}  ')
    print('~' * tam)
    print(c[0], end='')
    sleep(1)


# Programa Principal
comando = ''
while True:
    titulo('SISTEMA DE AJUDA PyHELP', 2)
    comando = str(input("Função ou Biblioteca > "))
    if comando.upper() == "FIM":
        break
    else:
        ajuda(comando)
titulo('ATÉ LOGO!', 1)