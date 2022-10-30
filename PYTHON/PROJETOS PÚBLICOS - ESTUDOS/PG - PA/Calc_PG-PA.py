def termos_da_seq():
    a1_pg = int(input("Digite o primeiro termo da sequência: "))
    q = int(input("Digite a razão: "))
    n_pg = int(input("Digite a posição do termo: "))
    op_1 = n_pg - 1
    op_2 = q ** op_1
    op_3 = a1_pg * op_2
    print(op_3)

def soma_dos_ter():
    a1_pg_2 = int(input("Digite o primeiro termo da sequência: "))
    q_2 = int(input("Digite a razão: "))
    n_pg_2 = int(input("Digite a posição do termo: "))
    op_1_2 = q_2 ** n_pg_2
    op_2_2 = op_1_2 * a1_pg_2
    op_3_2 = q_2 - 1
    op_4_2 = op_2_2 / op_3_2
    print(op_4_2 - 1)

def termos_da_sequencia():
    a1 = int(input("Digite o primeiro termo: "))
    n = int(input("Digite o número de termos: "))
    r = int(input("Digite a razão: "))
    valor_n = n -1
    mult = valor_n * r
    an = mult + a1
    print(an)

def soma_dos_termos():
    an_2 = int(input("Digite o termo geral/ enésimo termo: "))
    a1_2 = int(input("Digite o primeiro termo: "))
    n_2 = int(input("Digite o número de termos: "))
    soma = an_2 + a1_2
    mult_2 = soma * n_2
    sn = mult_2 / 2
    print(sn)

def bem_vindo_PA():
        print(70*'*')
        print(5*" ", "Seja bem vindo a calculadora de progressão aritimética", 15*" ")
        print(5*" ", "Escolha uma das opções abaixo:", 15*" ")
        print(70*'*')
        print('\n1 - TERMOS DA SEQUÊNCIA')
        print('\n2 - SOMA DE TODOS OS TERMOS')
        print('\n3 - SAIR')
        print(70*'*')
        opcao = int(input("Digite a opção: "))

        if opcao == 1:
            termos_da_sequencia()
            bem_vindo_PA()

        elif opcao == 2:
            soma_dos_termos()
            bem_vindo_PA()

        elif opcao == 3: 
            def sair():
                return
        else :
            print("Digite uma opção válida")
            bem_vindo_PA()

def bem_vindo_PG():
    print(70*'*')
    print(5*" ", "Seja bem vindo a calculadora de progressão geométrica", 15*" ")
    print(5*" ", "Escolha uma das opções abaixo:", 15*" ")
    print(70*'*')
    print('\n1 - TERMOS DA SEQUÊNCIA')
    print('\n2 - SOMA DOS TERMOS')
    print('\n3 - SAIR')
    print(70*'*')
    opcao = int(input("Digite a opção: "))

    if opcao == 1:
        termos_da_seq()
        bem_vindo_PG()

    elif opcao == 2:
        soma_dos_ter()
        bem_vindo_PG()

    elif opcao == 3: 
        def sair():
            return
    else :
        print("Digite uma opção válida")
        bem_vindo_PG()

def bem_vindo():
    print(70*'*')
    print(10*" ", "SELECIONE UMA DAS OPÇÕES ABAIXO", 10*" ")
    print(70*'*')
    print('\n1 - CALCULADORA DE PROGRESSÃO ARITIMÉTICA')
    print('\n2 - CALCULADORA DE PROGRESSÃO GEOMÉTRICA')
    print('\n3 - SAIR')
    print(70*'*')
    opcao = int(input("Digite a opção: "))

    if opcao == 1:
        bem_vindo_PA()
        bem_vindo()
        

    elif opcao == 2:
        bem_vindo_PG()
        bem_vindo()

    elif opcao == 3: 
        def sair():
            return
    else :
        print("Digite uma opção válida")
        bem_vindo()

bem_vindo()