drop database tbit_db;

create database tbit_db;

use tbit_db;

CREATE TABLE Fornecedor 
( 
 id_fornecedor INT not null auto_increment,  
 nome_fornecedor varchar(30),  
 cnpj_fornecedor varchar(18),  
 email_fornecedor varchar(40),  
 telefone_fornecedor varchar(20),  
 pais_fornecedor varchar(30),  
 cidade_fornecedor varchar(30),
 constraint pk_fornecedor primary key (id_fornecedor) 
); 

CREATE TABLE Produto 
( 
 id_produto INT not null auto_increment,  
 nome_produto varchar(30),  
 descricao_produto varchar(60),  
 quantidade_produto INT,  
 valor_produto decimal(10,2),  
 idFornecedor INT not null,
 constraint pk_produto primary key (id_produto),
 constraint fk_fornecedor_produto foreign key (idFornecedor) references Fornecedor(id_fornecedor)
); 

CREATE TABLE Cliente 
( 
 id_cliente INT not null auto_increment,  
 nome_cliente varchar(30),  
 descricao_cliente varchar(60),  
 cnpj_cliente varchar(18),
 constraint pk_cliente primary key (id_cliente)
); 

CREATE TABLE Compra 
(
 id_compra int not null auto_increment,
 idProduto int not null,  
 idCliente int not null,
 constraint pk_compra primary key (id_compra),
 constraint fk_produto_compra foreign key (idProduto) references Produto(id_produto),
 constraint fk_cliente_compra foreign key (idCliente) references Cliente(id_cliente)
); 

CREATE TABLE Funcionario 
( 
 id_funcionario INT not null auto_increment,  
 nome_funcionario varchar(30),  
 data_nascimento_funcionario date,  
 data_admissao_funcionario date,  
 cpf_funcionario varchar(14),  
 cidade_funcionario varchar(30),  
 estado_funcionario varchar(30),  
 telefone_funcionario varchar(15),  
 email_funcionario varchar(30),  
 usuario_funcionario varchar(30),  
 senha_funcionario varchar(30),
 constraint pk_funcionario primary key (id_funcionario)
); 

CREATE TABLE Cadastro 
( 
 id_cadastro int not null auto_increment,
 idFuncionario INT not null,  
 idCliente INT not null,
 constraint pk_cadastro primary key (id_cadastro),
 constraint fk_funcionario_cadastro foreign key (idFuncionario) references Funcionario(id_funcionario),
 constraint fk_cliente_cadastro foreign key (idCliente) references Cliente(id_cliente)
); 

create table Administrador
(
	id_administrador int not null auto_increment,
    usuario_administrador varchar(30),
    senha_administrador varchar(30),
    idFuncionario int not null,
    constraint pk_administrador primary key (id_administrador),
    constraint fk_funcionario_administrador foreign key (idFuncionario) references Funcionario(id_funcionario)
);