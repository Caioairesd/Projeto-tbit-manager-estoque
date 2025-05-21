create database if not exists tbit_db;

use tbit_db;

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

CREATE TABLE if not exists Cliente 
( 
    id_cliente INT not null auto_increment,  
    nome_cliente varchar(40) not null,  
    descricao_cliente varchar(200),  
    cnpj_cliente varchar(18),
    constraint pk_cliente primary key (id_cliente)
); 

CREATE TABLE if not exists Pedido 
(
    id_pedido int not null auto_increment,
    nota_fiscal varchar(20),
    data_pedido date,   
    forma_pagamento varchar(20),
    quantidade_produto_item int,
    idProduto int not null,  
    idCliente int not null,
    constraint pk_pedido primary key (id_pedido),
    constraint fk_produto_pedido foreign key (idProduto) references Produto(id_produto),
    constraint fk_cliente_pedido foreign key (idCliente) references Cliente(id_cliente)
); 

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

CREATE TABLE if not exists Cadastro 
( 
    id_cadastro int not null auto_increment,
    idFuncionario INT not null,  
    idCliente INT not null,
    constraint pk_cadastro primary key (id_cadastro),
    constraint fk_funcionario_cadastro foreign key (idFuncionario) references Funcionario(id_funcionario),
    constraint fk_cliente_cadastro foreign key (idCliente) references Cliente(id_cliente)
); 

CREATE TABLE if not exists Estoque
(
    id_estoque INT not null auto_increment,
    IdProduto INT not null,
    quantidade_estoque INT not null,
    constraint pk_estoque primary key (id_estoque),
    constraint fk_produto_estoque foreign key (IdProduto) references Produto(id_produto)
);

-- INSERT ÚNICO PARA ACESSO AO SISTEMA COMO USUÁRIO MASTER
INSERT  INTO Funcionario (nome_funcionario, data_nascimento_funcionario, data_admissao_funcionario, cpf_funcionario, cidade_funcionario, estado_funcionario, telefone_funcionario, email_funcionario, usuario_funcionario, senha_funcionario, perfil_funcionario) VALUES
('João Silva', '1985-05-15', '2020-03-10', '111.111.111-11', 'São Paulo', 'SP', '(11) 91234-5678', 'joao.silva@empresa.com', 'joao.silva', 'senha123', 'Administrador');

delimiter $$
    create trigger reabastecer_estoque
    after insert on Estoque
    FOR EACH ROW
    begin
        update Produto
        set quantidade_produto = quantidade_produto + new.quantidade_estoque
        where id_produto = new.IdProduto;
    end;
$$
delimiter ;

delimiter $$
    create trigger diminuir_quantidade_produto
    after insert on pedido
    for each row
    begin
        update Produto
        set quantidade_produto = quantidade_produto - new.quantidade_produto_item
        where id_produto = new.IdProduto;
    end;
$$
delimiter ;

DELIMITER $$
    CREATE PROCEDURE delete_fornecedor_e_produtos(IN fornecedor_excluido INT)
    BEGIN
        -- Verifica se o fornecedor existe
        IF EXISTS (SELECT 1 FROM Fornecedor WHERE id_fornecedor = fornecedor_excluido) THEN
        -- Deleta pedidos dos produtos do fornecedor
        DELETE FROM Pedido 
        WHERE idProduto IN (
        SELECT id_produto 
        FROM Produto 
        WHERE idFornecedor = fornecedor_excluido
        );
        -- Deleta estoque dos produtos do fornecedor
        DELETE FROM Estoque 
        WHERE IdProduto IN (
        SELECT id_produto 
        FROM Produto 
        WHERE idFornecedor = fornecedor_excluido
        );
        -- Deleta os produtos do fornecedor
        DELETE FROM Produto 
        WHERE idFornecedor = fornecedor_excluido;
        -- Por fim, deleta o fornecedor
        DELETE FROM Fornecedor 
        WHERE id_fornecedor = fornecedor_excluido;
        END IF;
    END$$
DELIMITER ;

-- procedure para deletar um produto e suas dependências
delimiter $$
    create procedure delete_produtos(IN produto_excluido INT)
    begin
        if exists (select 1 from Produto where id_produto = produto_excluido) then
            -- Deleta os pedidos associados ao produto
            delete from Pedido where idProduto = produto_excluido;

            -- Deleta o estoque associado ao produto
            delete from Estoque where IdProduto = produto_excluido;

            -- Deleta o produto
            delete from Produto where id_produto = produto_excluido;
        end if;
    END$$
DELIMITER ;

DELIMITER $$
	CREATE PROCEDURE delete_cliente(IN cliente_excluido INT)
		BEGIN
			IF EXISTS (SELECT 1 FROM Cliente WHERE id_cliente = cliente_excluido) THEN

			DELETE FROM Pedido WHERE idCliente = cliente_excluido;
			DELETE FROM Cadastro WHERE IdCliente = cliente_excluido;
			DELETE FROM Cliente WHERE id_cliente = cliente_excluido;
		end if;
	END$$
DELIMITER ;