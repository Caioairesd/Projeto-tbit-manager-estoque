import mysql.connector

MYSQL_HOST = 'localhost'
MYSQL_USER = 'root'
MYSQL_PASSWORD = 'root'
MYSQL_DATABASE = 'tbit_db'

class tbit_db:
    def __init__(self):
        try:
            self.conn = mysql.connector.connect(
                host='localhost',
                user='root',
                password='root'
            )
            self.cursor = self.conn.cursor()
            self.cursor.execute("create database if not exists tbit_db;")
            self.cursor.execute("USE tbit_db;")

            comandos_sql = [
                """
                    CREATE TABLE if not exists Fornecedor 
                    ( 
                    id_fornecedor INT not null auto_increment,  
                    nome_fornecedor varchar(40) not null,  
                    cnpj_fornecedor varchar(18),  
                    email_fornecedor varchar(50),  
                    telefone_fornecedor varchar(20),  
                    cidade_fornecedor varchar(30),
                    pais_fornecedor varchar(30),  
                    constraint pk_fornecedor primary key (id_fornecedor) 
                    );
                """,
                """
                    CREATE TABLE if not exists Produto 
                    ( 
                    id_produto INT not null auto_increment,  
                    nome_produto varchar(40) not null,  
                    descricao_produto varchar(200), 
                    categoria_produto varchar(50), 
                    quantidade_produto INT null,  
                    valor_produto decimal(10,2),  
                    idFornecedor INT not null,
                    constraint pk_produto primary key (id_produto),
                    constraint fk_fornecedor_produto foreign key (idFornecedor) references Fornecedor(id_fornecedor)
                    );
                """,
                """
                    CREATE TABLE if not exists Cliente 
                    ( 
                    id_cliente INT not null auto_increment,  
                    nome_cliente varchar(40) not null,  
                    descricao_cliente varchar(200),  
                    cnpj_cliente varchar(18),
                    constraint pk_cliente primary key (id_cliente)
                    );
                """,
                """
                    CREATE TABLE if not exists Pedido 
                    (
                    id_pedido int not null auto_increment,
                    nota_fiscal varchar(20),
                    data_pedido date,   
                    forma_pagamento varchar(20),
                    quantidade_produto_item int,
                    idProduto int not null,  
                    idCliente int not null,
                    constraint pk_compra primary key (id_pedido),
                    constraint fk_produto_compra foreign key (idProduto) references Produto(id_produto),
                    constraint fk_cliente_compra foreign key (idCliente) references Cliente(id_cliente)
                    );
                """,
                """
                    CREATE TABLE if not exists Funcionario 
                    ( 
                    id_funcionario INT not null auto_increment,  
                    nome_funcionario varchar(40) not null,  
                    data_nascimento_funcionario date,  
                    data_admissao_funcionario date,  
                    cpf_funcionario varchar(14),  
                    cidade_funcionario varchar(30),  
                    estado_funcionario varchar(30),  
                    telefone_funcionario varchar(15),  
                    email_funcionario varchar(50),  
                    usuario_funcionario varchar(30),
                    senha_funcionario varchar(30),
                    perfil_funcionario varchar(30),  
                    constraint pk_funcionario primary key (id_funcionario)
                    );
                """,
                """
                    CREATE TABLE if not exists Cadastro 
                    ( 
                    id_cadastro int not null auto_increment,
                    idFuncionario INT not null,  
                    idCliente INT not null,
                    constraint pk_cadastro primary key (id_cadastro),
                    constraint fk_funcionario_cadastro foreign key (idFuncionario) references Funcionario(id_funcionario),
                    constraint fk_cliente_cadastro foreign key (idCliente) references Cliente(id_cliente)
                    );
                """,
                """
                    CREATE TABLE if not exists Estoque
                    (
                    id_estoque INT not null auto_increment,
                    IdProduto INT not null,
                    quantidade_estoque INT not null,
                    constraint pk_estoque primary key (id_estoque),
                    constraint fk_produto_estoque foreign key (IdProduto) references Produto(id_produto)    
                    );
                """
            ]

            for comando in comandos_sql:
                self.cursor.execute(comando)

            self.conn.commit()
            print("Banco de dados e tabelas criados com sucesso!")
                

            def tabela_vazia(table):
                self.cursor.execute(f"SELECT COUNT(*) FROM {table}")
                return self.cursor.fetchone()[0] == 0

            if tabela_vazia("Funcionario"):
                self.cursor.execute("""
                    INSERT  INTO Funcionario (nome_funcionario, data_nascimento_funcionario, data_admissao_funcionario, cpf_funcionario, cidade_funcionario, estado_funcionario, telefone_funcionario, email_funcionario, usuario_funcionario, senha_funcionario, perfil_funcionario) VALUES
                    ('João Silva', '1985-05-15', '2020-03-10', '111.111.111-11', 'São Paulo', 'SP', '(11) 91234-5678', 'joao.silva@empresa.com', 'joao.silva', 'senha123', 'Administrador');
                    """)    
            self.cursor.close()
            self.cursor = self.conn.cursor()

            try:

                self.cursor.execute("""
                create trigger reabastecer_estoque
                after insert on Estoque
                FOR EACH ROW
                begin
                    update Produto
                    set quantidade_produto = quantidade_produto + new.quantidade_estoque
                    where id_produto = new.IdProduto;
                end;
                """)
            except mysql.connector.Error:
                pass # Trigger já existe

            try:
            
                self.cursor.execute("""
                create trigger diminuir_quantidade_produto
                after insert on pedido
                for each row
                begin
                    update Produto
                    set quantidade_produto = quantidade_produto - new.quantidade_produto_item
                    where id_produto = new.IdProduto;
                end;
                """)
            except mysql.connector.Error:
                pass # Trigger já existe

            try:
                self.cursor.execute("""
                CREATE PROCEDURE delete_fornecedor_e_produtos(IN fornecedor_excluido INT)
                BEGIN
                    
                    IF EXISTS (SELECT 1 FROM Fornecedor WHERE id_fornecedor = fornecedor_excluido) THEN
                    -- Deleta pedidos dos produtos do fornecedor
                    DELETE FROM Pedido 
                    WHERE idProduto IN (
                    SELECT id_produto 
                    FROM Produto 
                    WHERE idFornecedor = fornecedor_excluido
                    );
                    
                    DELETE FROM Estoque 
                    WHERE IdProduto IN (
                    SELECT id_produto 
                    FROM Produto 
                    WHERE idFornecedor = fornecedor_excluido
                    );
                    
                    DELETE FROM Produto 
                    WHERE idFornecedor = fornecedor_excluido;
                    
                    DELETE FROM Fornecedor 
                    WHERE id_fornecedor = fornecedor_excluido;
                    END IF;
                END;
                """)
            except mysql.connector.Error:
                pass # Procedure já existe

            try:
                self.cursor.execute("""
                create procedure delete_produtos(IN produto_excluido INT)
                begin
                    if exists (select 1 from Produto where id_produto = produto_excluido) then
                        
                        delete from Pedido where idProduto = produto_excluido;
                        
                        delete from Estoque where IdProduto = produto_excluido;
                        
                        delete from Produto where id_produto = produto_excluido;
                    end if;
                END;
                """)
            except mysql.connector.Error:
                pass # Procedure já existe

            try:
                self.cursor.execute("""
                DELIMITER $$

                CREATE PROCEDURE delete_cliente(IN cliente_excluido INT)
                BEGIN
                    IF EXISTS (SELECT 1 FROM Cliente WHERE id_cliente = cliente_excluido) THEN

                        DELETE FROM Pedido WHERE idCliente = cliente_excluido;
                        DELETE FROM Cadastro WHERE IdCliente = cliente_excluido;
                        DELETE FROM Cliente WHERE id_cliente = cliente_excluido;

                    END IF;
                END$$

                DELIMITER ;
                """)
            except mysql.connector.Error:
                pass # Procedure já existe

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
def register_fornecedor_db(nome_fornecedor,cnpj_fornecedor,email_fornecedor,telefone_fornecedor,cidade_fornecedor,pais_fornecedor):
    conn = get_connection()
    cursor = conn.cursor()
    query = "insert fornecedor(nome_fornecedor,cnpj_fornecedor,email_fornecedor,telefone_fornecedor,cidade_fornecedor,pais_fornecedor)VALUES(%s,%s,%s,%s,%s,%s)"
    cursor.execute(query,(nome_fornecedor,cnpj_fornecedor,email_fornecedor,telefone_fornecedor,cidade_fornecedor,pais_fornecedor))
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


