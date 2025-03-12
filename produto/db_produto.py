import mysql.connector
from config_produto import MYSQL_HOST, MYSQL_USER, MYSQL_PASSWORD, MYSQL_DATABASE

def get_connection():
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

def atualizar_produto(nome, descricao, quantidade, valor):
    conn = get_connection()
    cursor = conn.cursor()
    query = "UPDATE produto SET nome_produto = %s, descricao_produto = %s, quantidade_produto = %s, valor_produto = %s WHERE nome_produto LIKE %s"
    cursor.execute(query, (nome, descricao, quantidade, valor, nome))

    conn.commit()
    cursor.close()
    conn.close()

def listar_produtos():
    conn = get_connection()
    cursor = conn.cursor()
    query = "SELECT * FROM produto"
    cursor.execute(query)
    busca = cursor.fetchall()
    conn.commit()
    cursor.close()
    conn.close()

    return busca

def deletar_produto(produto_requisitado):
    conn = get_connection()
    cursor = conn.cursor()
    query = "DELETE FROM produto WHERE nome_produto = %s"
    cursor.execute(query, (produto_requisitado,))
    conn.commit()
    cursor.close()
    conn.close()

def pesquisar_produto(nome_requisitado):
    conn = get_connection()
    cursor = conn.cursor()
    query = "SELECT * FROM produto WHERE nome_produto = %s"
    cursor.execute(query, (nome_requisitado,))
    busca = cursor.fetchone()
    conn.commit()
    cursor.close()
    conn.close()

    return busca