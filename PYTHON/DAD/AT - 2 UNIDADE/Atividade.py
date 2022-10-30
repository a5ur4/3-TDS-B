def juros():
    valor_org = int(input("Digite o valor do boleto: "))
    n_dias = int(input("Digite o número de dias: "))
    juros = n_dias * 0.1
    valor_ju = int(juros * valor_org)
    valor_total = valor_org + valor_ju
    print("Valor do boleto = R$",valor_org)
    print("Dias =",n_dias)
    print("A taxa de juros diária = 10%")
    print("Dias em atraso",n_dias)
    print("Valor do Boleto sem juros = R$",valor_org)
    print("Total de juros =",valor_ju)

    print("Boleto atualizado - Valor total = R$",valor_total)


juros()