import openpyxl

def criar():
    nome = input("DIGITE O NOME DA PLANILHA: ")
    nome = openpyxl.Workbook()
    nome_pag_name = input("DIGITE O NOME DA PÁGINA: ")
    nome.create_sheet(nome_pag_name)
    nome_pag = nome[nome_pag_name]
    n_head =  int(input("DIGITE O NÚMERO DE INDICES NA PLANILHA: "))
    if n_head == 1:
        head = input("DIGITE O PRIMEIRO ÍNDICE DA PLANILHA: ")
        nome_pag.append([head])
    elif n_head == 2:
        head = input("DIGITE O PRIMEIRO ÍNDICE DA PLANILHA: ")
        head_2 = input("DIGITE O SEGUNDO ÍNDICE DA PLANILHA: ")
        nome_pag.append(head)
        nome_pag.append(head_2)
    elif n_head == 3:
        head = input("DIGITE O PRIMEIRO ÍNDICE DA PLANILHA: ")
        head_2 = input("DIGITE O SEGUNDO ÍNDICE DA PLANILHA: ")
        head_3 = input("DIGITE O TERCEIRO ÍNDICE DA PLANILHA: ")
        nome_pag.append(head)
        nome_pag.append(head_2)
        nome_pag.append(head_3)

    nome.save('teste.xlsx')

criar()