def update_fornecedor_db(nome_fornecedor,cnpj_fornecedor,email_fornecedor,telefone_fornecedor,cidade_fornecedor,pais_fornecedor):
    conn = get_connection()
    cursor = conn.cursor()
    query = "UPDATE fornecedor SET nome_fornecedor = %s,cnpj_fornecedor = %s,email_fornecedor = %s,telefone_fornecedor = %s,cidade_fornecedor = %s,pais_fornecedor = %s WHERE cnpj_fornecedor = %s"
    cursor.execute(query,(nome_fornecedor,cnpj_fornecedor,email_fornecedor,telefone_fornecedor,cidade_fornecedor,pais_fornecedor,cnpj_fornecedor,))
    conn.commit()
    cursor.close()

def delete_fornecedor_db(id_fornecedor):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.callproc("delete_fornecedor_e_produtos", [id_fornecedor])

    conn.commit()
    cursor.close()

def get_id_cnpj_db():
    conn = get_connection()
    cursor = conn.cursor()

    query = "SELECT id_fornecedor, cnpj_fornecedor FROM fornecedor"

    cursor.execute(query)
    busca = cursor.fetchall()
    conn.commit()
    cursor.close()
    conn.close()

    return busca

#Funções da tabela produto

def registrar_produto_db(nome_produto, descricao, categoria, quantidade, valor, id_fornecedor):
    conn = get_connection()
    cursor = conn.cursor()
    query = "INSERT INTO produto (nome_produto, descricao_produto, categoria_produto, quantidade_produto, valor_produto, idFornecedor)VALUES(%s, %s, %s, %s, %s, %s)"
    cursor.execute(query, (nome_produto, descricao, categoria, quantidade, valor, id_fornecedor))

    conn.commit()
    cursor.close()
    conn.close()

