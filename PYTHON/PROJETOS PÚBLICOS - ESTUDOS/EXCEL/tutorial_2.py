import openpyxl

#Carregando arquivo
book = openpyxl.load_workbook('Planilha de frutas.xlsx')
#Selecionando uma pagina
frutas_page = book['Frutas']
#Imprimindo os dados de cada linha
#min_row é pra apartir de qual linha quer ler e max_row até qual linha deve-se ler
for rows in frutas_page.iter_rows(min_row=2, max_row=5):
    for cell in rows:
        #printar as informações de maneira crua
        #print(cell.value)
        #printar as informações de maneira organizada
        #print(f'{rows[0].value},{rows[1].value},{rows[2].value}')
        #modificar coisas na planiha
        if cell.value == 'Banana':
            cell.value = 'Frutas 1'

#salvar as alterações
book.save('Planilha de frutas.xlsx')
