import mysql.connector
from Config import MYSQL_HOST, MYSQL_USER, MYSQL_PASSWORD, MYSQL_DATABASE

def get_connection():
    return mysql.connector.connect(
        host = MYSQL_HOST,
        user = MYSQL_USER,
        password = MYSQL_PASSWORD,
        database = MYSQL_DATABASE,
    )

def fazer_login_funcionario(nome, DataDeNascimento, DataDeAdmissao, Cidade, CPF, UF, Telefone, Email, Usuario, Senha):

    conn = get_connection()
    cursor = conn.cursor()
    query = "insert usuario(nome, telefone, email, usuario, senha) VALUES(%s, %s, %s, %s, %s)"
    cursor.execute(query, (nome, DataDeNascimento, DataDeAdmissao, Cidade, CPF, UF, Telefone, Email, Usuario, Senha))
    conn.commit()
    cursor.close()
    conn.close()