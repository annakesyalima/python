tupla = 'zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito','nove', 'dez','onze','doze','treze','quatorze', 'quinze','dezeseis','dezesete','dezoito','dezenove','vinte'

while True:
    n = int(input('Digite um número entre 0 e 20: '))
    if 0 > n > 20:
        n = int(input('Digite um número entre 0 e 20: '))
    if 0 <= n <= 20:
        print(f'Você digitou o número {tupla[n].upper()}')
        break