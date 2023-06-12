k = float(input('Quantos kilometros você andou?'))
d = float(input('Quantos dias você alugou o carro?'))
p = (d * 60) + (k * 0.15)

print('O total a pagar é de R${:.2f}'.format(p))