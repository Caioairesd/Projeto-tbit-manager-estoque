import mysql.connector

MYSQL_HOST = 'localhost'
MYSQL_USER = 'root'
MYSQL_PASSWORD = 'root'
MYSQL_DATABASE = 'tbit_db'

class tbit_db:
    def __init__(self):
        self.conn = mysql.connector.connect(
            host='localhost',
            user='root',
            password='root'
        )
        self.cursor = self.conn.cursor()

        try:
            self.cursor.execute("CREATE DATABASE IF NOT EXISTS tbit_db;")
            self.cursor.execute("USE tbit_db;")

            comandos_sql = [
                
                """CREATE TABLE IF NOT EXISTS fornecedor (
                    id_fornecedor INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
                    nome_fornecedor TEXT,
                    marca_fornecedor TEXT,
                    email_fornecedor TEXT,
                    telefone_fornecedor TEXT,
                    cidade_fornecedor TEXT,
                    pais_fornecedor TEXT
                );""",
                
                """CREATE TABLE IF NOT EXISTS funcionario (
                    id_funcionario INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
                    nome_funcionario TEXT,
                    data_nascimento_funcionario DATE DEFAULT NULL,
                    data_admissao_funcionario DATE DEFAULT NULL,
                    cpf_funcionario TEXT DEFAULT NULL,
                    cidade_funcionario TEXT,
                    estado_funcionario TEXT,
                    telefone_funcionario TEXT,
                    email_funcionario TEXT,
                    usuario_funcionario TEXT,
                    senha_funcionario TEXT
                );""",
                
                """CREATE TABLE IF NOT EXISTS produto (
                    id_produto INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
                    nome_produto TEXT,
                    descricao_produto TEXT,
                    quantidade_produto INT DEFAULT NULL,
                    valor_produto DECIMAL(10, 2) DEFAULT NULL,
                    fornecedor_produto TEXT
                );"""
            ]

            for comando in comandos_sql:
                self.cursor.execute(comando)

            self.conn.commit()
            print("Banco de dados e tabelas criados com sucesso!")

        except mysql.connector.Error as e:
            print(f"Erro ao inicializar o banco de dados: {e}")


    def close(self):
        self.cursor.close()
        self.conn.close()

def get_connection():
    return mysql.connector.connect(
    host = MYSQL_HOST,
    user = MYSQL_USER,
    password = MYSQL_PASSWORD,
    database = MYSQL_DATABASE)


#Funções da tabela fornecedor
def register_fornecedor(nome_fornecedor,marca_fornecedor,email_fornecedor,telefone_fornecedor,cidade_fornecedor,pais_fornecedor):
    conn = get_connection()
    cursor = conn.cursor()
    query = "insert fornecedor(nome_fornecedor,marca_fornecedor,email_fornecedor,telefone_fornecedor,cidade_fornecedor,pais_fornecedor)VALUES(%s,%s,%s,%s,%s,%s)"
    cursor.execute(query,(nome_fornecedor,marca_fornecedor,email_fornecedor,telefone_fornecedor,cidade_fornecedor,pais_fornecedor))
    conn.commit()
    cursor.close()
    conn.close()

def listar_fornecedor_db():
    conn = get_connection()
    cursor = conn.cursor()
    query = "SELECT * FROM fornecedor"
    cursor.execute(query)
    result = cursor.fetchall()
    conn.close()
    return result

def pesquisar_fornecedor_db(id_solicitado):
    conn = get_connection()
    cursor = conn.cursor()
    query = "SELECT * FROM fornecedor WHERE id_fornecedor =%s OR nome_fornecedor =%s"
    cursor.execute(query,(id_solicitado,id_solicitado))
    busca = cursor.fetchone()
    conn.commit()
    cursor.close()
    conn.close()
    return busca


def update_fornecedor(nome_fornecedor,marca_fornecedor,email_fornecedor,telefone_fornecedor,cidade_fornecedor,pais_fornecedor,id_fornecedor):
    conn = get_connection()
    cursor = conn.cursor()
    query = "UPDATE fornecedor SET nome_fornecedor = %s,marca_fornecedor = %s,email_fornecedor = %s,telefone_fornecedor = %s,cidade_fornecedor = %s,pais_fornecedor = %s WHERE id_fornecedor = %s"
    cursor.execute(query,(nome_fornecedor,marca_fornecedor,email_fornecedor,telefone_fornecedor,cidade_fornecedor,pais_fornecedor,id_fornecedor))
    conn.commit()
    cursor.close()

