import pyfiglet

def insert():
    ord_mat = int(input("Digite de que ordem é essa matriz: "))
    if ord_mat == 1:
        det_1dig = int(input("Digite o termo dessa matriz: "))
        print("\nO determinante dessa matriz é: ",det_1dig)
        print(70*'*')
    elif ord_mat == 2:
        a_2 = int(input("Digite o termo da primeira linha e coluna da matriz: "))
        b_2 = int(input("Digite o termo da primeira linha e segunda coluna da matriz: "))
        c_2 = int(input("Digite o termo da segunda linha e primeira coluna da matriz: "))
        d_2 = int(input("Digite o termo da segunda linha e segunda coluna da matriz: "))
        op_det2 = a_2 * d_2 - b_2 * c_2
        print("\nO determinante dessa matriz é: ",op_det2)
        print(70*'*')
    elif ord_mat == 3:
        a_11 = int(input("Digite o primeiro termo da primeira linha e coluna da matriz: "))
        a_12 = int(input("Digite o segundo termo da primeira linha e segunda coluna da matriz: "))
        a_13 = int(input("Digite o terceiro termo da primeira linha e terceira coluna da matriz: "))
        a_21 = int(input("Digite o primeiro termo da segunda linha e primeira coluna da matriz: "))
        a_22 = int(input("Digite o segundo termo da segunda linha e segunda coluna da matriz: "))
        a_23 = int(input("Digite o terceiro termo da segunda linha e terceira coluna da matriz: "))
        a_31 = int(input("Digite o primeiro termo da terceira linha e primeira coluna da matriz: "))
        a_32 = int(input("Digite o segundo termo da terceira linha e segunda coluna da matriz: "))
        a_33 = int(input("Digite o terceiro termo da terceira linha e terceira coluna da matriz: "))
        op_det3 = a_11 * a_22 * a_33 + a_12 * a_23 * a_31 + a_13 * a_21 * a_32 - a_13 * a_22 * a_31 - a_11 * a_23 * a_32 - a_12 * a_21 * a_33
        print("\nO determinante dessa matriz é: ",op_det3)
        print(70*'*')

