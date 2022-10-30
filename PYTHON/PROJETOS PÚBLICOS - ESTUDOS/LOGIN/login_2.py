def cadastro():
    usuario = input("\nDigite seu nome de usuário: ")
    senha = input("\nDigite sua senha: ")
    if len(senha) > 8:
        print("concluído com sucesso")
    else:
        print("")


cadastro()