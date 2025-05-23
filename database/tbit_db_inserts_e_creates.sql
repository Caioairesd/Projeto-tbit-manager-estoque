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
-- Inserção de dados na tabela Fornecedor (60 registros)
INSERT INTO Fornecedor (nome_fornecedor, cnpj_fornecedor, email_fornecedor, telefone_fornecedor, pais_fornecedor, cidade_fornecedor) VALUES
('TechImport', '12.345.678/0001-01', 'contato@techimport.com.br', '(11) 98765-4321', 'Brasil', 'São Paulo'),
('EletroParts', '23.456.789/0001-02', 'vendas@eletroparts.com', '(21) 99876-5432', 'Brasil', 'Rio de Janeiro'),
('Global Components', '34.567.890/0001-03', 'sales@globalcomp.com', '+1 (555) 123-4567', 'EUA', 'Nova York'),
('Asian Electronics', '45.678.901/0001-04', 'contact@asianelec.com', '+86 10 8765 4321', 'China', 'Xangai'),
('EuroTech', '56.789.012/0001-05', 'info@eurotech.de', '+49 30 12345678', 'Alemanha', 'Berlim'),
('MegaSupply', '67.890.123/0001-06', 'sac@megasupply.com.br', '(31) 91234-5678', 'Brasil', 'Belo Horizonte'),
('Componentes Brasil', '78.901.234/0001-07', 'contato@componentesbr.com', '(51) 98765-4321', 'Brasil', 'Porto Alegre'),
('Digital Import', '89.012.345/0001-08', 'vendas@digitalimport.com', '(41) 99876-5432', 'Brasil', 'Curitiba'),
('TechWorld', '90.123.456/0001-09', 'contact@techworld.com', '+44 20 7946 0958', 'Reino Unido', 'Londres'),
('Future Electronics', '01.234.567/0001-10', 'sales@futurelec.com', '+81 3 1234 5678', 'Japão', 'Tóquio'),
('TechSolutions', '12.345.678/0001-11', 'contato@techsolutions.com', '(11) 91234-5678', 'Brasil', 'Campinas'),
('EletroDist', '23.456.789/0001-12', 'vendas@eletrodist.com', '(19) 98765-4321', 'Brasil', 'São Carlos'),
('Global Tech', '34.567.890/0001-13', 'sales@globaltech.com', '+1 (212) 555-1234', 'EUA', 'Chicago'),
('China Import', '45.678.901/0001-14', 'contact@chinaimport.com', '+86 21 9876 5432', 'China', 'Pequim'),
('German Tech', '56.789.012/0001-15', 'info@germantech.de', '+49 89 9876543', 'Alemanha', 'Munique'),
('MegaTech', '67.890.123/0001-16', 'sac@megatech.com.br', '(31) 92345-6789', 'Brasil', 'Contagem'),
('Componentes RJ', '78.901.234/0001-17', 'contato@componentesrj.com', '(21) 98765-1234', 'Brasil', 'Niterói'),
('Digital Express', '89.012.345/0001-18', 'vendas@digitalexpress.com', '(47) 99876-5432', 'Brasil', 'Joinville'),
('TechEurope', '90.123.456/0001-19', 'contact@techeurope.eu', '+44 20 7123 4567', 'Reino Unido', 'Manchester'),
('Japan Electronics', '01.234.567/0001-20', 'sales@japanelec.com', '+81 6 9876 5432', 'Japão', 'Osaka'),
('TechBrasil', '12.345.678/0001-21', 'contato@techbrasil.com', '(11) 92345-6789', 'Brasil', 'São Bernardo'),
('EletroCenter', '23.456.789/0001-22', 'vendas@eletrocenter.com', '(21) 98765-4321', 'Brasil', 'Nova Iguaçu'),
('US Components', '34.567.890/0001-23', 'sales@uscomponents.com', '+1 (415) 555-9876', 'EUA', 'São Francisco'),
('China Tech', '45.678.901/0001-24', 'contact@chinatech.com', '+86 755 1234 5678', 'China', 'Shenzhen'),
('Berlin Electronics', '56.789.012/0001-25', 'info@berlinelec.de', '+49 30 9876543', 'Alemanha', 'Hamburgo'),
('MegaParts', '67.890.123/0001-26', 'sac@megaparts.com.br', '(31) 93456-7890', 'Brasil', 'Betim'),
('Componentes SP', '78.901.234/0001-27', 'contato@componentessp.com', '(11) 98765-1234', 'Brasil', 'Guarulhos'),
('Digital Plus', '89.012.345/0001-28', 'vendas@digitalplus.com', '(41) 92345-6789', 'Brasil', 'Londrina'),
('TechUK', '90.123.456/0001-29', 'contact@techuk.co.uk', '+44 20 8456 7890', 'Reino Unido', 'Birmingham'),
('Tokyo Electronics', '01.234.567/0001-30', 'sales@tokyoelec.com', '+81 3 9876 5432', 'Japão', 'Yokohama'),
('TechImport SP', '12.345.678/0001-31', 'contato@techimportsp.com', '(11) 93456-7890', 'Brasil', 'Santo André'),
('EletroParts RJ', '23.456.789/0001-32', 'vendas@eletropartsrj.com', '(21) 92345-6789', 'Brasil', 'São Gonçalo'),
('Global Parts', '34.567.890/0001-33', 'sales@globalparts.com', '+1 (305) 555-1234', 'EUA', 'Miami'),
('Shenzhen Import', '45.678.901/0001-34', 'contact@shenzhenimport.com', '+86 755 9876 5432', 'China', 'Guangzhou'),
('Frankfurt Tech', '56.789.012/0001-35', 'info@frankfurttech.de', '+49 69 1234567', 'Alemanha', 'Frankfurt'),
('MegaImport', '67.890.123/0001-36', 'sac@megaimport.com.br', '(31) 94567-8901', 'Brasil', 'Ribeirão das Neves'),
('Componentes MG', '78.901.234/0001-37', 'contato@componentesmg.com', '(31) 98765-1234', 'Brasil', 'Uberlândia'),
('Digital Tech', '89.012.345/0001-38', 'vendas@digitaltech.com', '(41) 93456-7890', 'Brasil', 'Maringá'),
('TechLondon', '90.123.456/0001-39', 'contact@techlondon.co.uk', '+44 20 7234 5678', 'Reino Unido', 'Liverpool'),
('Osaka Electronics', '01.234.567/0001-40', 'sales@osakaelec.com', '+81 6 1234 5678', 'Japão', 'Kyoto'),
('TechImport RJ', '12.345.678/0001-41', 'contato@techimportrj.com', '(21) 93456-7890', 'Brasil', 'Duque de Caxias'),
('EletroParts SP', '23.456.789/0001-42', 'vendas@eletropartssp.com', '(11) 92345-6789', 'Brasil', 'Osasco'),
('US Tech', '34.567.890/0001-43', 'sales@ustech.com', '+1 (713) 555-9876', 'EUA', 'Houston'),
('Beijing Import', '45.678.901/0001-44', 'contact@beijingimport.com', '+86 10 9876 5432', 'China', 'Tianjin'),
('Munich Electronics', '56.789.012/0001-45', 'info@munichelec.de', '+49 89 1234567', 'Alemanha', 'Colônia'),
('MegaDist', '67.890.123/0001-46', 'sac@megadist.com.br', '(31) 95678-9012', 'Brasil', 'Ibirité'),
('Componentes PR', '78.901.234/0001-47', 'contato@componentespr.com', '(41) 98765-1234', 'Brasil', 'Cascavel'),
('Digital World', '89.012.345/0001-48', 'vendas@digitalworld.com', '(41) 94567-8901', 'Brasil', 'Ponta Grossa'),
('TechScotland', '90.123.456/0001-49', 'contact@techscotland.co.uk', '+44 131 456 7890', 'Reino Unido', 'Edimburgo'),
('Nagoya Electronics', '01.234.567/0001-50', 'sales@nagoyaelec.com', '+81 52 9876 5432', 'Japão', 'Nagoya'),
('TechImport MG', '12.345.678/0001-51', 'contato@techimportmg.com', '(31) 93456-7890', 'Brasil', 'Contagem'),
('EletroParts MG', '23.456.789/0001-52', 'vendas@eletropartsmg.com', '(31) 92345-6789', 'Brasil', 'Betim'),
('Texas Components', '34.567.890/0001-53', 'sales@texascomponents.com', '+1 (512) 555-1234', 'EUA', 'Austin'),
('Shanghai Tech', '45.678.901/0001-54', 'contact@shanghaitech.com', '+86 21 1234 5678', 'China', 'Chongqing'),
('Dusseldorf Electronics', '56.789.012/0001-55', 'info@dusseldorfelec.de', '+49 211 9876543', 'Alemanha', 'Dusseldorf'),
('MegaCom', '67.890.123/0001-56', 'sac@megacom.com.br', '(31) 96789-0123', 'Brasil', 'Santa Luzia'),
('Componentes SC', '78.901.234/0001-57', 'contato@componentessc.com', '(48) 98765-1234', 'Brasil', 'São José'),
('Digital Info', '89.012.345/0001-58', 'vendas@digitalinfo.com', '(41) 95678-9012', 'Brasil', 'Colombo'),
('TechWales', '90.123.456/0001-59', 'contact@techwales.co.uk', '+44 29 8765 4321', 'Reino Unido', 'Cardiff'),
('Fukuoka Electronics', '01.234.567/0001-60', 'sales@fukuokaelec.com', '+81 92 9876 5432', 'Japão', 'Fukuoka');

