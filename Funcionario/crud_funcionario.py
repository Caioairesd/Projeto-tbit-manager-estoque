import mysql.connector
from Config import MYSQL_HOST, MYSQL_USER, MYSQL_PASSWORD, MYSQL_DATABASE

# Função para estabelecer a conexão com o banco de dados
def get_connection():
    return mysql.connector.connect(
        host=MYSQL_HOST,
        user=MYSQL_USER,
        password=MYSQL_PASSWORD,
        database=MYSQL_DATABASE,
    )

# Função para criar um novo funcionário no banco de dados
def login_funcionario(nome, Data_de_nascimento, Data_de_admissao, CPF, Cidade, UF, Telefone, Email, Usuario, Senha):
    conn = get_connection()
    cursor = conn.cursor()
    query = """
        INSERT INTO funcionario(nome_funcionario, data_nascimento_funcionario, data_admissao_funcionario,
        cpf_funcionario, cidade_funcionario, estado_funcionario, telefone_funcionario, email_funcionario, 
        usuario_funcionario, senha_funcionario) 
        VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
    """
    cursor.execute(query, (nome, Data_de_nascimento, Data_de_admissao, CPF, Cidade, UF, Telefone, Email, Usuario, Senha))
    conn.commit()
    cursor.close()
    conn.close()

# Função para buscar um funcionário por ID
def buscar_funcionario(id_funcionario):
    conn = get_connection()
    cursor = conn.cursor()
    query = "SELECT * FROM funcionario WHERE id_funcionario = %s"
    cursor.execute(query, (id_funcionario,))
    result = cursor.fetchone()  # Retorna uma linha, se encontrar o funcionário
    cursor.close()
    conn.close()
    return result

# Função para editar dados de um funcionário
def editar_funcionario(nome, Data_de_nascimento, Data_de_admissao, CPF, Cidade, UF, Telefone, Email, Usuario, Senha, funcionario_id):
    conn = get_connection()
    cursor = conn.cursor()
    query = """
        UPDATE funcionario 
        SET nome_funcionario = %s, data_nascimento_funcionario = %s, data_admissao_funcionario = %s,
        cpf_funcionario = %s, cidade_funcionario = %s, estado_funcionario = %s, telefone_funcionario = %s, 
        email_funcionario = %s, usuario_funcionario = %s, senha_funcionario = %s 
        WHERE id_funcionario = %s
    """
    cursor.execute(query, (nome, Data_de_nascimento, Data_de_admissao, CPF, Cidade, UF, Telefone, Email, Usuario, Senha, funcionario_id))
    conn.commit()
    cursor.close()
    conn.close()

# Função para excluir um funcionário
def excluir_funcionario(funcionario_id):
    conn = get_connection()
    cursor = conn.cursor()
    query = "DELETE FROM funcionario WHERE id_funcionario = %s"
    cursor.execute(query, (funcionario_id,))
    conn.commit()
    cursor.close()
    conn.close()

# Função para listar todos os funcionários
def listar_funcionarios_crud():
    conn = get_connection()
    cursor = conn.cursor()
    query = "SELECT * FROM funcionario"
    cursor.execute(query)
    result = cursor.fetchall()  # Retorna todas as linhas
    cursor.close()
    conn.close()
    return result
