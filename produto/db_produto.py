import mysql.connector
from config_produto import MYSQL_HOST, MYSQL_USER, MYSQL_PASSWORD, MYSQL_DATABASE

def get_connection(self):
    return mysql.connector.connect(
    host = MYSQL_HOST,
    user = MYSQL_USER,
    password = MYSQL_PASSWORD,
    database = MYSQL_DATABASE
)

def registrar_produto(nome, descricao, quantidade, valor):
    conn = get_connection()
    cursor = conn.cursor()
    query = "INSERT INTO produto (nome_produto, descricao_produto, quantidade_produto, valor_produto)VALUES(%s, %s, %s, %s)"
    cursor.execute(query, (nome, descricao, quantidade, valor))

    conn.commit()
    cursor.close()
    conn.close()