-- Inserção de dados na tabela Cliente (60 registros)
INSERT INTO Cliente (nome_cliente, descricao_cliente, cnpj_cliente) VALUES
('Loja Tech', 'Revenda de equipamentos eletrônicos', '11.111.111/0001-11'),
('Eletro Magazine', 'Rede de varejo de eletrônicos', '22.222.222/0001-22'),
('Informática Express', 'Loja de informática e acessórios', '33.333.333/0001-33'),
('Cell Store', 'Revenda de smartphones e tablets', '44.444.444/0001-44'),
('Office Tech', 'Equipamentos para escritório', '55.555.555/0001-55'),
('Gamer World', 'Especializada em produtos gamer', '66.666.666/0001-66'),
('Casa Digital', 'Eletrônicos para casa inteligente', '77.777.777/0001-77'),
('Tech Solutions', 'Soluções em tecnologia corporativa', '88.888.888/0001-88'),
('Digital Center', 'Shopping virtual de eletrônicos', '99.999.999/0001-99'),
('Connect Store', 'Dispositivos de conectividade', '10.101.010/0001-01'),
('Tech House', 'Eletrônicos para residências', '11.121.212/0001-12'),
('PC Express', 'Montagem e venda de computadores', '12.131.313/0001-13'),
('Mobile Center', 'Especializada em celulares', '13.141.414/0001-14'),
('Audio Visual', 'Equipamentos de áudio e vídeo', '14.151.515/0001-15'),
('Network Solutions', 'Soluções em rede e conectividade', '15.161.616/0001-16'),
('Gadget Store', 'Acessórios e gadgets tecnológicos', '16.171.717/0001-17'),
('Tech Kids', 'Tecnologia educacional para crianças', '17.181.818/0001-18'),
('Digital Office', 'Equipamentos para escritórios digitais', '18.191.919/0001-19'),
('Smart Home', 'Automação residencial', '19.202.020/0001-20'),
('Game Center', 'Loja especializada em games', '20.212.121/0001-21'),
('Tech Plus', 'Variedade em produtos eletrônicos', '21.222.222/0001-22'),
('Notebook Center', 'Especializada em notebooks', '22.232.323/0001-23'),
('Tablet World', 'Variedade em tablets', '23.242.424/0001-24'),
('Peripheral Store', 'Periféricos para computadores', '24.252.525/0001-25'),
('Data Solutions', 'Armazenamento e backup', '25.262.626/0001-26'),
('Security Tech', 'Equipamentos de segurança digital', '26.272.727/0001-27'),
('Photo Video', 'Equipamentos fotográficos e filmagem', '27.282.828/0001-28'),
('VR Experience', 'Realidade virtual e aumentada', '28.292.929/0001-29'),
('Drone Tech', 'Drones e acessórios', '29.303.030/0001-30'),
('Robot Store', 'Robótica e automação', '30.313.131/0001-31'),
('Tech Fashion', 'Tecnologia vestível', '31.323.232/0001-32'),
('Health Tech', 'Tecnologia para saúde', '32.333.333/0001-33'),
('Fitness Tech', 'Tecnologia para fitness', '33.343.434/0001-34'),
('Car Tech', 'Tecnologia automotiva', '34.353.535/0001-35'),
('Travel Tech', 'Tecnologia para viagens', '35.363.636/0001-36'),
('Outdoor Tech', 'Tecnologia para atividades ao ar livre', '36.373.737/0001-37'),
('Kitchen Tech', 'Eletrônicos para cozinha', '37.383.838/0001-38'),
('Bath Tech', 'Tecnologia para banheiros', '38.393.939/0001-39'),
('Bedroom Tech', 'Tecnologia para quartos', '39.404.040/0001-40'),
('Living Tech', 'Tecnologia para salas de estar', '40.414.141/0001-41'),
('Garden Tech', 'Tecnologia para jardins', '41.424.242/0001-42'),
('Pet Tech', 'Tecnologia para pets', '42.434.343/0001-43'),
('Baby Tech', 'Tecnologia para bebês', '43.444.444/0001-44'),
('Senior Tech', 'Tecnologia para idosos', '44.454.545/0001-45'),
('Accessibility Tech', 'Tecnologia para acessibilidade', '45.464.646/0001-46'),
('Green Tech', 'Tecnologia sustentável', '46.474.747/0001-47'),
('Solar Tech', 'Energia solar e tecnologia', '47.484.848/0001-48'),
('Wind Tech', 'Energia eólica e tecnologia', '48.494.949/0001-49'),
('Water Tech', 'Tecnologia para tratamento de água', '49.505.050/0001-50'),
('Air Tech', 'Tecnologia para qualidade do ar', '50.515.151/0001-51'),
('Recycling Tech', 'Tecnologia para reciclagem', '51.525.252/0001-52'),
('Farming Tech', 'Tecnologia para agricultura', '52.535.353/0001-53'),
('Fishing Tech', 'Tecnologia para pesca', '53.545.454/0001-54'),
('Hunting Tech', 'Tecnologia para caça', '54.555.555/0001-55'),
('Camping Tech', 'Tecnologia para camping', '55.565.656/0001-56'),
('Diving Tech', 'Tecnologia para mergulho', '56.575.757/0001-57'),
('Flying Tech', 'Tecnologia para aviação', '57.585.858/0001-58'),
('Space Tech', 'Tecnologia espacial', '58.595.959/0001-59'),
('Future Tech', 'Tecnologias futuras e inovadoras', '59.606.060/0001-60'),
('Loja Exemplo', 'Cliente atacadista do setor têxtil', '12.345.678/0001-90');

