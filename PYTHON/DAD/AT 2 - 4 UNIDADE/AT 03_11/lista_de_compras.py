"""
Prgrama que rebece itens e adiciona na lista e imprime um menu.txt de opções quando digitada a letra 'm'.
Programador: Luciano
25/08/2022.
00:23
"""
#Necessário para pegar a data e hora atual do sistema
import datetime
#Necesário para o timezone(Ajuste de Fuso Horário)


backup = open("backup/arquivos.txt", 'w+')
itens = [] #Recebe os itens da lista
conta_itens = 0 #Para contar os itens inseridos
LIMITE = 30 #constante para exibir os caracteres


#Laço para receber os intens da lista
while True:
    #Insere um item na lista
    itens.append(input(f"Digite o item {conta_itens + 1} da lista ou [m] para exibir o MENU DE OPÇÕES.\n"))

    #Verifica se foi digitado a letra "m". Objetivo, remover o m da lista, sair do laço
    if itens[conta_itens] == "m": #Compara o último item inserido
       itens.pop()#Para remover o "m" da lista
       break

    conta_itens += 1 #Conta a quatidade de itens inseridos
    print(itens) #Exibe a lista
    break



print('*' * LIMITE)
print("      LISTA DE COMPRAS")
print('*' * LIMITE)
print()

#Exibe os itens da lista
for i in range(len(itens)):
    print(f"{i + 1}. {itens[i]}")

#Executado apenas se a lista estiver vazia
if len(itens) == 0:
    print("A sua lista está vazia BB.")
print()
#print('*' * LIMITE)

while True:
    print('*' * LIMITE)
    print("        MENU DE OPÇÕES")
    print('*' * LIMITE)
    print()
    print("1 - INSERIR UM ITEM NA LISTA")
    print("2 - REMOVER ÚLTIMO ITEM INSERIDO")
    print("3 - REMOVER UM ITEM DA LISTA ATRAVÉS DO ÍNDICE")
    print("4 - REMOVER UM ITEM DA LISTA ATRAVÉS DO VALOR NA LISTA")
    print("5 - SALVAR LISTA")
    print("6 - LIMPAR LISTA")
    print("7 - SAIR")

    opcao = int(input("Opção: "))

    if opcao == 1:
        itens.append(input(f"Digite o item.\n"))
        print(itens)
    elif opcao == 2:
        itens.pop()
        print(itens)
    elif opcao == 3:
        itens.pop(int(input(f"Digite o índice para efetuar a remoção do valor nessa posição.\n")))
        print(itens)
    elif opcao == 4:
        itens.remove(input(f"Digite o item da lista para efetuar a remoção.\n"))
        print(itens)
    elif opcao == 5:
        backup.seek(0)
        for item in itens:
            backup.write(f'{item}\n')
        backup.close()
    elif opcao == 6:
        itens.clear()
        print(itens)
    elif opcao == 7:
        break