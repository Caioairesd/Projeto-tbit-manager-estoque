create database if not exists tbit_db;

use tbit_db;

CREATE TABLE if not exists Fornecedor 
( 
 id_fornecedor INT not null auto_increment,  
 nome_fornecedor varchar(40) not null,  
 cnpj_fornecedor varchar(18),  
 email_fornecedor varchar(50),  
 telefone_fornecedor varchar(20),  
 pais_fornecedor varchar(30),  
 cidade_fornecedor varchar(30),
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

delimiter $$
create procedure delete_fornecedor_e_produtos(IDfornecedor INT)
BEGIN

    DELETE FROM Pedido
    WHERE idProduto IN (SELECT id_produto FROM Produto WHERE idFornecedor = IDfornecedor);

    DELETE FROM Estoque
    WHERE IdProduto IN (SELECT id_produto FROM Produto WHERE idFornecedor = IDfornecedor);

    DELETE FROM Produto
    WHERE idFornecedor = IDfornecedor;

    DELETE FROM Fornecedor
    WHERE id_fornecedor = IDfornecedor;
END;
$$
delimiter ;