-- Inserção de dados na tabela Funcionario (60 registros)
INSERT INTO Funcionario (nome_funcionario, data_nascimento_funcionario, data_admissao_funcionario, cpf_funcionario, cidade_funcionario, estado_funcionario, telefone_funcionario, email_funcionario, usuario_funcionario, senha_funcionario, perfil_funcionario) VALUES
('João Silva', '1985-05-15', '2020-03-10', '111.111.111-11', 'São Paulo', 'SP', '(11) 91234-5678', 'joao.silva@empresa.com', 'joao.silva', 'senha123', 'Administrador'),
('Maria Oliveira', '1990-08-22', '2021-02-15', '222.222.222-22', 'Rio de Janeiro', 'RJ', '(21) 92345-6789', 'maria.oliveira@empresa.com', 'maria.oliveira', 'senha456', 'Administrador'),
('Carlos Souza', '1988-11-30', '2019-07-05', '333.333.333-33', 'Belo Horizonte', 'MG', '(31) 93456-7890', 'carlos.souza@empresa.com', 'carlos.souza', 'senha789', 'Administrador'),
('Ana Costa', '1992-04-18', '2022-01-20', '444.444.444-44', 'Porto Alegre', 'RS', '(51) 94567-8901', 'ana.costa@empresa.com', 'ana.costa', 'senha101', 'Administrador'),
('Pedro Santos', '1983-07-25', '2018-05-12', '555.555.555-55', 'Curitiba', 'PR', '(41) 95678-9012', 'pedro.santos@empresa.com', 'pedro.santos', 'senha112', 'Usuario simples'),
('Juliana Lima', '1995-01-08', '2022-06-30', '666.666.666-66', 'Salvador', 'BA', '(71) 96789-0123', 'juliana.lima@empresa.com', 'juliana.lima', 'senha131', 'Usuario simples'),
('Marcos Pereira', '1980-09-14', '2017-11-15', '777.777.777-77', 'Recife', 'PE', '(81) 97890-1234', 'marcos.pereira@empresa.com', 'marcos.pereira', 'senha415', 'Usuario simples'),
('Fernanda Rocha', '1987-12-03', '2020-09-22', '888.888.888-88', 'Fortaleza', 'CE', '(85) 98901-2345', 'fernanda.rocha@empresa.com', 'fernanda.rocha', 'senha161', 'Usuario simples'),
('Ricardo Alves', '1991-03-27', '2021-04-18', '999.999.999-99', 'Manaus', 'AM', '(92) 99012-3456', 'ricardo.alves@empresa.com', 'ricardo.alves', 'senha718', 'Usuario simples'),
('Patrícia Gomes', '1984-06-09', '2019-08-07', '010.101.010-10', 'Goiânia', 'GO', '(62) 90123-4567', 'patricia.gomes@empresa.com', 'patricia.gomes', 'senha192', 'Usuario simples'),
('Lucas Mendes', '1993-02-20', '2023-01-05', '020.202.020-20', 'Florianópolis', 'SC', '(48) 92345-6789', 'lucas.mendes@empresa.com', 'lucas.mendes', 'senha223', 'Usuario simples'),
('Amanda Ferreira', '1989-05-12', '2021-07-15', '030.303.030-30', 'Vitória', 'ES', '(27) 93456-7890', 'amanda.ferreira@empresa.com', 'amanda.ferreira', 'senha334', 'Usuario simples'),
('Rodrigo Martins', '1982-08-25', '2018-10-30', '040.404.040-40', 'Natal', 'RN', '(84) 94567-8901', 'rodrigo.martins@empresa.com', 'rodrigo.martins', 'senha445', 'Usuario simples'),
('Camila Almeida', '1994-11-18', '2022-03-22', '050.505.050-50', 'João Pessoa', 'PB', '(83) 95678-9012', 'camila.almeida@empresa.com', 'camila.almeida', 'senha556', 'Usuario simples'),
('Gustavo Henrique', '1986-04-30', '2020-06-14', '060.606.060-60', 'Maceió', 'AL', '(82) 96789-0123', 'gustavo.henrique@empresa.com', 'gustavo.henrique', 'senha667', 'Usuario simples'),
('Isabela Santos', '1990-07-22', '2021-09-05', '070.707.070-70', 'Aracaju', 'SE', '(79) 97890-1234', 'isabela.santos@empresa.com', 'isabela.santos', 'senha778', 'Usuario simples'),
('Felipe Oliveira', '1981-10-15', '2017-12-20', '080.808.080-80', 'Teresina', 'PI', '(86) 98901-2345', 'felipe.oliveira@empresa.com', 'felipe.oliveira', 'senha889', 'Usuario simples'),
('Laura Costa', '1996-01-28', '2023-02-10', '090.909.090-90', 'São Luís', 'MA', '(98) 99012-3456', 'laura.costa@empresa.com', 'laura.costa', 'senha990', 'Usuario simples'),
('Rafael Souza', '1983-03-05', '2019-05-25', '101.010.101-01', 'Belém', 'PA', '(91) 90123-4567', 'rafael.souza@empresa.com', 'rafael.souza', 'senha001', 'Usuario simples'),
('Beatriz Lima', '1988-06-17', '2020-08-30', '111.111.111-12', 'Boa Vista', 'RR', '(95) 91234-5678', 'beatriz.lima@empresa.com', 'beatriz.lima', 'senha112', 'Usuario simples'),
('Thiago Pereira', '1992-09-10', '2022-11-15', '121.212.121-21', 'Porto Velho', 'RO', '(69) 92345-6789', 'thiago.pereira@empresa.com', 'thiago.pereira', 'senha123', 'Usuario simples'),
('Vanessa Rocha', '1985-12-23', '2018-02-28', '131.313.131-31', 'Rio Branco', 'AC', '(68) 93456-7890', 'vanessa.rocha@empresa.com', 'vanessa.rocha', 'senha234', 'Usuario simples'),
('Daniel Alves', '1997-02-14', '2023-04-05', '141.414.141-41', 'Macapá', 'AP', '(96) 94567-8901', 'daniel.alves@empresa.com', 'daniel.alves', 'senha345', 'Usuario simples'),
('Carolina Gomes', '1989-05-27', '2021-07-10', '151.515.151-51', 'Palmas', 'TO', '(63) 95678-9012', 'carolina.gomes@empresa.com', 'carolina.gomes', 'senha456', 'Usuario simples'),
('Eduardo Mendes', '1984-08-08', '2019-10-15', '161.616.161-61', 'Campo Grande', 'MS', '(67) 96789-0123', 'eduardo.mendes@empresa.com', 'eduardo.mendes', 'senha567', 'Usuario simples'),
('Tatiane Ferreira', '1991-11-20', '2022-01-25', '171.717.171-71', 'Cuiabá', 'MT', '(65) 97890-1234', 'tatiane.ferreira@empresa.com', 'tatiane.ferreira', 'senha678', 'Usuario simples'),
('Vinícius Martins', '1986-01-03', '2020-03-10', '181.818.181-81', 'Brasília', 'DF', '(61) 98901-2345', 'vinicius.martins@empresa.com', 'vinicius.martins', 'senha789', 'Usuario simples'),
('Priscila Almeida', '1993-04-16', '2023-06-20', '191.919.191-91', 'São Paulo', 'SP', '(11) 99012-3456', 'priscila.almeida@empresa.com', 'priscila.almeida', 'senha890', 'Usuario simples'),
('Roberto Henrique', '1987-07-29', '2020-09-05', '202.020.202-02', 'Rio de Janeiro', 'RJ', '(21) 90123-4567', 'roberto.henrique@empresa.com', 'roberto.henrique', 'senha901', 'Usuario simples'),
('Aline Santos', '1994-10-12', '2022-12-15', '212.121.212-12', 'Belo Horizonte', 'MG', '(31) 91234-5678', 'aline.santos@empresa.com', 'aline.santos', 'senha012', 'Usuario simples'),
('Marcelo Oliveira', '1982-12-25', '2018-02-28', '222.222.222-23', 'Porto Alegre', 'RS', '(51) 92345-6789', 'marcelo.oliveira@empresa.com', 'marcelo.oliveira', 'senha123', 'Usuario simples'),
('Gabriela Costa', '1989-03-08', '2021-05-10', '232.323.232-32', 'Curitiba', 'PR', '(41) 93456-7890', 'gabriela.costa@empresa.com', 'gabriela.costa', 'senha234', 'Usuario simples'),
('Leonardo Souza', '1995-06-21', '2023-08-25', '242.424.242-42', 'Salvador', 'BA', '(71) 94567-8901', 'leonardo.souza@empresa.com', 'leonardo.souza', 'senha345', 'Usuario simples'),
('Fernanda Lima', '1988-09-03', '2020-11-15', '252.525.252-52', 'Recife', 'PE', '(81) 95678-9012', 'fernanda.lima@empresa.com', 'fernanda.lima', 'senha456', 'Usuario simples'),
('Bruno Pereira', '1983-12-16', '2019-02-20', '262.626.262-62', 'Fortaleza', 'CE', '(85) 96789-0123', 'bruno.pereira@empresa.com', 'bruno.pereira', 'senha567', 'Usuario simples'),
('Daniela Rocha', '1990-02-28', '2021-04-05', '272.727.272-72', 'Manaus', 'AM', '(92) 97890-1234', 'daniela.rocha@empresa.com', 'daniela.rocha', 'senha678', 'Usuario simples'),
('Fábio Alves', '1985-05-11', '2020-07-10', '282.828.282-82', 'Goiânia', 'GO', '(62) 98901-2345', 'fabio.alves@empresa.com', 'fabio.alves', 'senha789', 'Usuario simples'),
('Cristina Gomes', '1992-08-24', '2022-10-15', '292.929.292-92', 'Florianópolis', 'SC', '(48) 99012-3456', 'cristina.gomes@empresa.com', 'cristina.gomes', 'senha890', 'Usuario simples'),
('Alexandre Mendes', '1987-11-06', '2020-01-20', '303.030.303-03', 'Vitória', 'ES', '(27) 90123-4567', 'alexandre.mendes@empresa.com', 'alexandre.mendes', 'senha901', 'Usuario simples'),
('Monica Ferreira', '1993-01-19', '2023-03-25', '313.131.313-13', 'Natal', 'RN', '(84) 91234-5678', 'monica.ferreira@empresa.com', 'monica.ferreira', 'senha012', 'Usuario simples'),
('Ricardo Martins', '1986-04-02', '2020-06-05', '323.232.323-23', 'João Pessoa', 'PB', '(83) 92345-6789', 'ricardo.martins@empresa.com', 'ricardo.martins', 'senha123', 'Usuario simples'),
('Patricia Almeida', '1991-07-15', '2021-09-10', '333.333.333-34', 'Maceió', 'AL', '(82) 93456-7890', 'patricia.almeida@empresa.com', 'patricia.almeida', 'senha234', 'Usuario simples'),
('Rodrigo Henrique', '1984-10-28', '2019-12-15', '343.434.343-43', 'Aracaju', 'SE', '(79) 94567-8901', 'rodrigo.henrique@empresa.com', 'rodrigo.henrique', 'senha345', 'Usuario simples'),
('Tatiana Santos', '1996-02-10', '2023-04-20', '353.535.353-53', 'Teresina', 'PI', '(86) 95678-9012', 'tatiana.santos@empresa.com', 'tatiana.santos', 'senha456', 'Usuario simples'),
('Marcos Oliveira', '1989-05-23', '2021-07-05', '363.636.363-63', 'São Luís', 'MA', '(98) 96789-0123', 'marcos.oliveira@empresa.com', 'marcos.oliveira', 'senha567', 'Usuario simples'),
('Juliana Costa', '1994-08-05', '2022-10-10', '373.737.373-73', 'Belém', 'PA', '(91) 97890-1234', 'juliana.costa@empresa.com', 'juliana.costa', 'senha678', 'Usuario simples'),
('Gustavo Souza', '1987-11-18', '2020-01-15', '383.838.383-83', 'Boa Vista', 'RR', '(95) 98901-2345', 'gustavo.souza@empresa.com', 'gustavo.souza', 'senha789', 'Usuario simples'),
('Amanda Lima', '1992-01-31', '2022-03-20', '393.939.393-93', 'Porto Velho', 'RO', '(69) 99012-3456', 'amanda.lima@empresa.com', 'amanda.lima', 'senha890', 'Usuario simples'),
('Carlos Pereira', '1985-04-13', '2020-06-25', '404.040.404-04', 'Rio Branco', 'AC', '(68) 90123-4567', 'carlos.pereira@empresa.com', 'carlos.pereira', 'senha901', 'Usuario simples'),
('Luciana Rocha', '1990-07-26', '2021-09-05', '414.141.414-14', 'Macapá', 'AP', '(96) 91234-5678', 'luciana.rocha@empresa.com', 'luciana.rocha', 'senha012', 'Usuario simples'),
('Felipe Alves', '1983-10-08', '2018-12-10', '424.242.424-24', 'Palmas', 'TO', '(63) 92345-6789', 'felipe.alves@empresa.com', 'felipe.alves', 'senha123', 'Usuario simples'),
('Vanessa Gomes', '1996-01-21', '2023-03-15', '434.343.434-34', 'Campo Grande', 'MS', '(67) 93456-7890', 'vanessa.gomes@empresa.com', 'vanessa.gomes', 'senha234', 'Usuario simples'),
('Rafael Mendes', '1988-04-03', '2020-06-20', '444.444.444-45', 'Cuiabá', 'MT', '(65) 94567-8901', 'rafael.mendes@empresa.com', 'rafael.mendes', 'senha345', 'Usuario simples'),
('Camila Ferreira', '1993-07-16', '2022-09-25', '454.545.454-54', 'Brasília', 'DF', '(61) 95678-9012', 'camila.ferreira@empresa.com', 'camila.ferreira', 'senha456', 'Usuario simples'),
('Thiago Martins', '1986-10-29', '2020-12-05', '464.646.464-64', 'São Paulo', 'SP', '(11) 96789-0123', 'thiago.martins@empresa.com', 'thiago.martins', 'senha567', 'Usuario simples'),
('Isabela Almeida', '1991-01-11', '2022-03-10', '474.747.474-74', 'Rio de Janeiro', 'RJ', '(21) 97890-1234', 'isabela.almeida@empresa.com', 'isabela.almeida', 'senha678', 'Usuario simples'),
('Lucas Henrique', '1984-03-24', '2019-05-15', '484.848.484-84', 'Belo Horizonte', 'MG', '(31) 98901-2345', 'lucas.henrique@empresa.com', 'lucas.henrique', 'senha789', 'Usuario simples'),
('Laura Santos', '1997-06-06', '2023-08-20', '494.949.494-94', 'Porto Alegre', 'RS', '(51) 99012-3456', 'laura.santos@empresa.com', 'laura.santos', 'senha890', 'Usuario simples'),
('Eduardo Oliveira', '1990-09-19', '2021-11-25', '505.050.505-05', 'Curitiba', 'PR', '(41) 90123-4567', 'eduardo.oliveira@empresa.com', 'eduardo.oliveira', 'senha901', 'Usuario simples'),
('Beatriz Costa', '1985-12-02', '2020-02-05', '515.151.515-15', 'Salvador', 'BA', '(71) 91234-5678', 'beatriz.costa@empresa.com', 'beatriz.costa', 'senha012', 'Usuario simples');

