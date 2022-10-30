lista = [
    ["Davi", 16],
    ["Hagatta", 17],
    ["Arthur", 17],
    ["Carlos", 16]
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
def cadastrar_clientes(cliente, idade) :
    lista.append([cliente, idade])
def listar() :
    print("-" * 20)
    for i in range(0, len(lista)) :
        print("Index do cliente: " + i)
        print(f"Nome do cliente: {lista[i][0]}")
        print(f"Idade do cliente: {lista[i][1]}")
    print("-" * 20)

def contar_clientes() :
    contar = 0
    print("-" * 20)
    for i in lista :
        contar += 1
    print(f"Você tem {contar} clientes")

def buscar_clientes() :
    nome = input("Nome do cliente: ")
    for i in range(0, len(lista)) :
        if lista[i][0] == nome :
            print(f"Index do cliente: {i}")
            print(f"Nome do cliente: {lista[i][0]}")
            print(f"Idade do cliente: {lista[i][1]}")
def main() :
    while True:
        print("*"  * 20)
        print("Escolha uma opção:")
        print("*"  * 20)

        print("1. Cadastrar cliente (nome, idade)\n 2. Listar clientes cadastrados\n 3. Exibir total de clientes cadastrados\n 4. Buscar clientes pelo nome \n 5. Sair")
        print("*" * 20)

        pedido = input("Escolha uma opção: ")

        if pedido == "1" :
            nome = input("Nome do cliente: ")
            idade = input("Idade do cliente: ")

            cadastrar_clientes(nome, idade)
        if pedido == "2" :
            listar()
        if pedido == "3" :
            contar_clientes()
        if pedido == "4" :
            buscar_clientes()
        if pedido == "5" :
            break
main()