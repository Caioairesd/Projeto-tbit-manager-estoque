import mysql.connector
from config_fornecedor import MYSQL_HOST,MYSQL_USER, MYSQL_PASSWORD, MYSQL_DATABASE 

def get_connection():
    return mysql.connector.connect(
    host = MYSQL_HOST,
    user = MYSQL_USER,
    password = MYSQL_PASSWORD,
    database = MYSQL_DATABASE)

def register_fornecedor(nome_fornecedor,marca_fornecedor,email_fornecedor,telefone_fornecedor,cidade_fornecedor,pais_fornecedor):
    conn = get_connection()
    cursor = conn.cursor()
    query = "insert fornecedor(nome_fornecedor,marca_fornecedor,email_fornecedor,telefone_fornecedor,cidade_fornecedor,pais_fornecedor)VALUES(%s,%s,%s,%s,%s,%s)"
    cursor.execute(query,(nome_fornecedor,marca_fornecedor,email_fornecedor,telefone_fornecedor,cidade_fornecedor,pais_fornecedor))
    conn.commit()
    cursor.close()
    conn.close()

def read_fornecedor():
    conn = get_connection()
    cursor = conn.cursor()
    query = "SELECT * FROM tbit_db"
    cursor.execute(query)
    result = cursor.close()
    conn.close()
    return result

def update_fornecedor(nome_fornecedor,marca_fornecedor,email_fornecedor,telefone_fornecedor,cidade_fornecedor,pais_fornecedor):
    conn = get_connection()
    cursor = conn.cursor()
    query = "UPDATE tbit_db SET nome_fornecedor = %s,marca_fornecedor = %s,email_fornecedor = %s,telefone_fornecedor = %s,cidade_fornecedor = %s,pais_fornecedor = %s WHERE id_fornecedor = %s"
    cursor.execute(query,(nome_fornecedor,marca_fornecedor,email_fornecedor,telefone_fornecedor,cidade_fornecedor,pais_fornecedor))
    conn.commit()
    cursor.close()

def delete_fornecedor(id_fornecedor):
    conn = get_connection()
    cursor = conn.cursor()
    query = "DELETE FROM fornecedor WHERE id_fornecedor = %s"
    cursor.execute(query,(id_fornecedor))
    conn.commit()
    cursor.close()
    






