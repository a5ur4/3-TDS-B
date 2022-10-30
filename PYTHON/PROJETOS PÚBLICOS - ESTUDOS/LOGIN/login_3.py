dic = {}
lista = []
user = ""
password = ""
def cadastro():
    user = input("Digite o nome de usuário: ")
    password = input("Digite sua senha: ")
    if len(password) <= 8:
        confirm_password = input('Confirme sua senha: ')
    else:
        print('Algo deu errado, tente novamente')
    if confirm_password == password:
        print('Cadastro concluído')
        dic.update({user : password})
        lista.append((user, password))
        print(dic)
        
#arrumar a função login
def login():
    usuario = input('Usuario: ')
    senha = input('Senha: ')
    if usuario == dic:
    	if senha == dic:
    		print(f'Login valido, seja bem vindo {user}')
    else: 
        print('Login invalido, verifique as informações do usuário')
        
#arrumar a função mod, pra poder corresponder com as outras acima
def mod():
    user_mod = input('Nome do usuário: ')
    for i in range(0, len(lista)):
        if lista[i][0] == user_mod:
            user_back = input('Digite o novo nome do usuário: ')
            import copy
            mod = copy.deepcopy(dic)
            dic.update({user: user_back})
            lista.append(mod)
        else:
            print('Usuário não encontrado, tente novamente')

def mostrar():
    print(dic)

def menu():
    print(50*'*')
    print(15*' ', 'ESCOLHA UMA OPÇÃO:',15*' ')
    print(50*'*')
    print('\n1 - FAZER O LOGIN')
    print('\n2 - REALIZAR O CADASTRO')
    print('\n3 - MODIFICAR INFORMAÇÕES DO USUÁRIO')
    print('\n4 - MOSTRAR TODOS OS USUÁRIOS CADASTRADOS')
    print('\n5 - SAIR')

    opcao = int(input("\nDigite aqui: "))
    

    if opcao == 1:
        login()
        menu()

    elif opcao == 2:
        cadastro()
        menu()

    elif opcao == 3:
        mod()
        menu()

    elif opcao == 4:
        mostrar()
        menu()

    elif opcao == 5:
        def sair():
            return
    else :
            print("Digite uma opção válida")
            menu()
            
menu()