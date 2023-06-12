sexo = ''
idade = 1


sexo = str(input('Informe seus sexo: [M/F]: ')).strip().upper()[0]
while sexo not in 'MF':
    sexo = str(input('Dados inválidos. Por favor, informe seu sexo: ')).strip().upper()[0]

print('O sexo {} registrado com sucesso'.format(sexo))


idade = int(input('Digite a idade: '))

while idade < 18:
    idade = int(input('Pessoas menor de idade. Cadastre outra: '))

print('Pessoa com {} anos.'.format(idade))

profi = str(input('Qual a sua profissão? ')).upper()
if profi == 'PROFESSOR':
    print('Melhore!')
elif profi == 'POLITICO':
    print('Que é isso?')
else:
    print('Boa escolha')

print('FIM DO CADASTRO')
