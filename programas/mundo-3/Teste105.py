def notas(*n, sit=False):
    '''
    - > Função para analisar notas e situações de vários alunos
    :param n: uma ou mais notas e situações de vários alunos
    :param sit: Valor opcional, indicando se deve ou não adicionar a situação.
    :return: dicionário com várias informações sobre a situação da turma
    '''
    r = {}
    r['total'] = len(n)
    r['maior'] = max(n)
    r['menor'] = min(n)
    r['media'] = sum(n) / len(n)
    if sit:
        if r["media"] <= 5:
            r['situação'] = 'RUIM'
        elif 7 >= r["media"] >= 5:
            r['situação'] = 'REGULAR'
        else:
            r['situação'] = 'BOA'
    return f'{r}'



#Programa Principal
resp = notas(5.5, 9.5, 1, 6.0, 3, 1, 1, 4.5, 9, 1, sit=True)
print(resp)
print('-=' * 30)
help(notas)