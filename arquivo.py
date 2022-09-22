lista = [
]

def exibir_menu() :
    print("*"  * 20)
    print("Escolha uma opção:")
    print("*"  * 20)

    print("1. Cadastrar cliente (codigo, nome, idade)\n 2. Listar clientes cadastrados\n 3. Exibir total de clientes cadastrados\n 4. Sair")
    print("*" * 20)

    print("*" * 20)
    for i in range(0,len(lista)) :
        print(lista[i])

def cadastrar_clientes(codigo, cliente, idade) :
    lista.append([codigo, cliente, idade])


def listar() :
    print("-" * 20)
    for i in lista :
        print(i[0, 2, 3])
    print("-" * 20)

def contar_clientes() :
    contar = 0
    print("-" * 20)
    for i in lista :
        contar += 1
    print(f"Você tem {contar} clientes")

def main() :
    while True:
        print("*"  * 20)
        print("Escolha uma opção:")
        print("*"  * 20)

        print("1. Cadastrar cliente (codigo, nome, idade)\n 2. Listar clientes cadastrados\n 3. Exibir total de clientes cadastrados\n 4. Sair")
        print("*" * 20)

        pedido = input("Escolha uma opção: ")

        if pedido == "1" :
            codigo = int(input("Codigo do cliente: "))
            nome = input("Nome do cliente: ")
            idade = input("Idade do cliente: ")

            cadastrar_clientes(codigo, nome, idade)
        if pedido == "2" :
            listar()
        if pedido == "3" :
            contar_clientes()
        if pedido == "4" :
            break
main()