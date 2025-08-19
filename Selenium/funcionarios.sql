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