drop database tbit_db;

create database tbit_db;

use tbit_db;

CREATE TABLE Fornecedor 
( 
 id_fornecedor INT not null auto_increment,  
 nome_fornecedor INT,  
 cnpj_fornecedor INT,  
 email_fornecedor INT,  
 telefone_fornecedor INT,  
 pais_fornecedor INT,  
 cidade_fornecedor INT,
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
 constraint fk_id_fornecedor foreign key (idFornecedor) references Fornecedor(id_fornecedor)
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
 id_compra int not null,
 idProduto int not null,  
 idCliente int not null,
 constraint pk_compra primary key (id_compra),
 constraint fk_id_produto foreign key (idProduto) references Produto(id_produto),
 constraint fk_id_cliente foreign key (idCliente) references Cliente(id_cliente)
); 

CREATE TABLE Funcionario 
( 
 id_funcionario INT not null auto_increment,  
 nome_funcionario varchar(30),  
 data_nascimento_funcionario date,  
 data_admissao_funcionario date,  
 cpf_funcionario varchar(14),  
 cidade_funcionario varchar(15),  
 estado_funcionario varchar(15),  
 telefone_funcionario varchar(15),  
 email_funcionario varchar(30),  
 usuario_funcionario varchar(15),  
 senha_funcionario varchar(15),
 constraint pk_funcionario primary key (id_funcionario)
); 

CREATE TABLE Cadastro 
( 
 id_cadastro int not null,
 idFuncionario INT not null,  
 idCliente INT not null,
 constraint pk_cadastro primary key (id_cadastro),
 constraint fk_id_funcionario foreign key (idFuncionario) references Funcionario(id_funcionario),
 constraint fk_cliente_cadastro foreign key (idCliente) references Cliente(id_cliente)
); 
