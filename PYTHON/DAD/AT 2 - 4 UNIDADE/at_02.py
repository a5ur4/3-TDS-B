# ALUNOS: PEDRO ARTHUR BASTOS MOREIRA, MYQUEIAS SIQUEIRA TORRES SILVA, GABRIEL HEITOR S. D. BRITO
#TURMA: 2°TDS - B

"""
Programa cadastro de Aluno.
Cadastra o nome e a média do aluno e salva em um dicionário
"""

aluno_media = {}
aluno_media_chave = None
aluno_media_valor = None
QTDA_CARACTERES = 60

def criar_linha(caracter, qtda):
    print(caracter * qtda)

def exibir_menu():
    criar_linha('*', QTDA_CARACTERES)
    print("MENU".center(QTDA_CARACTERES))
    criar_linha('*', QTDA_CARACTERES)

    print("""
        1 - CADASTRAR ALUNO  
        2 - MOSTRAR DADOS DO ALUNO
        3 - DELETAR ALUNO DO DICIONARIO     
        4 - FAZER BACKUP EM ARQUIVO
        5 - EXIBIR ALUNOS CADASTRADOS NO ARQUIVO
        6 - SAIR
    """)
    criar_linha('*', QTDA_CARACTERES)

def mostrar_dados():
    if len(aluno_media) > 0:
        print("-" * QTDA_CARACTERES)
        print(f"\033[0;1;33mALUNOS CADASTRADOS = {len(aluno_media)}\033[m")
        print("-" * QTDA_CARACTERES)
        for k, v in aluno_media.items():
            print(f"\033[0;1;33m {k} => {v}\033[m")
        print("-" * QTDA_CARACTERES)
        print()
    else:
        print("\033[0;1;33mNão existe aluno cadastrado!\033[m")
        print()

def inserir_dados():
    nome = input("Digite o nome do aluno\n")
    media = float(input("Digite a média do aluno\n"))
    aluno_media[nome] = media

def deletar():
    deleta = input("Digite o nome do aluno: ")
    if deleta in aluno_media:
        del aluno_media[deleta]
    else:
        print('O valor não desejado existe')

def TESTE(aluno):
    try:
        with open("at.txt", 'w') as file:
            for alunos, medias in aluno_media.items():
                file.write(f'{alunos}:{medias}\n')
    except FileNotFoundError:
        print('o arquivo não foi encontrado')

def ler():
    try:
        with open("at.txt", 'r') as file:
            print(file.read())
    except FileNotFoundError:
        print('o arquivo não foi encontrado')

while True:
    exibir_menu()
    opcao = int(input("Digite a opcao do menu.txt, por favor.\n"))
    if opcao == 1:
        inserir_dados()
    elif opcao == 2:
        mostrar_dados()
    elif opcao == 3:
        deletar()
    elif opcao == 4:
        TESTE(aluno_media)
    elif opcao == 5:
        ler()
    elif opcao == 6:
        break