from itertools import count
from re import L
count = 0

def exibirMenu():
    with open("arquivos/menu.txt", 'r') as file:
        print(file.read())

def cadastrarLivro():
    global count
    print(f"Id do livro: {count}")
    livros_nome = input("Digite o nome do livro: ")
    livros_autor = input(f"Digite o nome do autor de {livros_nome}: ")
    file = open("arquivos/livrosCadastrados.txt", 'a+')
    count += 1
    file.write(f"id: {count}\n")
    file.write(f"nome: {livros_nome}\n")
    file.write(f"autor: {livros_autor}\n")
    pass

def exibirLivros():
    file = open("arquivos/livrosCadastrados.txt", 'r')
    file.seek(0)
    print(file.read())
    pass

def buscarLivro():
    nome_busc = input("Digite o nome do livro que desejas: ")
    file = open("arquivos/livrosCadastrados.txt", 'r')
    for line in file.readlines():
        if nome_busc in line:
            print(f"O Livro {nome_busc} foi encontrado. ")
            break
    else:
        print("O livro não foi encontrado")
    
while(True):
   exibirMenu()
   try:
       opcao = int(input("Digite a opção por favor\n"))
       if opcao == 1:
           cadastrarLivro()
       elif opcao == 2:
           exibirLivros()
       elif opcao == 3:
           buscarLivro()
       elif opcao == 4:
           break
   except ValueError:
       print("Você não digitou um número.\n")