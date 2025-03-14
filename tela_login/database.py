import mysql.connector

MYSQL_HOST = 'localhost'
MYSQL_USER = 'root'
MYSQL_PASSWORD = 'sua_senha'
MYSQL_DATABASE = 'tbit_db'


class tbit_db:
    def __init__(self):
        self.conn = mysql.connector.connect(
            host=MYSQL_HOST,
            user=MYSQL_USER,
            password=MYSQL_PASSWORD,
            database=MYSQL_DATABASE
        )
        self.cursor = self.conn.cursor()
        
        # Criação do banco de dados tbit_db caso não exista
        self.cursor.execute("CREATE DATABASE IF NOT EXISTS `tbit_db`;")
        self.cursor.execute("USE `tbit_db`;")
        
        # Criação das tabelas
        self.cursor.execute("""
            DROP TABLE IF EXISTS `fornecedor`;
            CREATE TABLE `fornecedor` (
                `id_fornecedor` INT NOT NULL AUTO_INCREMENT,
                `nome_fornecedor` TEXT,
                `marca_fornecedor` TEXT,
                `email_fornecedor` TEXT,
                `telefone_fornecedor` TEXT,
                `cidade_fornecedor` TEXT,
                `pais_fornecedor` TEXT,
                PRIMARY KEY (`id_fornecedor`)
            );

            DROP TABLE IF EXISTS `funcionario`;
            CREATE TABLE `funcionario` (
                `id_funcionario` INT NOT NULL AUTO_INCREMENT,
                `nome_funcionario` TEXT,
                `data_nascimento_funcionario` DATE DEFAULT NULL,
                `data_admissao_funcionario` DATE DEFAULT NULL,
                `cpf_funcionario` TEXT DEFAULT NULL,
                `cidade_funcionario` TEXT,
                `estado_funcionario` TEXT,
                `telefone_funcionario` TEXT,
                `email_funcionario` TEXT,
                `usuario_funcionario` TEXT,
                `senha_funcionario` TEXT,
                PRIMARY KEY (`id_funcionario`)
            );

            DROP TABLE IF EXISTS `produto`;
            CREATE TABLE `produto` (
                `id_produto` INT NOT NULL AUTO_INCREMENT,
                `nome_produto` TEXT,
                `descricao_produto` TEXT,
                `quantidade_produto` INT DEFAULT NULL,
                `valor_produto` DECIMAL(10, 2) DEFAULT NULL,
                `fornecedor_produto` TEXT,
                PRIMARY KEY (`id_produto`)
            );
        """)
        
        # Comitar as alterações no banco de dados
        self.conn.commit()

        print("Banco de dados e tabelas criados com sucesso!")

   
    
    def create_fornecedor(self, nome_fornecedor, marca_fornecedor, email_fornecedor, telefone_fornecedor, cidade_fornecedor, pais_fornecedor):
        self.cursor.execute("INSERT INTO fornecedor (marca_fornecedor, email_fornecedor, telefone_fornecedor, cidade_fornecedor, pais_fornecedor)VALUES(%s, %s, %s, %s)", (nome_fornecedor, marca_fornecedor, email_fornecedor, telefone_fornecedor, cidade_fornecedor, pais_fornecedor))
        self.conn.commit()
    
    def read_fornecedor(self, id_fornecedor):
        self.cursor.execute('SELECT * FROM fornecedor WHERE id_fornecedor = %s', (id_fornecedor,))
        return self.cursor.fetchone()
    
    def update_fornecedor(self, id_fornecedor, nome_fornecedor, marca_fornecedor, email_fornecedor, telefone_fornecedor, cidade_fornecedor, pais_fornecedor):
        self.cursor.execute("""
            UPDATE fornecedor SET 
                nome_fornecedor = %s, 
                marca_fornecedor = %s, 
                email_fornecedor = %s, 
                telefone_fornecedor = %s, 
                cidade_fornecedor = %s, 
                pais_fornecedor = %s 
            WHERE id_fornecedor = %s
        """, (nome_fornecedor, marca_fornecedor, email_fornecedor, telefone_fornecedor, cidade_fornecedor, pais_fornecedor, id_fornecedor))

    def delete_fornecedor(self, id_fornecedor):
        self.cursor.execute('DELETE FROM fornecedor WHERE id_fornecedor = %s', (id_fornecedor,))
        self.conn.commit()

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
    
    def close(self):
        self.conn.commit()
        self.conn.close()