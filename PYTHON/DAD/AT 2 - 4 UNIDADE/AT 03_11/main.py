import mysql.connector
from mysql.connector import Error

# Script Banco de Dados
"""

CREATE TABLE bd_alunos.tb_alunos (
  id INT NOT NULL AUTO_INCREMENT,
  nome VARCHAR(100) NULL,
  media FLOAT NULL,
  situcao CHAR NULL DEFAULT 'N',
  PRIMARY KEY (id));
"""


def conectarBancoSql():
    try:
        con = mysql.connector.connect(
            host="localhost",
            database="db_alunos",
            user="root",
            password=""
        )

        if con.is_connected():
            db_info = con.get_server_info();
            print("Conexão efetuada com sucesso!", db_info)
            return con
    except Error as e:
        print("Erro ao acessar a tabela MySQL", e)


def listarAlunos():
    query = "SELECT * FROM tb_alunos"
    con = conectarBancoSql()
    consulta_sql = query
    cursor = con.cursor()
    cursor.execute(consulta_sql)
    linhas = cursor.fetchall()
    print("Número total de registros retornados: ", cursor.rowcount)

    if len(linhas) > 0:
        print("\nMostrando os autores cadastrados.")
        for linha in linhas:
            print("ID => ", linha[0])
            print("Nome => ", linha[1])
            print("MÉDIA => ", linha[2])
            if linha[3] == 'S':
               print("SITUCAÇÃO => ", "APROVADO")
            else:
               print("SITUCAÇÃO => ", "REPROVADO")
            print("**********************\n")

    if con.is_connected():
        cursor.close()
        con.close()
        print("A conexão com o MySQL foi encarrada!\n")


listarAlunos()