def atualizar_produto_db(nome_produto, descricao, categoria, valor):
    conn = get_connection()
    cursor = conn.cursor()
    query = "UPDATE produto SET nome_produto = %s, descricao_produto = %s, categoria_produto = %s, valor_produto = %s WHERE nome_produto LIKE %s"
    cursor.execute(query, (nome_produto, descricao, categoria, valor, nome_produto))

    conn.commit()
    cursor.close()
    conn.close()

def listar_produtos_db():
    conn = get_connection()
    cursor = conn.cursor()
    
    query = """SELECT p.id_produto, p.nome_produto, p.descricao_produto, p.categoria_produto, p.quantidade_produto, p.valor_produto, f.nome_fornecedor FROM produto AS p 
    JOIN fornecedor AS f ON f.id_fornecedor = p.idFornecedor"""

    cursor.execute(query)
    busca = cursor.fetchall()
    conn.commit()
    cursor.close()
    conn.close()

    return busca

def deletar_produto_db(produto_requisitado):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.callproc("delete_produtos", [produto_requisitado])

    conn.commit()
    cursor.close()
    conn.close()

def pesquisar_produto_db(produto_requisitado):
    conn = get_connection()
    cursor = conn.cursor()
    query = "SELECT * FROM produto WHERE nome_produto = %s OR id_produto = %s"
    cursor.execute(query, (produto_requisitado, produto_requisitado,))
    busca = cursor.fetchone()
    conn.commit()
    cursor.close()
    conn.close()

    return busca

def listar_fornecedores_db():
    conn = get_connection()
    cursor = conn.cursor()
    query = "SELECT id_fornecedor, nome_fornecedor FROM fornecedor"
    cursor.execute(query)
    busca = cursor.fetchall()
    conn.commit()
    cursor.close()
    conn.close()

    return busca

def get_id_produto_db(produto):
    conn = get_connection()
    cursor = conn.cursor()

    query = "SELECT id_produto FROM produto WHERE nome_produto = %s"

    cursor.execute(query, (produto,))
    busca = cursor.fetchone()
    cursor.close()
    conn.close()

    return busca[0]

