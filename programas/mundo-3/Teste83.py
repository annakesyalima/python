r = str(input('Digite a expressão: '))
list = []
for e in r:
    if e == "(":
        list.append("(")
    elif e == ")":
        if len(list) > 0:
            list.pop()
        else:
            list.append(')')
            break
if len(list) == 0:
    print('Sua expressão está válida!')
else:
    print('Sua expressão está inválida!')