n = int(input('Quantos alunos tem na sua turma? '))
maior = 0
aluno = ''
for c in range(0, n):
    print(F'ALUNO {c+1}')
    a = str(input('Nome: '))
    nt = float(input(f'Nota de {a}: '))
    print('-=' * 20)
    if c == 0:
        maior = nt
        aluno = a
    else:
        if nt > maior:
            maior = nt
            aluno = a
print(f'O melhor aluno da turmo foi {aluno}, com nota {maior}')