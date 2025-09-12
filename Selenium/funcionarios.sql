CREATE DATABASE empresa;

USE empresa;

CREATE TABLE funcionarios(
	id INT AUTO_INCREMENT NOT NULL,
    nome_completo VARCHAR(255) NOT NULL,
    data_nascimento DATE NOT NULL,
    data_admissao DATE NOT NULL,
    cpf VARCHAR(40) NOT NULL,
    cidade VARCHAR(80) NOT NULL,
    uf CHAR(2) NOT NULL,
    telefone VARCHAR(40) NOT NULL,
    email VARCHAR(255) NOT NULL,
    usuario VARCHAR(80) NOT NULL,
    senha VARCHAR(80) NOT NULL,
    perfil VARCHAR(30) NOT NULL,
    PRIMARY KEY (id)
);

INSERT INTO funcionarios (nome_completo, data_nascimento, data_admissao, cpf, cidade, uf, telefone, email, usuario, senha, perfil) VALUES
('Lucas Almeida', '1990-04-15', '2019-08-01', '123.456.789-00', 'Curitiba', 'PR', '3001-1234', 'lucas.almeida@gmail.com', 'lucas_almeida', '1234', 'ADM'),
('Mariana Silva', '1987-11-23', '2018-03-12', '987.654.321-11', 'Curitiba', 'PR', '3001-5678', 'mariana.silva@gmail.com', 'mariana_silva', '1234', 'Funcionário'),
('Pedro Santos', '1995-06-30', '2020-05-20', '456.789.123-22', 'Curitiba', 'PR', '3001-9101', 'pedro.santos@gmail.com', 'pedro_santos', '1234', 'ADM'),
('Juliana Costa', '1992-09-14', '2021-07-15', '321.654.987-33', 'Curitiba', 'PR', '3001-1122', 'juliana.costa@gmail.com', 'juliana_costa', '1234', 'Funcionário'),
('Rafael Oliveira', '1989-12-05', '2017-11-30', '654.321.789-44', 'Curitiba', 'PR', '3001-3344', 'rafael.oliveira@gmail.com', 'rafael_oliveira', '1234', 'ADM'),
('Fernanda Lima', '1993-03-22', '2019-02-28', '789.123.456-55', 'Curitiba', 'PR', '3001-5566', 'fernanda.lima@gmail.com', 'fernanda_lima', '1234', 'Funcionário'),
('Gustavo Pereira', '1988-07-18', '2016-09-10', '159.753.486-66', 'Curitiba', 'PR', '3001-7788', 'gustavo.pereira@gmail.com', 'gustavo_pereira', '1234', 'ADM'),
('Larissa Martins', '1991-10-07', '2020-01-05', '357.951.852-77', 'Curitiba', 'PR', '3001-9900', 'larissa.martins@gmail.com', 'larissa_martins', '1234', 'Funcionário'),
('Bruno Fernandes', '1985-05-25', '2015-04-22', '951.753.159-88', 'Curitiba', 'PR', '3001-2233', 'bruno.fernandes@gmail.com', 'bruno_fernandes', '1234', 'ADM');