-- Inserção de dados na tabela Produto (60 registros)
INSERT INTO Produto (id_produto, nome_produto, descricao_produto, categoria_produto, quantidade_produto, valor_produto, idFornecedor) VALUES
(1, 'Notebook Dell', 'Notebook Dell Inspiron 15 i5 8GB 256GB SSD', 'Notebooks', 90, 3499.90, 1),
(2, 'Mouse Logitech', 'Mouse sem fio Logitech M170', 'Periféricos', 238, 79.90, 2),
(3, 'Teclado Mecânico', 'Teclado mecânico Redragon Kumara', 'Teclados', 67, 279.90, 3),
(4, 'Monitor 24\"', 'Monitor LG 24\" Full HD IPS', 'Monitores', 52, 899.90, 4),
(5, 'SSD 480GB', 'SSD Kingston 480GB SATA', 'Armazenamento', 145, 249.90, 5),
(6, 'Smartphone Samsung', 'Samsung Galaxy A54 128GB', 'Smartphones', 74, 1899.90, 6),
(7, 'Tablet Amazon', 'Fire HD 10 32GB', 'Tablets', 53, 999.90, 7),
(8, 'Impressora HP', 'Impressora HP DeskJet 2776', 'Impressoras', 42, 499.90, 8),
(9, 'Headphone Sony', 'Fone de ouvido Sony WH-CH510', 'Fones', 112, 199.90, 9),
(10, 'Webcam Logitech', 'Webcam Logitech C920 HD Pro', 'Periféricos', 82, 399.90, 10),
(11, 'Roteador TP-Link', 'Roteador Wi-Fi TP-Link Archer C6', 'Rede', 102, 299.90, 11),
(12, 'HD Externo Seagate', 'HD Externo Seagate 1TB USB 3.0', 'Armazenamento', 72, 349.90, 12),
(13, 'Pendrive Kingston', 'Pendrive Kingston 64GB USB 3.0', 'Armazenamento', 192, 59.90, 13),
(14, 'Placa de Vídeo GTX 1650', 'Placa de vídeo GTX 1650 GDDR6', 'Placas de Vídeo', 22, 1299.90, 14),
(15, 'Processador Intel i5 10ª geração', 'Processador Intel Core i5 10400F', 'Processadores', 42, 999.90, 15),
(16, 'Placa-Mãe ATX LGA 1200', 'Placa-mãe ATX LGA 1200 para Intel', 'Placas-Mãe', 32, 699.90, 16),
(17, 'Memória RAM DDR4 8GB', 'Memória RAM 8GB DDR4 3200MHz', 'Memória RAM', 112, 199.90, 17),
(18, 'SSD NVMe 500GB', 'SSD NVMe 500GB PCIe Gen3', 'Armazenamento', 72, 349.90, 18),
(19, 'Fonte ATX 500W 80 Plus', 'Fonte ATX 500W certificada', 'Fontes de Alimentação', 52, 299.90, 19),
(20, 'Gabinete Gamer com RGB', 'Gabinete gamer ATX com iluminação RGB', 'Gabinetes', 42, 399.90, 20),
(21, 'Water Cooler 240mm', 'Water cooler para processador', 'Coolers', 28, 349.90, 21),
(22, 'Mouse Gamer Redragon Cobra', 'Mouse gamer Redragon Cobra', 'Periféricos', 82, 159.90, 22),
(23, 'Teclado Gamer Redragon Kumara', 'Teclado gamer Redragon Kumara', 'Teclados', 72, 279.90, 23),
(24, 'Monitor Gamer 24\" 144Hz', 'Monitor Gamer 24\" 144Hz', 'Monitores', 36, 1299.90, 24),
(25, 'Headset Gamer', 'Headset gamer com microfone', 'Audio e Som', 92, 199.90, 25),
(26, 'Mousepad RGB', 'Mousepad gamer com iluminação RGB', 'Periféricos', 62, 89.90, 26),
(37, 'Webcam Gamer', 'Webcam gamer Full HD', 'Periféricos', 42, 349.90, 37),
(38, 'Controle Bluetooth', 'Controle Bluetooth para PC/Android', 'Acessórios', 72, 149.90, 38),
(39, 'Joystick Gamer', 'Joystick gamer sem fio', 'Acessórios', 52, 229.90, 39),
(40, 'Volante Gamer', 'Volante gamer com pedal', 'Acessórios', 12, 799.90, 40),
(41, 'SSD NVMe', 'SSD NVMe 500GB PCIe Gen3', 'Armazenamento', 72, 349.90, 41),
(42, 'Memória RAM', 'Memória RAM 8GB DDR4 3200MHz', 'Memória RAM', 112, 199.90, 42),
(43, 'Placa de Vídeo RTX 3060', 'Placa de vídeo NVIDIA RTX 3060', 'Placas de Vídeo', 30, 2499.90, 43),
(44, 'Processador Ryzen 5 5600X', 'Processador AMD Ryzen 5 5600X', 'Processadores', 55, 1099.90, 44),
(45, 'Placa-Mãe B550', 'Placa-Mãe B550 compatível com Ryzen', 'Placas-Mãe', 40, 799.90, 45),
(46, 'Fonte ATX 750W Modular', 'Fonte ATX 750W Modular 80 Plus Gold', 'Fontes de Alimentação', 47, 599.90, 46),
(47, 'Water Cooler 360mm', 'Water Cooler 360mm para Overclock', 'Resfriamento', 25, 499.90, 47),
(48, 'Gabinete Full-Tower', 'Gabinete Full-Tower com vidro temperado', 'Gabinetes', 33, 699.90, 48),
(49, 'Hub USB-C', 'Hub USB-C 7 em 1', 'Redes e Conectividade', 72, 179.90, 49),
(50, 'Carregador Wireless', 'Carregador wireless 10W', 'Energia', 92, 119.90, 50),
(51, 'Cabo Lightning', 'Cabo Lightning original 1m', 'Cabos e Conectividade', 152, 89.90, 51),
(52, 'Capa para Notebook', 'Capa para notebook 15.6\"', 'Acessórios', 112, 49.90, 52),
(53, 'Suporte para Tablet', 'Suporte ajustável para tablet', 'Móveis e Suportes', 82, 39.90, 53),
(54, 'Estação de Docking', 'Estação de docking USB-C', 'Redes e Conectividade', 52, 299.90, 54),
(55, 'Scanner de Documentos', 'Scanner portátil de documentos', 'Impressão e Digitalização', 32, 499.90, 55),
(56, 'Leitor de Cartão', 'Leitor de cartão SD/CF', 'Acessórios', 92, 59.90, 56),
(57, 'Projetor Mini', 'Projetor mini portátil', 'Monitores', 22, 699.90, 57),
(58, 'TV Box Android', 'TV Box Android 4GB RAM', 'Monitores', 72, 299.90, 58),
(59, 'Controle Remoto', 'Controle remoto universal', 'Acessórios', 132, 49.90, 59),
(60, 'Antena Digital', 'Antena digital interna', 'Redes e Conectividade', 102, 79.90, 60);