def delete_fornecedor(id_fornecedor):
    conn = get_connection()
    cursor = conn.cursor()
    query = "DELETE FROM fornecedor WHERE id_fornecedor = %s"
    cursor.execute(query,(id_fornecedor,))
    conn.commit()
    cursor.close()

#Funções da tabela produto


def registrar_produto(nome_produto, descricao, quantidade, valor):
    conn = get_connection()
    cursor = conn.cursor()
    query = "INSERT INTO produto (nome_produto, descricao_produto, quantidade_produto, valor_produto)VALUES(%s, %s, %s, %s)"
    cursor.execute(query, (nome_produto, descricao, quantidade, valor))

    conn.commit()
    cursor.close()
    conn.close()

def atualizar_produto(nome_produto, descricao, quantidade, valor):
    conn = get_connection()
    cursor = conn.cursor()
    query = "UPDATE produto SET nome_produto = %s, descricao_produto = %s, quantidade_produto = %s, valor_produto = %s WHERE nome_produto LIKE %s"
    cursor.execute(query, (nome_produto, descricao, quantidade, valor, nome_produto))

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

def pesquisar_produto(produto_requisitado):
    conn = get_connection()
    cursor = conn.cursor()
    query = "SELECT * FROM produto WHERE nome_produto = %s OR id_produto = %s"
    cursor.execute(query, (produto_requisitado, produto_requisitado,))
    busca = cursor.fetchone()
    conn.commit()
    cursor.close()
    conn.close()

    return busca

# funções da tabela  funcionario

# Função para criar um novo funcionário no banco de dados
def register_funcionario_db(nome_funcionario, data_nascimento_funcionario, data_admissao_funcionario, cpf_funcionario, cidade_funcionario, uf_funcionario, telefone_funcionario, email_funcionario, usuario_funcionario, senha_funcionario):
    conn = get_connection()
    cursor = conn.cursor()
    query = """
        INSERT INTO funcionario(nome_funcionario, data_nascimento_funcionario, data_admissao_funcionario,
        cpf_funcionario, cidade_funcionario, estado_funcionario, telefone_funcionario, email_funcionario, 
        usuario_funcionario, senha_funcionario) 
        VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
    """
    cursor.execute(query, (nome_funcionario, data_nascimento_funcionario, data_admissao_funcionario, cpf_funcionario, cidade_funcionario, uf_funcionario, telefone_funcionario, email_funcionario, usuario_funcionario, senha_funcionario))
    conn.commit()
    cursor.close()
    conn.close()

# Função para buscar um funcionário por ID
def pesquisar_funcionario_db(id_funcionario):
    conn = get_connection()
    cursor = conn.cursor()
    query = "SELECT * FROM funcionario WHERE id_funcionario = %s"
    cursor.execute(query, (id_funcionario,))
    result = cursor.fetchone()  # Retorna uma linha, se encontrar o funcionário
    cursor.close()
    conn.close()
    return result

# Função para editar dados de um funcionário
def update_funcionario_db(nome_funcionario, data_nascimento_funcionario, data_admissao_funcionario, cpf_funcionario, cidade_funcionario, uf_funcionario, telefone_funcionario, email_funcionario, usuario_funcionario, senha_funcionario, id_funcionario):
    conn = get_connection()
    cursor = conn.cursor()
    query = """
        UPDATE funcionario 
        SET nome_funcionario = %s, data_nascimento_funcionario = %s, data_admissao_funcionario = %s,
        cpf_funcionario = %s, cidade_funcionario = %s, estado_funcionario = %s, telefone_funcionario = %s, 
        email_funcionario = %s, usuario_funcionario = %s, senha_funcionario = %s 
        WHERE id_funcionario = %s
    """
    cursor.execute(query, (nome_funcionario, data_nascimento_funcionario, data_admissao_funcionario, cpf_funcionario, cidade_funcionario, uf_funcionario, telefone_funcionario, email_funcionario, usuario_funcionario, senha_funcionario, id_funcionario))
    conn.commit()
    cursor.close()
    conn.close()

# Função para excluir um funcionário
def delete_funcionario_db(id_funcionario):
    conn = get_connection()
    cursor = conn.cursor()
    query = "DELETE FROM funcionario WHERE id_funcionario = %s"
    cursor.execute(query, (id_funcionario,))
    conn.commit()
    cursor.close()
    conn.close()

# Função para listar todos os funcionários
def listar_funcionarios_db():
    conn = get_connection()
    cursor = conn.cursor()
    query = "SELECT * FROM funcionario"
    cursor.execute(query)
    result = cursor.fetchall()  # Retorna todas as linhas
    cursor.close()
    conn.close()
    return result
