INSERT INTO Fornecedor (nome_fornecedor, cnpj_fornecedor, email_fornecedor, telefone_fornecedor, pais_fornecedor, cidade_fornecedor) VALUES
('TechParts Brasil', '12.345.678/0001-95', 'contato@techparts.com.br', '+55 (11) 98765-4321', 'Brasil', 'São Paulo'),
('EletroComponentes Ltda', '98.765.432/0001-10', 'vendas@eletrocomp.com', '+55 (21) 91234-5678', 'Brasil', 'Rio de Janeiro'),
('Global Hardware Inc', '23.456.789/0001-45', 'contact@globalhw.com', '+1 (212) 555-0199', 'EUA', 'Nova York'),
('Asian Electronics Co', '87.654.321/0001-33', 'sales@asian-elec.com', '+852 1234 5678', 'China', 'Hong Kong'),
('EuroTech Solutions', '34.567.891/0001-22', 'info@eurotech.eu', '+49 30 12345678', 'Alemanha', 'Berlim'),
('MegaSupply Distribuidora', '45.678.912/0001-88', 'atendimento@megasupply.com.br', '+55 (31) 99876-5432', 'Brasil', 'Belo Horizonte'),
('Componentes Digitais SA', '56.789.123/0001-77', 'sac@compdigital.com', '+55 (51) 98765-1234', 'Brasil', 'Porto Alegre'),
('TecnoImport Ltda', '67.891.234/0001-66', 'tecnocompras@tecnimport.com', '+55 (41) 91234-8765', 'Brasil', 'Curitiba'),
('Quality Parts International', '78.912.345/0001-55', 'quality@qparts.com', '+44 20 7123 4567', 'Reino Unido', 'Londres'),
('Japan Electronic Corp', '89.123.456/0001-44', 'export@jpec.co.jp', '+81 3 1234 5678', 'Japão', 'Tóquio');

INSERT INTO Produto (nome_produto, descricao_produto, quantidade_produto, valor_produto, idFornecedor) VALUES  
('Notebook Dell', 'Notebook i5, 8GB RAM, SSD 256GB', 50, 3500.00, 1),  
('Mouse Logitech', 'Mouse sem fio, 1200DPI', 200, 120.50, 2),  
('Teclado Mecânico', 'Teclado RGB, switches azuis', 80, 299.90, 3),  
('Monitor 24"', 'Monitor Full HD, 75Hz', 30, 899.00, 1),  
('Headphone Sony', 'Fone over-ear, cancelamento de ruído', 40, 450.00, 4),  
('Webcam HD', 'Webcam 1080p, microfone integrado', 60, 250.00, 5),  
('Impressora Laser', 'Impressora monocromática, 20ppm', 25, 1200.00, 2);  

INSERT INTO Cliente (nome_cliente, descricao_cliente, cnpj_cliente) VALUES  
('Empresa Tech Ltda', 'Revenda de equipamentos de informática', '12.345.678/0001-01'),  
('Comércio Digital SA', 'Distribuidor de eletrônicos', '98.765.432/0001-02'),  
('Serviços Rápidos ME', 'Manutenção de hardware', '56.789.012/0001-03'),  
('Loja Virtual Express', 'E-commerce de acessórios', '34.567.890/0001-04'),  
('Consultoria Inovação', 'Soluções em TI para empresas', '78.901.234/0001-05');  

INSERT INTO Funcionario (nome_funcionario, data_nascimento_funcionario, data_admissao_funcionario, cpf_funcionario, cidade_funcionario, estado_funcionario, telefone_funcionario, email_funcionario, usuario_funcionario, senha_funcionario) VALUES  
('João da Silva', '1990-05-15', '2020-03-10', '123.456.789-01', 'São Paulo', 'SP', '(11) 99999-9999', 'joao.silva@empresa.com', 'joao.silva', 'senha123'),  
('Maria Souza', '1985-08-20', '2019-07-22', '987.654.321-02', 'Rio de Janeiro', 'RJ', '(21) 88888-8888', 'maria.souza@empresa.com', 'maria.souza', 'abc456'),  
('Carlos Oliveira', '1992-11-30', '2021-01-05', '456.789.012-03', 'Belo Horizonte', 'MG', '(31) 77777-7777', 'carlos.oliveira@empresa.com', 'carlos.oliv', '789xyz'),  
('Ana Pereira', '1988-04-25', '2022-06-15', '321.654.987-04', 'Curitiba', 'PR', '(41) 66666-6666', 'ana.pereira@empresa.com', 'ana.pereira', 'p@ssw0rd'),  
('Pedro Costa', '1995-07-12', '2023-02-18', '654.321.987-05', 'Porto Alegre', 'RS', '(51) 55555-5555', 'pedro.costa@empresa.com', 'pedro.costa', 'costapwd');  

-- Compra (relaciona Produto e Cliente)  
INSERT INTO Compra (idProduto, idCliente) VALUES  
(1, 1), (2, 2), (3, 3), (4, 4), (5, 5), (6, 1), (7, 2);  

-- Cadastro (relaciona Funcionario e Cliente)  
INSERT INTO Cadastro (idFuncionario, idCliente) VALUES  
(1, 1), (2, 2), (3, 3), (4, 4), (5, 5);  

-- Administrador (relaciona Funcionario)  
INSERT INTO Administrador (usuario_administrador, senha_administrador, idFuncionario) VALUES  
('admin.joao', 'admin123', 1),  
('admin.maria', 'maria456', 2);  