def Dij():
    v_ij = int(input("Digite os valores de i e j juntos: "))
    if v_ij == 11:
        a_22 = int(input("Digite o segundo termo da segunda linha e segunda coluna da matriz: "))
        a_23 = int(input("Digite o terceiro termo da segunda linha e terceira coluna da matriz: "))
        a_32 = int(input("Digite o segundo termo da terceira linha e segunda coluna da matriz: "))
        a_33 = int(input("Digite o terceiro termo da terceira linha e terceira coluna da matriz: "))
        op_11 = a_22 * a_33 - a_23 * a_32
        print("\nD11 é det = ",op_11)
        print(70*'*')
    elif v_ij == 21:
        a_12 = int(input("Digite o segundo termo da primeira linha e segunda coluna da matriz: "))
        a_13 = int(input("Digite o terceiro termo da primeira linha e terceira coluna da matriz: "))
        a_32 = int(input("Digite o segundo termo da terceira linha e segunda coluna da matriz: "))
        a_33 = int(input("Digite o terceiro termo da terceira linha e terceira coluna da matriz: "))
        op_21 = a_12 * a_33 - a_13 * a_32
        print("\nD21 é det = ",op_21)
        print(70*'*')
    elif v_ij == 31:
        a_12 = int(input("Digite o segundo termo da primeira linha e segunda coluna da matriz: "))
        a_13 = int(input("Digite o terceiro termo da primeira linha e terceira coluna da matriz: "))
        a_22 = int(input("Digite o segundo termo da segunda linha e segunda coluna da matriz: "))
        a_23 = int(input("Digite o terceiro termo da segunda linha e terceira coluna da matriz: "))        
        op_31 = a_12 * a_23 - a_13 * a_22
        print("\nD31 é det = ",op_31)
        print(70*'*')
    elif v_ij == 12:
        a_21 = int(input("Digite o primeiro termo da segunda linha e primeira coluna da matriz: "))
        a_23 = int(input("Digite o terceiro termo da segunda linha e terceira coluna da matriz: "))
        a_31 = int(input("Digite o primeiro termo da terceira linha e primeira coluna da matriz: "))
        a_33 = int(input("Digite o terceiro termo da terceira linha e terceira coluna da matriz: "))
        op_12 = a_21 * a_33 + a_23 * a_31
        print("\nD12 é det = ",op_12)
        print(70*'*')
    elif v_ij == 13:
        a_21 = int(input("Digite o primeiro termo da segunda linha e primeira coluna da matriz: "))
        a_22 = int(input("Digite o segundo termo da segunda linha e segunda coluna da matriz: "))
        a_31 = int(input("Digite o primeiro termo da terceira linha e primeira coluna da matriz: "))
        a_32 = int(input("Digite o segundo termo da terceira linha e segunda coluna da matriz: "))
        op_13 = a_21 * a_32 + a_22 * a_31
        print("\nD13 é det = ",op_13)
        print(70*'*')
    elif v_ij == 22:
        a_11 = int(input("Digite o primeiro termo da primeira linha e coluna da matriz: "))
        a_13 = int(input("Digite o terceiro termo da primeira linha e terceira coluna da matriz: "))
        a_31 = int(input("Digite o primeiro termo da terceira linha e primeira coluna da matriz: "))
        a_33 = int(input("Digite o terceiro termo da terceira linha e terceira coluna da matriz: "))
        op_22 = a_11 * a_33 + a_13 * a_31
        print("\nD22 é det = ",op_22)
        print(70*'*')
    elif v_ij == 23:
        a_11 = int(input("Digite o primeiro termo da primeira linha e coluna da matriz: "))
        a_12 = int(input("Digite o segundo termo da primeira linha e segunda coluna da matriz: "))
        a_31 = int(input("Digite o primeiro termo da terceira linha e primeira coluna da matriz: "))
        a_32 = int(input("Digite o segundo termo da terceira linha e segunda coluna da matriz: "))
        op_23 = a_11 * a_32 + a_12 * a_31
        print("\nD23 é det = ",op_23)
        print(70*'*')
    elif v_ij == 32:
        a_11 = int(input("Digite o primeiro termo da primeira linha e coluna da matriz: "))
        a_13 = int(input("Digite o terceiro termo da primeira linha e terceira coluna da matriz: "))
        a_21 = int(input("Digite o primeiro termo da segunda linha e primeira coluna da matriz: "))
        a_23 = int(input("Digite o terceiro termo da segunda linha e terceira coluna da matriz: "))
        op_32 = a_11 * a_23 + a_13 * a_21
        print("\nD32 é det = ",op_32)
        print(70*'*')
    elif v_ij == 33:
        a_11 = int(input("Digite o primeiro termo da primeira linha e coluna da matriz: "))
        a_12 = int(input("Digite o segundo termo da primeira linha e segunda coluna da matriz: "))
        a_21 = int(input("Digite o primeiro termo da segunda linha e primeira coluna da matriz: "))
        a_22 = int(input("Digite o segundo termo da segunda linha e segunda coluna da matriz: "))
        op_33 = a_11 * a_22 + a_12 * a_21
        print("\nD33 é det = ",op_33)
        print(70*'*')

def Aij():
    i = int(input("Digite a linha (i) da matriz: "))
    j = int(input("Digite a coluna (j) da matriz: "))
    Dij = int(input("Digite o Valor do menor complementar (Dij) da matriz: "))
    op_1Aij = i + j
    op_2Aij = (-1) ** op_1Aij
    op_3Aij = op_2Aij * Dij
    print("\nO valor Cofator é: ",op_3Aij)
    print(70*'*')

def bem_vindo():
    bem_vindo_text = pyfiglet.figlet_format("BEM VINDO", font = "slant"  )
    print(bem_vindo_text)   
    print(70*'*')
    print(10*" ", "SELECIONE UMA DAS OPÇÕES ABAIXO", 10*" ")
    print(70*'*')
    print('\n1 - CALCULADORA DE DETERMINANTE DE MATRIZES')
    print('\n2 - CALCULADORA DE Dij (MENOR COMPLEMENTAR)')
    print('\n3 - CALCULADORA DE Aij (COFRATOR)')
    print('\n4 - SAIR')
    print(70*'*')
    opcao = int(input("Digite a opção: "))

    if opcao == 1:
            insert()
            bem_vindo()
            

    elif opcao == 2:
            Dij()
            bem_vindo()

    elif opcao == 3:
        Aij()
        bem_vindo()

    elif opcao == 4:
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