-- Inserção de dados na tabela Pedido (60 registros)
INSERT INTO Pedido (nota_fiscal, data_pedido, forma_pagamento, quantidade_produto_item, idProduto, idCliente) VALUES
('NF1001', '2023-01-05', 'Cartão Crédito', 2, 1, 1),
('NF1002', '2023-01-10', 'Boleto', 5, 2, 2),
('NF1003', '2023-01-15', 'PIX', 1, 3, 3),
('NF1004', '2023-01-20', 'Cartão Débito', 3, 4, 4),
('NF1005', '2023-01-25', 'Cartão Crédito', 2, 5, 5),
('NF1006', '2023-02-01', 'Boleto', 4, 6, 6),
('NF1007', '2023-02-05', 'PIX', 1, 7, 7),
('NF1008', '2023-02-10', 'Cartão Débito', 2, 8, 8),
('NF1009', '2023-02-15', 'Cartão Crédito', 3, 9, 9),
('NF1010', '2023-02-20', 'Boleto', 1, 10, 10),
('NF1011', '2023-02-25', 'PIX', 2, 11, 11),
('NF1012', '2023-03-01', 'Cartão Débito', 1, 12, 12),
('NF1013', '2023-03-05', 'Cartão Crédito', 4, 13, 13),
('NF1014', '2023-03-10', 'Boleto', 2, 14, 14),
('NF1015', '2023-03-15', 'PIX', 1, 15, 15),
('NF1016', '2023-03-20', 'Cartão Débito', 3, 16, 16),
('NF1017', '2023-03-25', 'Cartão Crédito', 2, 17, 17),
('NF1018', '2023-04-01', 'Boleto', 1, 18, 18),
('NF1019', '2023-04-05', 'PIX', 5, 19, 19),
('NF1020', '2023-04-10', 'Cartão Débito', 2, 20, 20),
('NF1021', '2023-04-15', 'Cartão Crédito', 1, 21, 21),
('NF1022', '2023-04-20', 'Boleto', 3, 22, 22),
('NF1023', '2023-04-25', 'PIX', 2, 23, 23),
('NF1024', '2023-05-01', 'Cartão Débito', 1, 24, 24),
('NF1025', '2023-05-05', 'Cartão Crédito', 4, 25, 25),
('NF1026', '2023-05-10', 'Boleto', 2, 26, 26),
('NF1027', '2023-05-15', 'PIX', 1, 27, 27),
('NF1028', '2023-05-20', 'Cartão Débito', 3, 28, 28),
('NF1029', '2023-05-25', 'Cartão Crédito', 2, 29, 29),
('NF1030', '2023-06-01', 'Boleto', 1, 30, 30),
('NF1031', '2023-06-05', 'PIX', 2, 31, 31),
('NF1032', '2023-06-10', 'Cartão Débito', 1, 32, 32),
('NF1033', '2023-06-15', 'Cartão Crédito', 3, 33, 33),
('NF1034', '2023-06-20', 'Boleto', 2, 34, 34),
('NF1035', '2023-06-25', 'PIX', 1, 35, 35),
('NF1036', '2023-07-01', 'Cartão Débito', 4, 36, 36),
('NF1037', '2023-07-05', 'Cartão Crédito', 2, 37, 37),
('NF1038', '2023-07-10', 'Boleto', 1, 38, 38),
('NF1039', '2023-07-15', 'PIX', 3, 39, 39),
('NF1040', '2023-07-20', 'Cartão Débito', 2, 40, 40),
('NF1041', '2023-07-25', 'Cartão Crédito', 1, 41, 41),
('NF1042', '2023-08-01', 'Boleto', 5, 42, 42),
('NF1043', '2023-08-05', 'PIX', 2, 43, 43),
('NF1044', '2023-08-10', 'Cartão Débito', 1, 44, 44),
('NF1045', '2023-08-15', 'Cartão Crédito', 3, 45, 45),
('NF1046', '2023-08-20', 'Boleto', 2, 46, 46),
('NF1047', '2023-08-25', 'PIX', 1, 47, 47),
('NF1048', '2023-09-01', 'Cartão Débito', 4, 48, 48),
('NF1049', '2023-09-05', 'Cartão Crédito', 2, 49, 49),
('NF1050', '2023-09-10', 'Boleto', 1, 50, 50),
('NF1051', '2023-09-15', 'PIX', 3, 51, 51),
('NF1052', '2023-09-20', 'Cartão Débito', 2, 52, 52),
('NF1053', '2023-09-25', 'Cartão Crédito', 1, 53, 53),
('NF1054', '2023-10-01', 'Boleto', 5, 54, 54),
('NF1055', '2023-10-05', 'PIX', 2, 55, 55),
('NF1056', '2023-10-10', 'Cartão Débito', 1, 56, 56),
('NF1057', '2023-10-15', 'Cartão Crédito', 3, 57, 57),
('NF1058', '2023-10-20', 'Boleto', 2, 58, 58),
('NF1059', '2023-10-25', 'PIX', 1, 59, 59),
('NF1060', '2023-11-01', 'Cartão Débito', 4, 60, 60);