# funções da tabela  funcionario

# Função para criar um novo funcionário no banco de dados
def register_funcionario_db(nome_funcionario, data_nascimento_funcionario, data_admissao_funcionario, cpf_funcionario, cidade_funcionario, uf_funcionario, telefone_funcionario, email_funcionario, usuario_funcionario, senha_funcionario, perfil_funcionario):
    conn = get_connection()
    cursor = conn.cursor()

    query = """
        INSERT INTO funcionario(nome_funcionario, data_nascimento_funcionario, data_admissao_funcionario,
        cpf_funcionario, cidade_funcionario, estado_funcionario, telefone_funcionario, email_funcionario, 
        usuario_funcionario, senha_funcionario, perfil_funcionario) 
        VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
    """
    cursor.execute(query, (nome_funcionario, data_nascimento_funcionario, data_admissao_funcionario, cpf_funcionario, cidade_funcionario, uf_funcionario, telefone_funcionario, email_funcionario, usuario_funcionario, senha_funcionario, perfil_funcionario))
    
    conn.commit()
    cursor.close()
    conn.close()

# Função para buscar um funcionário por ID
def pesquisar_funcionario_db(id_funcionario):
    conn = get_connection()
    cursor = conn.cursor()
    query = "SELECT * FROM funcionario WHERE id_funcionario = %s OR nome_funcionario = %s"
    cursor.execute(query, (id_funcionario, id_funcionario,))
    result = cursor.fetchone()  # Retorna uma linha, se encontrar o funcionário
    cursor.close()
    conn.close()
    return result

# Função para editar dados de um funcionário
def update_funcionario_db(nome_funcionario, data_nascimento_funcionario, data_admissao_funcionario, cpf_funcionario, cidade_funcionario, uf_funcionario, telefone_funcionario, email_funcionario, usuario_funcionario, senha_funcionario, perfil_funcionario, id_funcionario):
    conn = get_connection()
    cursor = conn.cursor()

    query = """
        UPDATE funcionario 
        SET nome_funcionario = %s, data_nascimento_funcionario = %s, data_admissao_funcionario = %s,
        cpf_funcionario = %s, cidade_funcionario = %s, estado_funcionario = %s, telefone_funcionario = %s, 
        email_funcionario = %s, usuario_funcionario = %s, senha_funcionario = %s, perfil_funcionario = %s 
        WHERE id_funcionario = %s
    """
    cursor.execute(query, (nome_funcionario, data_nascimento_funcionario, data_admissao_funcionario, cpf_funcionario, cidade_funcionario, uf_funcionario, telefone_funcionario, email_funcionario, usuario_funcionario, senha_funcionario, perfil_funcionario, id_funcionario))
    
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

def listar_funcionarios_parcial_db():
    conn = get_connection()
    cursor = conn.cursor()

    query = "SELECT id_funcionario, nome_funcionario, data_admissao_funcionario, cidade_funcionario, estado_funcionario, email_funcionario, perfil_funcionario FROM funcionario "

    cursor.execute(query)
    result = cursor.fetchall()  # Retorna todas as linhas
    cursor.close()
    conn.close()

    return result

# FUNÇÕES USADAS NA TELA DE REABASTECIMENTO E ESTOQUE
def consultar_estoque_db():
    conn = get_connection()
    cursor = conn.cursor()

    query = "SELECT id_produto, nome_produto, categoria_produto, quantidade_produto FROM produto"

    cursor.execute(query)
    result = cursor.fetchall()
    cursor.close()
    conn.close()

    return result

def registrar_reabastecimento_db(id_produto, quantidade_recebida):
    conn = get_connection()
    cursor = conn.cursor()

    query = "INSERT INTO estoque(idProduto, quantidade_estoque) VALUES (%s, %s)"

    cursor.execute(query, (id_produto, quantidade_recebida,))
    conn.commit()
    cursor.close()
    conn.close()

