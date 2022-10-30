dic = {'usuario': 0, 'senha': 0}
lista = []

def login():
    usuario = input('Usuario: ')
    senha = input('\n Senha: ')
    if usuario == user and senha == password:
        print('Login realizado com sucesso')
    else: 
        print('Login invalido, verifique as informações do usuário')

def cadastro():
    user = input("Digite o nome de usuário: ")
    password = input("Digite sua senha: ")
    if len(password) < 8:
        confirm_password = input('Confirme sua senha: ')
    if confirm_password == password:
        print('Cadastro concluído')
        dic.update({'username': usuario})
        dic.update({'senha': senha})
        lista.append((usuario, senha))
    else:
        print('Algo deu errado, tente novamente')

def mod():
    user_mod = input('Nome do usuário: ')
    for i in range(0, len(lista)):
        if lista[i][0] == user_mod:
            user_back = input('Digite o novo nome do usuário: ')
            import copy
            mod = copy.deepcopy(dic)
            dic.update({'usuario': user_back})
            lista.append(mod)
        else:
            print('Usuário não encontrado, tente novamente')

def menu():
    print(50*'*')
    print(20*' ', 'ESCOLHA UMA OPÇÃO:',20*' ')
    print(50*'*')
    print('\n1 - FAZER O LOGIN')
    print('\n2 - REALIZAR O CADASTRO')
    print('\n3 - MODIFICAR INFORMAÇÕES DO USUÁRIO')
    print('\n4 - SAIR')

    opcao = input("\nDigite aqui: ")
    

    if opcao == '1':
        login()
        menu()

    if opcao == '2':
        cadastro()
        menu()

    if opcao == '3':
        mod()
        menu()

    if opcao == '4':
        def sair():
            return
            
menu()