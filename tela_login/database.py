import mysql.connector

MYSQL_HOST = 'localhost'
MYSQL_USER = 'root'
MYSQL_PASSWORD = 'root'
MYSQL_DATABASE = 'tbit_db'


import mysql.connector

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
                "DROP TABLE IF EXISTS fornecedor;",
                """CREATE TABLE fornecedor (
                    id_fornecedor INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
                    nome_fornecedor TEXT,
                    marca_fornecedor TEXT,
                    email_fornecedor TEXT,
                    telefone_fornecedor TEXT,
                    cidade_fornecedor TEXT,
                    pais_fornecedor TEXT
                );""",
                "DROP TABLE IF EXISTS funcionario;",
                """CREATE TABLE funcionario (
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
                "DROP TABLE IF EXISTS produto;",
                """CREATE TABLE produto (
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



    def create_funcionario(self, nome_funcionario, data_nascimento_funcionario, data_admissao_funcionario, cpf_funcionario, cidade_funcionario, estado_funcionario, telefone_funcionario, email_funcionario, usuario_funcionario, senha_funcionario):
        self.cursor.execute("""
            INSERT INTO funcionario (nome_funcionario, data_nascimento_funcionario, data_admissao_funcionario, cpf_funcionario, cidade_funcionario, estado_funcionario, telefone_funcionario, email_funcionario, usuario_funcionario, senha_funcionario)
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
        """, (nome_funcionario, data_nascimento_funcionario, data_admissao_funcionario, cpf_funcionario, cidade_funcionario, estado_funcionario, telefone_funcionario, email_funcionario, usuario_funcionario, senha_funcionario))
        self.conn.commit()
    
    def read_funcionario(self, id_funcionario):
        self.cursor.execute('SELECT * FROM funcionario WHERE id_funcionario = %s', (id_funcionario,))
        return self.cursor.fetchone()
    
    def update_funcionario(self, id_funcionario, nome_funcionario, data_nascimento_funcionario, data_admissao_funcionario, cpf_funcionario, cidade_funcionario, estado_funcionario, telefone_funcionario, email_funcionario, usuario_funcionario, senha_funcionario):
        self.cursor.execute("""
            UPDATE funcionario SET 
                nome_funcionario = %s, 
                data_nascimento_funcionario = %s, 
                data_admissao_funcionario = %s, 
                cpf_funcionario = %s, 
                cidade_funcionario = %s, 
                estado_funcionario = %s, 
                telefone_funcionario = %s, 
                email_funcionario = %s, 
                usuario_funcionario = %s, 
                senha_funcionario = %s 
            WHERE id_funcionario = %s
        """, (nome_funcionario, data_nascimento_funcionario, data_admissao_funcionario, cpf_funcionario, cidade_funcionario, estado_funcionario, telefone_funcionario, email_funcionario, usuario_funcionario, senha_funcionario, id_funcionario))

    def delete_funcionario(self, id_funcionario):
        self.cursor.execute('DELETE FROM funcionario WHERE id_funcionario = %s', (id_funcionario,))
        self.conn.commit()

    def create_produto(self, nome_produto, descricao_produto, quantidade_produto, valor_produto, fornecedor_produto):
        self.cursor.execute("""
            INSERT INTO produto (nome_produto, descricao_produto, quantidade_produto, valor_produto, fornecedor_produto)
            VALUES (%s, %s, %s, %s, %s)
        """, (nome_produto, descricao_produto, quantidade_produto, valor_produto, fornecedor_produto))
        self.conn.commit()
    
    def read_produto(self, id_produto):
        self.cursor.execute('SELECT * FROM produto WHERE id_produto = %s', (id_produto,))
        return self.cursor.fetchone()
    
    def update_produto(self, id_produto, nome_produto, descricao_produto, quantidade_produto, valor_produto, fornecedor_produto):
        self.cursor.execute("""
            UPDATE produto SET 
                nome_produto = %s, 
                descricao_produto = %s, 
                quantidade_produto = %s, 
                valor_produto = %s, 
                fornecedor_produto = %s 
            WHERE id_produto = %s
        """, (nome_produto, descricao_produto, quantidade_produto, valor_produto, fornecedor_produto, id_produto))

    def delete_produto(self, id_produto):
        self.cursor.execute('DELETE FROM produto WHERE id_produto = %s', (id_produto,))
        self.conn.commit()
    
