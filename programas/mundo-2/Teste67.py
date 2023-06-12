m = 1
while True:
    num = int(input('Qual tabuada você quer? '))
    if num < 0:
        break
    for c in range(1, 11):
        m = num * c
        print(f'{num} x {c} = {m}')
print(f'PROGRAMA TABUADA ENCERRADO. Volte sempre!')