import requests
import json

request = requests.get("https://fakestoreapi.com/products")
produtos = json.loads(request.content)#converte a resposta para uma lista de dicionários

print(f"{produtos}\n")
print(f"{produtos[0]}\n")
print(f"{produtos[0]['image']}\n")

for prod in produtos:
    print(f'{prod["image"]}\n')

for titulo in produtos:
    print(f'{titulo["title"]}\n')

backup = open("backup/dados.txt", 'w+')

while True:
    print('1. SALVAR DADOS\n2. LER DADOS\n3. SAIR\n\n')

    opc = int(input('SELECIONE UMA OPCAO: '))

    if opc == 1:
        backup.seek(0)
        for prod in produtos:
            backup.write(f'{prod["image"]}\n')
    elif opc == 2:
        backup.seek(0)
        print(f'{backup.read()}\n')
    elif opc == 3:
        break
    else:
        print('Valor inválido!')