-- Inserção de dados na tabela Cadastro (60 registros)
INSERT INTO Cadastro (idFuncionario, idCliente) VALUES
(1, 1), (2, 2), (3, 3), (4, 4), (5, 5), (6, 6), (7, 7), (8, 8), (9, 9), (10, 10),
(11, 11), (12, 12), (13, 13), (14, 14), (15, 15), (16, 16), (17, 17), (18, 18), (19, 19), (20, 20),
(21, 21), (22, 22), (23, 23), (24, 24), (25, 25), (26, 26), (27, 27), (28, 28), (29, 29), (30, 30),
(31, 31), (32, 32), (33, 33), (34, 34), (35, 35), (36, 36), (37, 37), (38, 38), (39, 39), (40, 40),
(41, 41), (42, 42), (43, 43), (44, 44), (45, 45), (46, 46), (47, 47), (48, 48), (49, 49), (50, 50),
(51, 51), (52, 52), (53, 53), (54, 54), (55, 55), (56, 56), (57, 57), (58, 58), (59, 59), (60, 60);

-- Inserção de dados na tabela Estoque (60 registros)
INSERT INTO Estoque (IdProduto, quantidade_estoque) VALUES
(1, 30), (2, 80), (3, 20), (4, 15), (5, 50), (6, 25), (7, 18), (8, 12), (9, 40), (10, 30),
(11, 35), (12, 25), (13, 70), (14, 18), (15, 150), (16, 50), (17, 40), (18, 30), (19, 35), (20, 20),
(21, 45), (22, 25), (23, 15), (24, 60), (25, 40), (26, 30), (27, 8), (28, 12), (29, 45), (30, 18),
(31, 10), (32, 30), (33, 25), (34, 12), (35, 35), (36, 20), (37, 15), (38, 25), (39, 18), (40, 5),
(41, 25), (42, 40), (43, 8), (44, 15), (45, 10), (46, 18), (47, 15), (48, 10), (49, 25), (50, 35),
(51, 60), (52, 40), (53, 30), (54, 18), (55, 12), (56, 35), (57, 8), (58, 25), (59, 50), (60, 40);