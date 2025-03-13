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
    query = "insert funcionario(nome_funcionario, data_nascimento_funcionario, data_admissao_funcionario ,cpf_funcionario, cidade_funcionario, estado_funcionario , telefone_funcionario, email_funcionario, usuario_funcionario,senha_funcionario) VALUES(%s, %s, %s, %s, %s,%s,%s,%s,%s,%s)"
    cursor.execute(query, (nome, Data_de_nascimento, Data_de_admissao, CPF, Cidade, UF, Telefone, Email, Usuario, Senha))
    conn.commit()
    cursor.close()
    conn.close()

def buscar_funcionario(id_funcionario):

    conn = get_connection()
    cursor = conn.cursor()
    query = "SELECT * FROM funcionario WHERE id_funcionario = %s"
    cursor.execute(query, (id_funcionario,))
    result = cursor.fetchone()
    cursor.close()
    conn.close()
    return result

def editar_funcionario(nome, Data_de_nascimento, Data_de_admissao, CPF, Cidade, UF, Telefone, Email, Usuario, Senha, funcionario_id):
    conn = get_connection()
    cursor = conn.cursor()
    query = "UPDATE funcionario SET nome = %s,  Data_de_nascimento = %s , Data_de_admissao=%s, CPF=%s, Cidade=%s, UF=%s, Telefone=%s, Email=%s, Usuario=%s, Senha=%s WHERE id_funcionario = %s"
    cursor.execute(query, (nome, Data_de_nascimento, Data_de_admissao, CPF, Cidade, UF, Telefone, Email, Usuario, Senha, funcionario_id))
    conn.commit()
    cursor.close()
    conn.close()
  
def excluir_funcionario (funcionario_id):

    conn = get_connection()
    cursor = conn.cursor()
    query = "DELETE FROM funcionario WHERE id_funcionario = %s"
    cursor.execute(query, (funcionario_id,))
    conn.commit()
    cursor.close()
    conn.close()

