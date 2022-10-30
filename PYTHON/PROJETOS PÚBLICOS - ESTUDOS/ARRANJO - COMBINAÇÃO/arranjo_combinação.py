import pyfiglet
from math import factorial

def arranjo():
    n = int(input("Digite o valor de (n): "))
    p = int(input("Digite o valor de (p): "))
    n_fact = factorial(n)
    op1 = n - p
    p_fact = factorial(op1)
    vf_fact = n_fact / p_fact
    print("\nO valor do arranjo é de: ",vf_fact)
    print(70*'*')

def combinação():
    n_c = int(input("Digite o valor de (n): "))
    p_c = int(input("Digite o valor de (p): "))
    n_c_fact = factorial(n_c)
    p_c_fact = factorial(p_c)
    op1_c = n_c - p_c
    op1_c_fact = factorial(op1_c)
    op2_c_fact = p_c_fact * op1_c_fact
    opv_comb = n_c_fact / op2_c_fact
    print("\nO valor de combinação é de: ",opv_comb)
    print(70*'*')

def bem_vindo():
    bem_vindo_text = pyfiglet.figlet_format("BEM VINDO", font = "slant"  )
    print(bem_vindo_text)   
    print(70*'*')
    print(10*" ", "SELECIONE UMA DAS OPÇÕES ABAIXO", 10*" ")
    print(70*'*')
    print('\n1 - CALCULADORA DE ARRANJO')
    print('\n2 - CALCULADORA DE COMBINAÇÃO')
    print('\n3 - SAIR')
    print(70*'*')
    opcao = int(input("Digite a opção: "))
    if opcao == 1:
            arranjo()
            bem_vindo()
            
    elif opcao == 2:
            combinação()
            bem_vindo()

    elif opcao == 3:
        print(70*'*')
        print("Tem certeza de que deseja sair?")
        decision = input("Se sim digite (s), se não digite (n): ")
        if decision =='s':
            def sair():
                return
        else:
            bem_vindo()
            
    else:
        print("Digite uma opção válida")
        bem_vindo()


bem_vindo()