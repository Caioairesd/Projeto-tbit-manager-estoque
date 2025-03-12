import mysql.connector
from Config import MYSQL_HOST, MYSQL_USER, MYSQL_PASSWORD, MYSQL_DATABASE

def get_connection():
    return mysql.connector.connect(
        host = MYSQL_HOST,
        user = MYSQL_USER,
        password = MYSQL_PASSWORD,
        database = MYSQL_DATABASE,
    )

def login_funcionario(nome, Data_de_nascimento,  Data_de_admissao,  CPF, Cidade, UF, Telefone, Email, Usuario, Senha):

    conn = get_connection()
    cursor = conn.cursor()
    query = "insert INTO funcionario(id_funcionario, nome_funcionario, data_nascimento_funcionario, data_admissao_funcionario ,cpf_funcionario, cidade_funcionario, estado_funcionario , telefone_funcionario, email_funcionario, usuario_funcionario,senha_funcionario) VALUES(%s, %s, %s, %s, %s,%s,%s,%s,%s,%s)"
    cursor.execute(query, (nome, Data_de_nascimento, Data_de_admissao, CPF, Cidade, UF, Telefone, Email, Usuario, Senha))
    conn.commit()
    cursor.close()
    conn.close()
def editar_funcionario():
    conn = get_connection()
    cursor = conn.cursor()
    query = "SELECT * FROM funcionario"
    cursor.execute(query)
    result = cursor.fetchall()
    cursor.close()
    conn.close()
    return result