# FUNÇÕES USADAS NA TELA DE CLIENTE
def registrar_cliente_db(nome_cliente, descricao_cliete, cnpj_cliente):
    conn = get_connection()
    cursor = conn.cursor()

    query = "INSERT INTO cliente (nome_cliente, descricao_cliente, cnpj_cliente) VALUES (%s, %s, %s)"

    cursor.execute(query, (nome_cliente, descricao_cliete, cnpj_cliente,))
    conn.commit()
    cursor.close()
    conn.close()

def update_cliente_db(nome_cliente, descricao_cliete, cnpj_cliente, id_usuario):
    conn = get_connection()
    cursor = conn.cursor()

    query = "UPDATE cliente SET nome_cliente = %s, descricao_cliente = %s, cnpj_cliente = %s WHERE id_cliente = %s"

    cursor.execute(query, (nome_cliente, descricao_cliete, cnpj_cliente, id_usuario,))
    conn.commit()
    cursor.close()
    conn.close()

def delete_cliente_db(id_cliente):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.callproc("delete_cliente", [id_cliente])

    conn.commit()
    cursor.close()
    conn.close()

def get_id_cliente_db(cliente):
    conn = get_connection()
    cursor = conn.cursor()

    query = "SELECT id_cliente FROM cliente WHERE nome_cliente = %s"

    cursor.execute(query, (cliente,))
    busca = cursor.fetchone()
    cursor.close()
    conn.close()

    return busca[0]

def get_clientes_db():
    conn = get_connection()
    cursor = conn.cursor()

    query = "SELECT * FROM cliente"

    cursor.execute(query)
    result = cursor.fetchall()
    cursor.close()
    conn.close()

    return result

def pesquisar_cliente_db(cliente_procurado):
    conn = get_connection()
    cursor = conn.cursor()

    query = "SELECT id_cliente, nome_cliente, descricao_cliente, cnpj_cliente FROM cliente WHERE id_cliente = %s"

    cursor.execute(query, (cliente_procurado,))
    result = cursor.fetchone()
    cursor.close()
    conn.close()

    return result

# FUNCOES USADAS NA TELA DE "PEDIDO"
def fazer_pedido_db(nf_pedido, data_pedido, forma_pagamento, quantidade_produto_item, idProduto, idCliente):
    conn = get_connection()
    cursor = conn.cursor()

    query = "INSERT INTO pedido (nota_fiscal, data_pedido, forma_pagamento, quantidade_produto_item, idProduto, idCliente) VALUES (%s, %s, %s, %s, %s, %s)"

    cursor.execute(query, (nf_pedido, data_pedido, forma_pagamento, quantidade_produto_item, idProduto, idCliente,))
    conn.commit()
    cursor.close()
    conn.close()

def get_id_nome_produtos_db():
    conn = get_connection()
    cursor = conn.cursor()

    query = "SELECT id_produto, nome_produto, quantidade_produto FROM produto"

    cursor.execute(query)
    result = cursor.fetchall()
    cursor.close()
    conn.close()

    return result

def get_id_nome_clientes_db():
    conn = get_connection()
    cursor = conn.cursor()

    query = "SELECT id_cliente, nome_cliente FROM cliente"

    cursor.execute(query)
    result = cursor.fetchall()
    cursor.close()
    conn.close()

    return result

def get_pedidos_db():
    conn = get_connection()
    cursor = conn.cursor()

    query = """SELECT pe.id_pedido, pe.nota_fiscal, pe.data_pedido, pe.forma_pagamento, ci.nome_cliente, po.nome_produto, pe.quantidade_produto_item FROM pedido AS pe
            JOIN produto AS po ON po.id_produto = pe.idProduto
            JOIN cliente AS ci ON pe.idCliente = ci.id_cliente"""

    cursor.execute(query)
    result = cursor.fetchall()
    cursor.close()
    conn.close()

    return result

# Funções responsáveis pela funcionalidade do Dashboard

def montante_pedidos():
    conn = get_connection()
    cursor = conn.cursor()
    query = """
    SELECT SUM(pr.valor_produto * pe.quantidade_produto_item) 
    FROM produto pr 
    JOIN pedido pe ON pr.id_produto = pe.IdProduto;
    """
    cursor.execute(query)
    result = cursor.fetchone()[0]  # Pegando apenas o primeiro valor retornado
    cursor.close()
    conn.close()

    return float(result) if result else 0.0  # Convertendo para número puro

