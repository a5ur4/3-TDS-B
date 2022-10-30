def numero():
    numb = int(input("Digite o número desejado: ")) 
    if numb >= 0:
        print(numb, "positivo")
    else:
        print(numb, "negativo")
    return numb


numero()