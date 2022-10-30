def bhaskara():
    a_b = int(input("Digite o termo a da operação: "))
    b_b = int(input("Digite o termo b da operação: "))
    delta_b = int(input("Digite o delta da operação: "))
    op1_b = delta_b ** 0.5
    op2_b = a_b * 2
    op3_b = b_b * -1
    op1_base = op3_b + op1_b
    op2_base = op3_b - op1_b
    op3_base = op1_base / op2_b
    op4_base = op2_base / op2_b
    print(70*'*')
    print("\nX¹ =", op3_base)
    print("\nX² =", op4_base)
    print('\n',70*'*')

def delta():
    a_d = int(input("Digite o termo a de delta: "))
    b_d = int(input("Digite o termo b de delta: "))
    c_d = int(input("Digite o termo c de delta: "))
    op1 = b_d ** 2
    op2 = a_d * c_d
    op2 = op2 * 4
    op3 = op2 - op1
    op4 = op3 * -1
    print(70*'*')
    print("\nΔ =", op4)
    print('\n',70*'*')

def menu():
    print(70*'*')
    print(10*" ", "SELECIONE UMA DAS OPÇÕES ABAIXO", 10*" ")
    print(70*'*')
    print('\n1 - CALCULADORA DE BHASKARA')
    print('\n2 - CALCULADORA DE DELTA')
    print('\n3 - SAIR')
    print(70*'*')
    opcao = int(input("Digite a opção: "))

    if opcao == 1:
        bhaskara()
        menu()
    elif opcao == 2:
        delta()
        menu()
    elif opção == 3:
        exit()

menu()