def total_vendas():
    conn = get_connection()
    cursor = conn.cursor()
    query = """
    SELECT count(id_pedido) from Pedido;
    """
    cursor.execute(query)
    result = cursor.fetchone()[0] # Pegando apenas o primeiro valor retornado
    cursor.close()
    conn.close()
    
    return int(result )  if result else 0

def total_clientes():
    conn = get_connection()
    cursor = conn.cursor()
    query = """
    select count(id_cliente) from cliente;
    """
    cursor.execute(query)
    result = cursor.fetchone()[0] # Pegando apenas o primeiro valor retornado
    cursor.close()
    conn.close()
    
    return int(result )  if result else 0

def total_produtos():
    conn = get_connection()
    cursor = conn.cursor()
    query = """
    select count(id_produto) from produto;
    """
    cursor.execute(query)
    result = cursor.fetchone()[0] # Pegando apenas o primeiro valor retornado
    cursor.close()
    conn.close()
    
    return int(result )  if result else 0

def produtos_mais_vendidos():
    conn = get_connection()
    cursor = conn.cursor()
    query = """
    SELECT pr.nome_produto, COUNT(pe.id_pedido) AS total_vendas
    FROM pedido pe
    JOIN produto pr ON pe.idProduto = pr.id_produto
    GROUP BY pr.id_produto
    ORDER BY COUNT(pe.id_pedido) DESC
    LIMIT 5;
    """
    cursor.execute(query)
    
    # Pegando todas as linhas da consulta
    resultados = cursor.fetchall()
    
    # Transformando em dicionário
    dados_produtos_mais_vendidos = [dict(nome=row[0], total_vendas=row[1]) for row in resultados]

    cursor.close()
    conn.close()
    return dados_produtos_mais_vendidos

def clientes_mais_pedidos():
    conn = get_connection()
    cursor = conn.cursor()
    query = """
    SELECT cl.nome_cliente, COUNT(pe.id_pedido) AS total_vendas 
    FROM pedido pe JOIN cliente cl 
    ON pe.idCliente = cl.id_cliente 
    GROUP BY cl.nome_cliente 
    ORDER BY COUNT(pe.id_pedido) desc limit 5;
    """
    cursor.execute(query)
    
    
    resultados = cursor.fetchall()
    
    dados_clientes_mais_pedidos = [dict(nome_cliente=row[0], total_vendas=row[1]) for row in resultados]

    cursor.close()
    conn.close()
    return dados_clientes_mais_pedidos

def Categorias_mais_vendidas():
    conn = get_connection()
    cursor = conn.cursor()
    query = """ SELECT pr.categoria_produto, COUNT(pe.id_pedido) AS pedidos_categoria
    FROM pedido pe JOIN produto pr 
    ON pr.id_produto = pe.idProduto 
    GROUP BY pr.categoria_produto 
    ORDER BY COUNT(pe.id_pedido) desc limit 10;
    """
    cursor.execute(query)
    
    
    resultados = cursor.fetchall()
    
    dados_categorias_mais_vendidas = [dict(categoria_produto=row[0], pedidos_categoria=row[1]) for row in resultados]

    cursor.close()
    conn.close()
    return dados_categorias_mais_vendidas

def vendas_por_mes():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SET lc_time_names = 'pt_BR';")
    query =  """
    SELECT 
        DATE_FORMAT(data_pedido, '%M %Y') AS mes_extenso,
        COUNT(*) AS total_vendas
    FROM Pedido
    GROUP BY DATE_FORMAT(data_pedido, '%M %Y')
    ORDER BY MIN(data_pedido);
"""
    cursor.execute(query)
    
    resultados = cursor.fetchall()
    
    dados_pedidos = [dict(mes=row[0],pedidos=row[1]) for row in resultados]

    cursor.close()
    conn.close()
    return dados_pedidos

    '''def update_dashboard():
        
        vendas_por_mes()
        Categorias_mais_vendidas()
        clientes_mais_pedidos()
        produtos_mais_vendidos()
        total_produtos()
        total_clientes()
        total_vendas()'''