while True:
    print('MENU PRINCIPAL'.center(30))
    print('-' * 30)
    print('1 - Ver pessoas cadastradas')
    print('2 - Cadastrar nova pessoa')
    print('3 - Sair do Sistema')
    print('-' * 30)
    op = str(input('Sua Opção: ')).strip()
    print('-' * 30)
    if op not in '123':
        op = str(input('Sua Opção: ')).strip()
    if op in '1':
        print('Opção 1'.center(30))
        print('-' * 30)
    elif op in '2':
        print('Opção 2'.center(30))
        print('-' * 30)
    elif op in '3':
        print('Saindo do sistema...Até logo'.center(30))
        print('-' * 30)
        break


