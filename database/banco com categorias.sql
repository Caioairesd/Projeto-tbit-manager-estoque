-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Tempo de geração: 16/05/2025 às 03:10
-- Versão do servidor: 10.4.32-MariaDB
-- Versão do PHP: 8.2.12

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";

CREATE DATABASE IF NOT EXISTS tbit_db;

USE tbit_db;

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Banco de dados: `tbit_db`
--

DELIMITER $$
--
-- Procedimentos
--
CREATE DEFINER=`root`@`localhost` PROCEDURE `delete_fornecedor_e_produtos` (`IDfornecedor` INT)   BEGIN

    DELETE FROM Pedido
    WHERE idProduto IN (SELECT id_produto FROM Produto WHERE idFornecedor = IDfornecedor);

    DELETE FROM Produto
    WHERE idFornecedor = IDfornecedor;

    DELETE FROM Fornecedor
    WHERE id_fornecedor = IDfornecedor;
END$$

DELIMITER ;

-- --------------------------------------------------------

--
-- Estrutura para tabela `cadastro`
--

CREATE TABLE `cadastro` (
  `id_cadastro` int(11) NOT NULL,
  `idFuncionario` int(11) NOT NULL,
  `idCliente` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Despejando dados para a tabela `cadastro`
--

INSERT INTO `cadastro` (`id_cadastro`, `idFuncionario`, `idCliente`) VALUES
(1, 1, 1),
(2, 2, 2),
(3, 3, 3),
(4, 4, 4),
(5, 5, 5),
(6, 6, 6),
(7, 7, 7),
(8, 8, 8),
(9, 9, 9),
(10, 10, 10),
(11, 11, 11),
(12, 12, 12),
(13, 13, 13),
(14, 14, 14),
(15, 15, 15),
(16, 16, 16),
(17, 17, 17),
(18, 18, 18),
(19, 19, 19),
(20, 20, 20),
(21, 21, 21),
(22, 22, 22),
(23, 23, 23),
(24, 24, 24),
(25, 25, 25),
(26, 26, 26),
(27, 27, 27),
(28, 28, 28),
(29, 29, 29),
(30, 30, 30),
(31, 31, 31),
(32, 32, 32),
(33, 33, 33),
(34, 34, 34),
(35, 35, 35),
(36, 36, 36),
(37, 37, 37),
(38, 38, 38),
(39, 39, 39),
(40, 40, 40),
(41, 41, 41),
(42, 42, 42),
(43, 43, 43),
(44, 44, 44),
(45, 45, 45),
(46, 46, 46),
(47, 47, 47),
(48, 48, 48),
(49, 49, 49),
(50, 50, 50),
(51, 51, 51),
(52, 52, 52),
(53, 53, 53),
(54, 54, 54),
(55, 55, 55),
(56, 56, 56),
(57, 57, 57),
(58, 58, 58),
(59, 59, 59),
(60, 60, 60);

-- --------------------------------------------------------

--
-- Estrutura para tabela `cliente`
--

CREATE TABLE `cliente` (
  `id_cliente` int(11) NOT NULL,
  `nome_cliente` varchar(40) DEFAULT NULL,
  `descricao_cliente` varchar(200) DEFAULT NULL,
  `cnpj_cliente` varchar(18) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Despejando dados para a tabela `cliente`
--

INSERT INTO `cliente` (`id_cliente`, `nome_cliente`, `descricao_cliente`, `cnpj_cliente`) VALUES
(1, 'Loja Tech', 'Revenda de equipamentos eletrônicos', '11.111.111/0001-11'),
(2, 'Eletro Magazine', 'Rede de varejo de eletrônicos', '22.222.222/0001-22'),
(3, 'Informática Express', 'Loja de informática e acessórios', '33.333.333/0001-33'),
(4, 'Cell Store', 'Revenda de smartphones e tablets', '44.444.444/0001-44'),
(5, 'Office Tech', 'Equipamentos para escritório', '55.555.555/0001-55'),
(6, 'Gamer World', 'Especializada em produtos gamer', '66.666.666/0001-66'),
(7, 'Casa Digital', 'Eletrônicos para casa inteligente', '77.777.777/0001-77'),
(8, 'Tech Solutions', 'Soluções em tecnologia corporativa', '88.888.888/0001-88'),
(9, 'Digital Center', 'Shopping virtual de eletrônicos', '99.999.999/0001-99'),
(10, 'Connect Store', 'Dispositivos de conectividade', '10.101.010/0001-01'),
(11, 'Tech House', 'Eletrônicos para residências', '11.121.212/0001-12'),
(12, 'PC Express', 'Montagem e venda de computadores', '12.131.313/0001-13'),
(13, 'Mobile Center', 'Especializada em celulares', '13.141.414/0001-14'),
(14, 'Audio Visual', 'Equipamentos de áudio e vídeo', '14.151.515/0001-15'),
(15, 'Network Solutions', 'Soluções em rede e conectividade', '15.161.616/0001-16'),
(16, 'Gadget Store', 'Acessórios e gadgets tecnológicos', '16.171.717/0001-17'),
(17, 'Tech Kids', 'Tecnologia educacional para crianças', '17.181.818/0001-18'),
(18, 'Digital Office', 'Equipamentos para escritórios digitais', '18.191.919/0001-19'),
(19, 'Smart Home', 'Automação residencial', '19.202.020/0001-20'),
(20, 'Game Center', 'Loja especializada em games', '20.212.121/0001-21'),
(21, 'Tech Plus', 'Variedade em produtos eletrônicos', '21.222.222/0001-22'),
(22, 'Notebook Center', 'Especializada em notebooks', '22.232.323/0001-23'),
(23, 'Tablet World', 'Variedade em tablets', '23.242.424/0001-24'),
(24, 'Peripheral Store', 'Periféricos para computadores', '24.252.525/0001-25'),
(25, 'Data Solutions', 'Armazenamento e backup', '25.262.626/0001-26'),
(26, 'Security Tech', 'Equipamentos de segurança digital', '26.272.727/0001-27'),
(27, 'Photo Video', 'Equipamentos fotográficos e filmagem', '27.282.828/0001-28'),
(28, 'VR Experience', 'Realidade virtual e aumentada', '28.292.929/0001-29'),
(29, 'Drone Tech', 'Drones e acessórios', '29.303.030/0001-30'),
(30, 'Robot Store', 'Robótica e automação', '30.313.131/0001-31'),
(31, 'Tech Fashion', 'Tecnologia vestível', '31.323.232/0001-32'),
(32, 'Health Tech', 'Tecnologia para saúde', '32.333.333/0001-33'),
(33, 'Fitness Tech', 'Tecnologia para fitness', '33.343.434/0001-34'),
(34, 'Car Tech', 'Tecnologia automotiva', '34.353.535/0001-35'),
(35, 'Travel Tech', 'Tecnologia para viagens', '35.363.636/0001-36'),
(36, 'Outdoor Tech', 'Tecnologia para atividades ao ar livre', '36.373.737/0001-37'),
(37, 'Kitchen Tech', 'Eletrônicos para cozinha', '37.383.838/0001-38'),
(38, 'Bath Tech', 'Tecnologia para banheiros', '38.393.939/0001-39'),
(39, 'Bedroom Tech', 'Tecnologia para quartos', '39.404.040/0001-40'),
(40, 'Living Tech', 'Tecnologia para salas de estar', '40.414.141/0001-41'),
(41, 'Garden Tech', 'Tecnologia para jardins', '41.424.242/0001-42'),
(42, 'Pet Tech', 'Tecnologia para pets', '42.434.343/0001-43'),
(43, 'Baby Tech', 'Tecnologia para bebês', '43.444.444/0001-44'),
(44, 'Senior Tech', 'Tecnologia para idosos', '44.454.545/0001-45'),
(45, 'Accessibility Tech', 'Tecnologia para acessibilidade', '45.464.646/0001-46'),
(46, 'Green Tech', 'Tecnologia sustentável', '46.474.747/0001-47'),
(47, 'Solar Tech', 'Energia solar e tecnologia', '47.484.848/0001-48'),
(48, 'Wind Tech', 'Energia eólica e tecnologia', '48.494.949/0001-49'),
(49, 'Water Tech', 'Tecnologia para tratamento de água', '49.505.050/0001-50'),
(50, 'Air Tech', 'Tecnologia para qualidade do ar', '50.515.151/0001-51'),
(51, 'Recycling Tech', 'Tecnologia para reciclagem', '51.525.252/0001-52'),
(52, 'Farming Tech', 'Tecnologia para agricultura', '52.535.353/0001-53'),
(53, 'Fishing Tech', 'Tecnologia para pesca', '53.545.454/0001-54'),
(54, 'Hunting Tech', 'Tecnologia para caça', '54.555.555/0001-55'),
(55, 'Camping Tech', 'Tecnologia para camping', '55.565.656/0001-56'),
(56, 'Diving Tech', 'Tecnologia para mergulho', '56.575.757/0001-57'),
(57, 'Flying Tech', 'Tecnologia para aviação', '57.585.858/0001-58'),
(58, 'Space Tech', 'Tecnologia espacial', '58.595.959/0001-59'),
(59, 'Future Tech', 'Tecnologias futuras e inovadoras', '59.606.060/0001-60'),
(60, 'Loja Exemplo', 'Cliente atacadista do setor têxtil', '12.345.678/0001-90');

-- --------------------------------------------------------

--
-- Estrutura para tabela `estoque`
--

CREATE TABLE `estoque` (
  `id_estoque` int(11) NOT NULL,
  `IdProduto` int(11) NOT NULL,
  `quantidade_estoque` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Despejando dados para a tabela `estoque`
--

INSERT INTO `estoque` (`id_estoque`, `IdProduto`, `quantidade_estoque`) VALUES
(1, 1, 50),
(2, 2, 120),
(3, 3, 35),
(4, 4, 28),
(5, 5, 75),
(6, 6, 40),
(7, 7, 30),
(8, 8, 25),
(9, 9, 60),
(10, 10, 45),
(11, 11, 55),
(12, 12, 40),
(13, 13, 100),
(14, 14, 30),
(15, 15, 200),
(16, 16, 80),
(17, 17, 60),
(18, 18, 45),
(19, 19, 50),
(20, 20, 35),
(21, 21, 70),
(22, 22, 40),
(23, 23, 25),
(24, 24, 90),
(25, 25, 60),
(26, 26, 50),
(27, 27, 15),
(28, 28, 20),
(29, 29, 65),
(30, 30, 30),
(31, 31, 18),
(32, 32, 45),
(33, 33, 40),
(34, 34, 22),
(35, 35, 50),
(36, 36, 35),
(37, 37, 25),
(38, 38, 40),
(39, 39, 30),
(40, 40, 10),
(41, 41, 40),
(42, 42, 60),
(43, 43, 15),
(44, 44, 25),
(45, 45, 20),
(46, 46, 30),
(47, 47, 25),
(48, 48, 18),
(49, 49, 40),
(50, 50, 50),
(51, 51, 80),
(52, 52, 60),
(53, 53, 45),
(54, 54, 30),
(55, 55, 20),
(56, 56, 50),
(57, 57, 15),
(58, 58, 40),
(59, 59, 70),
(60, 60, 60);

--
-- Acionadores `estoque`
--
DELIMITER $$
CREATE TRIGGER `reabastecer_estoque` AFTER INSERT ON `estoque` FOR EACH ROW begin
    update Produto
    set quantidade_produto = quantidade_produto + new.quantidade_estoque
    where id_produto = new.IdProduto;
end
$$
DELIMITER ;

-- --------------------------------------------------------

--
-- Estrutura para tabela `fornecedor`
--

CREATE TABLE `fornecedor` (
  `id_fornecedor` int(11) NOT NULL,
  `nome_fornecedor` varchar(40) DEFAULT NULL,
  `cnpj_fornecedor` varchar(18) DEFAULT NULL,
  `email_fornecedor` varchar(50) DEFAULT NULL,
  `telefone_fornecedor` varchar(20) DEFAULT NULL,
  `pais_fornecedor` varchar(30) DEFAULT NULL,
  `cidade_fornecedor` varchar(30) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Despejando dados para a tabela `fornecedor`
--

INSERT INTO `fornecedor` (`id_fornecedor`, `nome_fornecedor`, `cnpj_fornecedor`, `email_fornecedor`, `telefone_fornecedor`, `pais_fornecedor`, `cidade_fornecedor`) VALUES
(1, 'TechImport', '12.345.678/0001-01', 'contato@techimport.com.br', '(11) 98765-4321', 'Brasil', 'São Paulo'),
(2, 'EletroParts', '23.456.789/0001-02', 'vendas@eletroparts.com', '(21) 99876-5432', 'Brasil', 'Rio de Janeiro'),
(3, 'Global Components', '34.567.890/0001-03', 'sales@globalcomp.com', '+1 (555) 123-4567', 'EUA', 'Nova York'),
(4, 'Asian Electronics', '45.678.901/0001-04', 'contact@asianelec.com', '+86 10 8765 4321', 'China', 'Xangai'),
(5, 'EuroTech', '56.789.012/0001-05', 'info@eurotech.de', '+49 30 12345678', 'Alemanha', 'Berlim'),
(6, 'MegaSupply', '67.890.123/0001-06', 'sac@megasupply.com.br', '(31) 91234-5678', 'Brasil', 'Belo Horizonte'),
(7, 'Componentes Brasil', '78.901.234/0001-07', 'contato@componentesbr.com', '(51) 98765-4321', 'Brasil', 'Porto Alegre'),
(8, 'Digital Import', '89.012.345/0001-08', 'vendas@digitalimport.com', '(41) 99876-5432', 'Brasil', 'Curitiba'),
(9, 'TechWorld', '90.123.456/0001-09', 'contact@techworld.com', '+44 20 7946 0958', 'Reino Unido', 'Londres'),
(10, 'Future Electronics', '01.234.567/0001-10', 'sales@futurelec.com', '+81 3 1234 5678', 'Japão', 'Tóquio'),
(11, 'TechSolutions', '12.345.678/0001-11', 'contato@techsolutions.com', '(11) 91234-5678', 'Brasil', 'Campinas'),
(12, 'EletroDist', '23.456.789/0001-12', 'vendas@eletrodist.com', '(19) 98765-4321', 'Brasil', 'São Carlos'),
(13, 'Global Tech', '34.567.890/0001-13', 'sales@globaltech.com', '+1 (212) 555-1234', 'EUA', 'Chicago'),
(14, 'China Import', '45.678.901/0001-14', 'contact@chinaimport.com', '+86 21 9876 5432', 'China', 'Pequim'),
(15, 'German Tech', '56.789.012/0001-15', 'info@germantech.de', '+49 89 9876543', 'Alemanha', 'Munique'),
(16, 'MegaTech', '67.890.123/0001-16', 'sac@megatech.com.br', '(31) 92345-6789', 'Brasil', 'Contagem'),
(17, 'Componentes RJ', '78.901.234/0001-17', 'contato@componentesrj.com', '(21) 98765-1234', 'Brasil', 'Niterói'),
(18, 'Digital Express', '89.012.345/0001-18', 'vendas@digitalexpress.com', '(47) 99876-5432', 'Brasil', 'Joinville'),
(19, 'TechEurope', '90.123.456/0001-19', 'contact@techeurope.eu', '+44 20 7123 4567', 'Reino Unido', 'Manchester'),
(20, 'Japan Electronics', '01.234.567/0001-20', 'sales@japanelec.com', '+81 6 9876 5432', 'Japão', 'Osaka'),
(21, 'TechBrasil', '12.345.678/0001-21', 'contato@techbrasil.com', '(11) 92345-6789', 'Brasil', 'São Bernardo'),
(22, 'EletroCenter', '23.456.789/0001-22', 'vendas@eletrocenter.com', '(21) 98765-4321', 'Brasil', 'Nova Iguaçu'),
(23, 'US Components', '34.567.890/0001-23', 'sales@uscomponents.com', '+1 (415) 555-9876', 'EUA', 'São Francisco'),
(24, 'China Tech', '45.678.901/0001-24', 'contact@chinatech.com', '+86 755 1234 5678', 'China', 'Shenzhen'),
(25, 'Berlin Electronics', '56.789.012/0001-25', 'info@berlinelec.de', '+49 30 9876543', 'Alemanha', 'Hamburgo'),
(26, 'MegaParts', '67.890.123/0001-26', 'sac@megaparts.com.br', '(31) 93456-7890', 'Brasil', 'Betim'),
(27, 'Componentes SP', '78.901.234/0001-27', 'contato@componentessp.com', '(11) 98765-1234', 'Brasil', 'Guarulhos'),
(28, 'Digital Plus', '89.012.345/0001-28', 'vendas@digitalplus.com', '(41) 92345-6789', 'Brasil', 'Londrina'),
(29, 'TechUK', '90.123.456/0001-29', 'contact@techuk.co.uk', '+44 20 8456 7890', 'Reino Unido', 'Birmingham'),
(30, 'Tokyo Electronics', '01.234.567/0001-30', 'sales@tokyoelec.com', '+81 3 9876 5432', 'Japão', 'Yokohama'),
(31, 'TechImport SP', '12.345.678/0001-31', 'contato@techimportsp.com', '(11) 93456-7890', 'Brasil', 'Santo André'),
(32, 'EletroParts RJ', '23.456.789/0001-32', 'vendas@eletropartsrj.com', '(21) 92345-6789', 'Brasil', 'São Gonçalo'),
(33, 'Global Parts', '34.567.890/0001-33', 'sales@globalparts.com', '+1 (305) 555-1234', 'EUA', 'Miami'),
(34, 'Shenzhen Import', '45.678.901/0001-34', 'contact@shenzhenimport.com', '+86 755 9876 5432', 'China', 'Guangzhou'),
(35, 'Frankfurt Tech', '56.789.012/0001-35', 'info@frankfurttech.de', '+49 69 1234567', 'Alemanha', 'Frankfurt'),
(36, 'MegaImport', '67.890.123/0001-36', 'sac@megaimport.com.br', '(31) 94567-8901', 'Brasil', 'Ribeirão das Neves'),
(37, 'Componentes MG', '78.901.234/0001-37', 'contato@componentesmg.com', '(31) 98765-1234', 'Brasil', 'Uberlândia'),
(38, 'Digital Tech', '89.012.345/0001-38', 'vendas@digitaltech.com', '(41) 93456-7890', 'Brasil', 'Maringá'),
(39, 'TechLondon', '90.123.456/0001-39', 'contact@techlondon.co.uk', '+44 20 7234 5678', 'Reino Unido', 'Liverpool'),
(40, 'Osaka Electronics', '01.234.567/0001-40', 'sales@osakaelec.com', '+81 6 1234 5678', 'Japão', 'Kyoto'),
(41, 'TechImport RJ', '12.345.678/0001-41', 'contato@techimportrj.com', '(21) 93456-7890', 'Brasil', 'Duque de Caxias'),
(42, 'EletroParts SP', '23.456.789/0001-42', 'vendas@eletropartssp.com', '(11) 92345-6789', 'Brasil', 'Osasco'),
(43, 'US Tech', '34.567.890/0001-43', 'sales@ustech.com', '+1 (713) 555-9876', 'EUA', 'Houston'),
(44, 'Beijing Import', '45.678.901/0001-44', 'contact@beijingimport.com', '+86 10 9876 5432', 'China', 'Tianjin'),
(45, 'Munich Electronics', '56.789.012/0001-45', 'info@munichelec.de', '+49 89 1234567', 'Alemanha', 'Colônia'),
(46, 'MegaDist', '67.890.123/0001-46', 'sac@megadist.com.br', '(31) 95678-9012', 'Brasil', 'Ibirité'),
(47, 'Componentes PR', '78.901.234/0001-47', 'contato@componentespr.com', '(41) 98765-1234', 'Brasil', 'Cascavel'),
(48, 'Digital World', '89.012.345/0001-48', 'vendas@digitalworld.com', '(41) 94567-8901', 'Brasil', 'Ponta Grossa'),
(49, 'TechScotland', '90.123.456/0001-49', 'contact@techscotland.co.uk', '+44 131 456 7890', 'Reino Unido', 'Edimburgo'),
(50, 'Nagoya Electronics', '01.234.567/0001-50', 'sales@nagoyaelec.com', '+81 52 9876 5432', 'Japão', 'Nagoya'),
(51, 'TechImport MG', '12.345.678/0001-51', 'contato@techimportmg.com', '(31) 93456-7890', 'Brasil', 'Contagem'),
(52, 'EletroParts MG', '23.456.789/0001-52', 'vendas@eletropartsmg.com', '(31) 92345-6789', 'Brasil', 'Betim'),
(53, 'Texas Components', '34.567.890/0001-53', 'sales@texascomponents.com', '+1 (512) 555-1234', 'EUA', 'Austin'),
(54, 'Shanghai Tech', '45.678.901/0001-54', 'contact@shanghaitech.com', '+86 21 1234 5678', 'China', 'Chongqing'),
(55, 'Dusseldorf Electronics', '56.789.012/0001-55', 'info@dusseldorfelec.de', '+49 211 9876543', 'Alemanha', 'Dusseldorf'),
(56, 'MegaCom', '67.890.123/0001-56', 'sac@megacom.com.br', '(31) 96789-0123', 'Brasil', 'Santa Luzia'),
(57, 'Componentes SC', '78.901.234/0001-57', 'contato@componentessc.com', '(48) 98765-1234', 'Brasil', 'São José'),
(58, 'Digital Info', '89.012.345/0001-58', 'vendas@digitalinfo.com', '(41) 95678-9012', 'Brasil', 'Colombo'),
(59, 'TechWales', '90.123.456/0001-59', 'contact@techwales.co.uk', '+44 29 8765 4321', 'Reino Unido', 'Cardiff'),
(60, 'Fukuoka Electronics', '01.234.567/0001-60', 'sales@fukuokaelec.com', '+81 92 9876 5432', 'Japão', 'Fukuoka');

-- --------------------------------------------------------

--
-- Estrutura para tabela `funcionario`
--

CREATE TABLE `funcionario` (
  `id_funcionario` int(11) NOT NULL,
  `nome_funcionario` varchar(40) DEFAULT NULL,
  `data_nascimento_funcionario` date DEFAULT NULL,
  `data_admissao_funcionario` date DEFAULT NULL,
  `cpf_funcionario` varchar(14) DEFAULT NULL,
  `cidade_funcionario` varchar(30) DEFAULT NULL,
  `estado_funcionario` varchar(30) DEFAULT NULL,
  `telefone_funcionario` varchar(15) DEFAULT NULL,
  `email_funcionario` varchar(50) DEFAULT NULL,
  `usuario_funcionario` varchar(30) DEFAULT NULL,
  `senha_funcionario` varchar(30) DEFAULT NULL,
  `perfil_funcionario` varchar(30) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Despejando dados para a tabela `funcionario`
--

INSERT INTO `funcionario` (`id_funcionario`, `nome_funcionario`, `data_nascimento_funcionario`, `data_admissao_funcionario`, `cpf_funcionario`, `cidade_funcionario`, `estado_funcionario`, `telefone_funcionario`, `email_funcionario`, `usuario_funcionario`, `senha_funcionario`, `perfil_funcionario`) VALUES
(1, 'João Silva', '1985-05-15', '2020-03-10', '111.111.111-11', 'São Paulo', 'SP', '(11) 91234-5678', 'joao.silva@empresa.com', 'joao.silva', 'senha123', 'Administrador'),
(2, 'Maria Oliveira', '1990-08-22', '2021-02-15', '222.222.222-22', 'Rio de Janeiro', 'RJ', '(21) 92345-6789', 'maria.oliveira@empresa.com', 'maria.oliveira', 'senha456', 'Administrador'),
(3, 'Carlos Souza', '1988-11-30', '2019-07-05', '333.333.333-33', 'Belo Horizonte', 'MG', '(31) 93456-7890', 'carlos.souza@empresa.com', 'carlos.souza', 'senha789', 'Administrador'),
(4, 'Ana Costa', '1992-04-18', '2022-01-20', '444.444.444-44', 'Porto Alegre', 'RS', '(51) 94567-8901', 'ana.costa@empresa.com', 'ana.costa', 'senha101', 'Administrador'),
(5, 'Pedro Santos', '1983-07-25', '2018-05-12', '555.555.555-55', 'Curitiba', 'PR', '(41) 95678-9012', 'pedro.santos@empresa.com', 'pedro.santos', 'senha112', 'Usuario simples'),
(6, 'Juliana Lima', '1995-01-08', '2022-06-30', '666.666.666-66', 'Salvador', 'BA', '(71) 96789-0123', 'juliana.lima@empresa.com', 'juliana.lima', 'senha131', 'Usuario simples'),
(7, 'Marcos Pereira', '1980-09-14', '2017-11-15', '777.777.777-77', 'Recife', 'PE', '(81) 97890-1234', 'marcos.pereira@empresa.com', 'marcos.pereira', 'senha415', 'Usuario simples'),
(8, 'Fernanda Rocha', '1987-12-03', '2020-09-22', '888.888.888-88', 'Fortaleza', 'CE', '(85) 98901-2345', 'fernanda.rocha@empresa.com', 'fernanda.rocha', 'senha161', 'Usuario simples'),
(9, 'Ricardo Alves', '1991-03-27', '2021-04-18', '999.999.999-99', 'Manaus', 'AM', '(92) 99012-3456', 'ricardo.alves@empresa.com', 'ricardo.alves', 'senha718', 'Usuario simples'),
(10, 'Patrícia Gomes', '1984-06-09', '2019-08-07', '010.101.010-10', 'Goiânia', 'GO', '(62) 90123-4567', 'patricia.gomes@empresa.com', 'patricia.gomes', 'senha192', 'Usuario simples'),
(11, 'Lucas Mendes', '1993-02-20', '2023-01-05', '020.202.020-20', 'Florianópolis', 'SC', '(48) 92345-6789', 'lucas.mendes@empresa.com', 'lucas.mendes', 'senha223', 'Usuario simples'),
(12, 'Amanda Ferreira', '1989-05-12', '2021-07-15', '030.303.030-30', 'Vitória', 'ES', '(27) 93456-7890', 'amanda.ferreira@empresa.com', 'amanda.ferreira', 'senha334', 'Usuario simples'),
(13, 'Rodrigo Martins', '1982-08-25', '2018-10-30', '040.404.040-40', 'Natal', 'RN', '(84) 94567-8901', 'rodrigo.martins@empresa.com', 'rodrigo.martins', 'senha445', 'Usuario simples'),
(14, 'Camila Almeida', '1994-11-18', '2022-03-22', '050.505.050-50', 'João Pessoa', 'PB', '(83) 95678-9012', 'camila.almeida@empresa.com', 'camila.almeida', 'senha556', 'Usuario simples'),
(15, 'Gustavo Henrique', '1986-04-30', '2020-06-14', '060.606.060-60', 'Maceió', 'AL', '(82) 96789-0123', 'gustavo.henrique@empresa.com', 'gustavo.henrique', 'senha667', 'Usuario simples'),
(16, 'Isabela Santos', '1990-07-22', '2021-09-05', '070.707.070-70', 'Aracaju', 'SE', '(79) 97890-1234', 'isabela.santos@empresa.com', 'isabela.santos', 'senha778', 'Usuario simples'),
(17, 'Felipe Oliveira', '1981-10-15', '2017-12-20', '080.808.080-80', 'Teresina', 'PI', '(86) 98901-2345', 'felipe.oliveira@empresa.com', 'felipe.oliveira', 'senha889', 'Usuario simples'),
(18, 'Laura Costa', '1996-01-28', '2023-02-10', '090.909.090-90', 'São Luís', 'MA', '(98) 99012-3456', 'laura.costa@empresa.com', 'laura.costa', 'senha990', 'Usuario simples'),
(19, 'Rafael Souza', '1983-03-05', '2019-05-25', '101.010.101-01', 'Belém', 'PA', '(91) 90123-4567', 'rafael.souza@empresa.com', 'rafael.souza', 'senha001', 'Usuario simples'),
(20, 'Beatriz Lima', '1988-06-17', '2020-08-30', '111.111.111-12', 'Boa Vista', 'RR', '(95) 91234-5678', 'beatriz.lima@empresa.com', 'beatriz.lima', 'senha112', 'Usuario simples'),
(21, 'Thiago Pereira', '1992-09-10', '2022-11-15', '121.212.121-21', 'Porto Velho', 'RO', '(69) 92345-6789', 'thiago.pereira@empresa.com', 'thiago.pereira', 'senha123', 'Usuario simples'),
(22, 'Vanessa Rocha', '1985-12-23', '2018-02-28', '131.313.131-31', 'Rio Branco', 'AC', '(68) 93456-7890', 'vanessa.rocha@empresa.com', 'vanessa.rocha', 'senha234', 'Usuario simples'),
(23, 'Daniel Alves', '1997-02-14', '2023-04-05', '141.414.141-41', 'Macapá', 'AP', '(96) 94567-8901', 'daniel.alves@empresa.com', 'daniel.alves', 'senha345', 'Usuario simples'),
(24, 'Carolina Gomes', '1989-05-27', '2021-07-10', '151.515.151-51', 'Palmas', 'TO', '(63) 95678-9012', 'carolina.gomes@empresa.com', 'carolina.gomes', 'senha456', 'Usuario simples'),
(25, 'Eduardo Mendes', '1984-08-08', '2019-10-15', '161.616.161-61', 'Campo Grande', 'MS', '(67) 96789-0123', 'eduardo.mendes@empresa.com', 'eduardo.mendes', 'senha567', 'Usuario simples'),
(26, 'Tatiane Ferreira', '1991-11-20', '2022-01-25', '171.717.171-71', 'Cuiabá', 'MT', '(65) 97890-1234', 'tatiane.ferreira@empresa.com', 'tatiane.ferreira', 'senha678', 'Usuario simples'),
(27, 'Vinícius Martins', '1986-01-03', '2020-03-10', '181.818.181-81', 'Brasília', 'DF', '(61) 98901-2345', 'vinicius.martins@empresa.com', 'vinicius.martins', 'senha789', 'Usuario simples'),
(28, 'Priscila Almeida', '1993-04-16', '2023-06-20', '191.919.191-91', 'São Paulo', 'SP', '(11) 99012-3456', 'priscila.almeida@empresa.com', 'priscila.almeida', 'senha890', 'Usuario simples'),
(29, 'Roberto Henrique', '1987-07-29', '2020-09-05', '202.020.202-02', 'Rio de Janeiro', 'RJ', '(21) 90123-4567', 'roberto.henrique@empresa.com', 'roberto.henrique', 'senha901', 'Usuario simples'),
(30, 'Aline Santos', '1994-10-12', '2022-12-15', '212.121.212-12', 'Belo Horizonte', 'MG', '(31) 91234-5678', 'aline.santos@empresa.com', 'aline.santos', 'senha012', 'Usuario simples'),
(31, 'Marcelo Oliveira', '1982-12-25', '2018-02-28', '222.222.222-23', 'Porto Alegre', 'RS', '(51) 92345-6789', 'marcelo.oliveira@empresa.com', 'marcelo.oliveira', 'senha123', 'Usuario simples'),
(32, 'Gabriela Costa', '1989-03-08', '2021-05-10', '232.323.232-32', 'Curitiba', 'PR', '(41) 93456-7890', 'gabriela.costa@empresa.com', 'gabriela.costa', 'senha234', 'Usuario simples'),
(33, 'Leonardo Souza', '1995-06-21', '2023-08-25', '242.424.242-42', 'Salvador', 'BA', '(71) 94567-8901', 'leonardo.souza@empresa.com', 'leonardo.souza', 'senha345', 'Usuario simples'),
(34, 'Fernanda Lima', '1988-09-03', '2020-11-15', '252.525.252-52', 'Recife', 'PE', '(81) 95678-9012', 'fernanda.lima@empresa.com', 'fernanda.lima', 'senha456', 'Usuario simples'),
(35, 'Bruno Pereira', '1983-12-16', '2019-02-20', '262.626.262-62', 'Fortaleza', 'CE', '(85) 96789-0123', 'bruno.pereira@empresa.com', 'bruno.pereira', 'senha567', 'Usuario simples'),
(36, 'Daniela Rocha', '1990-02-28', '2021-04-05', '272.727.272-72', 'Manaus', 'AM', '(92) 97890-1234', 'daniela.rocha@empresa.com', 'daniela.rocha', 'senha678', 'Usuario simples'),
(37, 'Fábio Alves', '1985-05-11', '2020-07-10', '282.828.282-82', 'Goiânia', 'GO', '(62) 98901-2345', 'fabio.alves@empresa.com', 'fabio.alves', 'senha789', 'Usuario simples'),
(38, 'Cristina Gomes', '1992-08-24', '2022-10-15', '292.929.292-92', 'Florianópolis', 'SC', '(48) 99012-3456', 'cristina.gomes@empresa.com', 'cristina.gomes', 'senha890', 'Usuario simples'),
(39, 'Alexandre Mendes', '1987-11-06', '2020-01-20', '303.030.303-03', 'Vitória', 'ES', '(27) 90123-4567', 'alexandre.mendes@empresa.com', 'alexandre.mendes', 'senha901', 'Usuario simples'),
(40, 'Monica Ferreira', '1993-01-19', '2023-03-25', '313.131.313-13', 'Natal', 'RN', '(84) 91234-5678', 'monica.ferreira@empresa.com', 'monica.ferreira', 'senha012', 'Usuario simples'),
(41, 'Ricardo Martins', '1986-04-02', '2020-06-05', '323.232.323-23', 'João Pessoa', 'PB', '(83) 92345-6789', 'ricardo.martins@empresa.com', 'ricardo.martins', 'senha123', 'Usuario simples'),
(42, 'Patricia Almeida', '1991-07-15', '2021-09-10', '333.333.333-34', 'Maceió', 'AL', '(82) 93456-7890', 'patricia.almeida@empresa.com', 'patricia.almeida', 'senha234', 'Usuario simples'),
(43, 'Rodrigo Henrique', '1984-10-28', '2019-12-15', '343.434.343-43', 'Aracaju', 'SE', '(79) 94567-8901', 'rodrigo.henrique@empresa.com', 'rodrigo.henrique', 'senha345', 'Usuario simples'),
(44, 'Tatiana Santos', '1996-02-10', '2023-04-20', '353.535.353-53', 'Teresina', 'PI', '(86) 95678-9012', 'tatiana.santos@empresa.com', 'tatiana.santos', 'senha456', 'Usuario simples'),
(45, 'Marcos Oliveira', '1989-05-23', '2021-07-05', '363.636.363-63', 'São Luís', 'MA', '(98) 96789-0123', 'marcos.oliveira@empresa.com', 'marcos.oliveira', 'senha567', 'Usuario simples'),
(46, 'Juliana Costa', '1994-08-05', '2022-10-10', '373.737.373-73', 'Belém', 'PA', '(91) 97890-1234', 'juliana.costa@empresa.com', 'juliana.costa', 'senha678', 'Usuario simples'),
(47, 'Gustavo Souza', '1987-11-18', '2020-01-15', '383.838.383-83', 'Boa Vista', 'RR', '(95) 98901-2345', 'gustavo.souza@empresa.com', 'gustavo.souza', 'senha789', 'Usuario simples'),
(48, 'Amanda Lima', '1992-01-31', '2022-03-20', '393.939.393-93', 'Porto Velho', 'RO', '(69) 99012-3456', 'amanda.lima@empresa.com', 'amanda.lima', 'senha890', 'Usuario simples'),
(49, 'Carlos Pereira', '1985-04-13', '2020-06-25', '404.040.404-04', 'Rio Branco', 'AC', '(68) 90123-4567', 'carlos.pereira@empresa.com', 'carlos.pereira', 'senha901', 'Usuario simples'),
(50, 'Luciana Rocha', '1990-07-26', '2021-09-05', '414.141.414-14', 'Macapá', 'AP', '(96) 91234-5678', 'luciana.rocha@empresa.com', 'luciana.rocha', 'senha012', 'Usuario simples'),
(51, 'Felipe Alves', '1983-10-08', '2018-12-10', '424.242.424-24', 'Palmas', 'TO', '(63) 92345-6789', 'felipe.alves@empresa.com', 'felipe.alves', 'senha123', 'Usuario simples'),
(52, 'Vanessa Gomes', '1996-01-21', '2023-03-15', '434.343.434-34', 'Campo Grande', 'MS', '(67) 93456-7890', 'vanessa.gomes@empresa.com', 'vanessa.gomes', 'senha234', 'Usuario simples'),
(53, 'Rafael Mendes', '1988-04-03', '2020-06-20', '444.444.444-45', 'Cuiabá', 'MT', '(65) 94567-8901', 'rafael.mendes@empresa.com', 'rafael.mendes', 'senha345', 'Usuario simples'),
(54, 'Camila Ferreira', '1993-07-16', '2022-09-25', '454.545.454-54', 'Brasília', 'DF', '(61) 95678-9012', 'camila.ferreira@empresa.com', 'camila.ferreira', 'senha456', 'Usuario simples'),
(55, 'Thiago Martins', '1986-10-29', '2020-12-05', '464.646.464-64', 'São Paulo', 'SP', '(11) 96789-0123', 'thiago.martins@empresa.com', 'thiago.martins', 'senha567', 'Usuario simples'),
(56, 'Isabela Almeida', '1991-01-11', '2022-03-10', '474.747.474-74', 'Rio de Janeiro', 'RJ', '(21) 97890-1234', 'isabela.almeida@empresa.com', 'isabela.almeida', 'senha678', 'Usuario simples'),
(57, 'Lucas Henrique', '1984-03-24', '2019-05-15', '484.848.484-84', 'Belo Horizonte', 'MG', '(31) 98901-2345', 'lucas.henrique@empresa.com', 'lucas.henrique', 'senha789', 'Usuario simples'),
(58, 'Laura Santos', '1997-06-06', '2023-08-20', '494.949.494-94', 'Porto Alegre', 'RS', '(51) 99012-3456', 'laura.santos@empresa.com', 'laura.santos', 'senha890', 'Usuario simples'),
(59, 'Eduardo Oliveira', '1990-09-19', '2021-11-25', '505.050.505-05', 'Curitiba', 'PR', '(41) 90123-4567', 'eduardo.oliveira@empresa.com', 'eduardo.oliveira', 'senha901', 'Usuario simples'),
(60, 'Beatriz Costa', '1985-12-02', '2020-02-05', '515.151.515-15', 'Salvador', 'BA', '(71) 91234-5678', 'beatriz.costa@empresa.com', 'beatriz.costa', 'senha012', 'Usuario simples');

-- --------------------------------------------------------

--
-- Estrutura para tabela `pedido`
--

CREATE TABLE `pedido` (
  `id_pedido` int(11) NOT NULL,
  `quantidade_produto_item` int(11) DEFAULT NULL,
  `idProduto` int(11) NOT NULL,
  `idCliente` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Despejando dados para a tabela `pedido`
--

INSERT INTO `pedido` (`id_pedido`, `quantidade_produto_item`, `idProduto`, `idCliente`) VALUES
(1, 1, 1, 1),
(2, 2, 2, 2),
(3, 3, 1, 3),
(4, 4, 4, 1),
(5, 5, 5, 5),
(6, 6, 6, 6),
(7, 7, 7, 7),
(8, 8, 8, 8),
(9, 8, 1, 9),
(10, 8, 10, 10),
(11, 8, 11, 11),
(12, 8, 12, 1),
(13, 8, 13, 13),
(14, 8, 14, 14),
(15, 8, 15, 15),
(16, 8, 16, 16),
(17, 8, 17, 17),
(18, 8, 18, 18),
(19, 8, 19, 19),
(20, 8, 20, 20),
(21, 8, 21, 21),
(22, 8, 22, 22),
(23, 8, 23, 23),
(24, 8, 24, 24),
(25, 8, 25, 25),
(26, 8, 26, 26),
(27, 8, 27, 27),
(28, 8, 28, 28),
(29, 8, 29, 29),
(30, 8, 30, 30),
(31, 8, 31, 31),
(32, 8, 32, 32),
(33, 8, 33, 33),
(34, 8, 34, 34),
(35, 8, 35, 35),
(36, 8, 36, 36),
(37, 8, 37, 37),
(38, 8, 38, 38),
(39, 8, 39, 39),
(40, 8, 40, 40),
(41, 8, 41, 41),
(42, 8, 42, 42),
(43, 8, 43, 43),
(44, 8, 44, 44),
(45, 8, 45, 45),
(46, 8, 46, 46),
(47, 8, 47, 47),
(48, 8, 48, 48),
(49, 8, 49, 49),
(50, 8, 50, 50),
(51, 8, 51, 51),
(52, 8, 52, 52),
(53, 8, 53, 53),
(54, 8, 54, 54),
(55, 8, 55, 55),
(56, 8, 56, 56),
(57, 8, 57, 57),
(58, 8, 58, 58),
(59, 8, 59, 59),
(60, 8, 60, 60),
(61, 10, 60, 38),
(62, 9, 1, 50);

--
-- Acionadores `pedido`
--
DELIMITER $$
CREATE TRIGGER `diminuir_quantidade_produto` AFTER INSERT ON `pedido` FOR EACH ROW begin
    update Produto
    set quantidade_produto = quantidade_produto - new.quantidade_produto_item
    where id_produto = new.IdProduto;
end
$$
DELIMITER ;

-- --------------------------------------------------------

--
-- Estrutura para tabela `produto`
--

CREATE TABLE `produto` (
  `id_produto` int(11) NOT NULL,
  `nome_produto` varchar(40) DEFAULT NULL,
  `descricao_produto` varchar(200) DEFAULT NULL,
  `categoria_produto` varchar(50) NOT NULL,
  `quantidade_produto` int(11) DEFAULT NULL,
  `valor_produto` decimal(10,2) DEFAULT NULL,
  `idFornecedor` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Despejando dados para a tabela `produto`
--

INSERT INTO `produto` (`id_produto`, `nome_produto`, `descricao_produto`, `categoria_produto`, `quantidade_produto`, `valor_produto`, `idFornecedor`) VALUES
(1, 'Notebook Dell', 'Notebook Dell Inspiron 15 i5 8GB 256GB SSD', 'Notebooks', 90, 3499.90, 1),
(2, 'Mouse Logitech', 'Mouse sem fio Logitech M170', 'Periféricos', 238, 79.90, 2),
(3, 'Teclado Mecânico', 'Teclado mecânico Redragon Kumara', 'Periféricos', 67, 279.90, 3),
(4, 'Monitor 24\"', 'Monitor LG 24\" Full HD IPS', 'Monitores', 52, 899.90, 4),
(5, 'SSD 480GB', 'SSD Kingston 480GB SATA', 'Armazenamento', 145, 249.90, 5),
(6, 'Smartphone Samsung', 'Samsung Galaxy A54 128GB', 'Celulares', 74, 1899.90, 6),
(7, 'Tablet Amazon', 'Fire HD 10 32GB', 'Tablets', 53, 999.90, 7),
(8, 'Impressora HP', 'Impressora HP DeskJet 2776', 'Impressão e Digitalização', 42, 499.90, 8),
(9, 'Headphone Sony', 'Fone de ouvido Sony WH-CH510', 'Áudio e Som', 112, 199.90, 9),
(10, 'Webcam Logitech', 'Webcam Logitech C920 HD Pro', 'Periféricos', 82, 399.90, 10),
(11, 'Roteador TP-Link', 'Roteador Wi-Fi TP-Link Archer C6', 'Redes e Conectividade', 102, 299.90, 11),
(12, 'HD Externo Seagate', 'HD Externo Seagate 1TB USB 3.0', 'Armazenamento', 72, 349.90, 12),
(13, 'Pendrive Kingston', 'Pendrive Kingston 64GB USB 3.0', 'Armazenamento', 192, 59.90, 13),
(14, 'Placa de Vídeo GTX 1650', 'Placa de vídeo GTX 1650 GDDR6', 'Placas de Vídeo', 22, 1299.90, 14),
(15, 'Processador Intel i5 10ª geração', 'Processador Intel Core i5 10400F', 'Processadores', 42, 999.90, 15),
(16, 'Placa-Mãe ATX LGA 1200', 'Placa-mãe ATX LGA 1200 para Intel', 'Placas-Mãe', 32, 699.90, 16),
(17, 'Memória RAM DDR4 8GB', 'Memória RAM 8GB DDR4 3200MHz', 'Memória RAM', 112, 199.90, 17),
(18, 'SSD NVMe 500GB', 'SSD NVMe 500GB PCIe Gen3', 'Armazenamento', 72, 349.90, 18),
(19, 'Fonte ATX 500W 80 Plus', 'Fonte ATX 500W certificada', 'Fontes de Alimentação', 52, 299.90, 19),
(20, 'Gabinete Gamer com RGB', 'Gabinete gamer ATX com iluminação RGB', 'Gabinetes', 42, 399.90, 20),
(21, 'Water Cooler 240mm', 'Water cooler para processador', 'Resfriamento', 28, 349.90, 21),
(22, 'Mouse Gamer Redragon Cobra', 'Mouse gamer Redragon Cobra', 'Periféricos', 82, 159.90, 22),
(23, 'Teclado Gamer Redragon Kumara', 'Teclado gamer Redragon Kumara', 'Periféricos', 72, 279.90, 23),
(24, 'Monitor Gamer 24\" 144Hz', 'Monitor Gamer 24\" 144Hz', 'Monitores', 36, 1299.90, 24),
(25, 'Headset Gamer', 'Headset gamer com microfone', 'Áudio e Som', 92, 199.90, 25),
(26, 'Mousepad RGB', 'Mousepad gamer com iluminação RGB', 'Periféricos', 62, 89.90, 26),
(27, 'Webcam Gamer Full HD', 'Webcam gamer Full HD', 'Periféricos', 42, 349.90, 27),
(28, 'Controle Bluetooth para PC/Android', 'Controle Bluetooth para PC/Android', 'Acessórios', 72, 149.90, 28),
(29, 'Joystick Gamer sem fio', 'Joystick gamer sem fio', 'Acessórios', 52, 229.90, 29),
(30, 'Memória RAM 32GB DDR4', 'Memória RAM 32GB DDR4 3600MHz', 'Memória RAM', 62, 429.90, 30),
(31, 'Notebook Gamer', 'Notebook Gamer Acer Nitro 5', 'Notebooks', 28, 4999.90, 31),
(32, 'Mouse Gamer', 'Mouse gamer Redragon Cobra', 'Periféricos', 82, 159.90, 32),
(33, 'Teclado Gamer', 'Teclado gamer Redragon Kumara', 'Periféricos', 72, 279.90, 33),
(34, 'Monitor Gamer', 'Monitor Gamer 24\" 144Hz', 'Monitores', 36, 1299.90, 34),
(35, 'Headset Gamer', 'Headset gamer com microfone', 'Áudio e Som', 92, 199.90, 35),
(36, 'Mousepad RGB', 'Mousepad gamer com iluminação RGB', 'Periféricos', 62, 89.90, 36),
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

--
-- Índices para tabelas despejadas
--

--
-- Índices de tabela `cadastro`
--
ALTER TABLE `cadastro`
  ADD PRIMARY KEY (`id_cadastro`),
  ADD KEY `fk_funcionario_cadastro` (`idFuncionario`),
  ADD KEY `fk_cliente_cadastro` (`idCliente`);

--
-- Índices de tabela `cliente`
--
ALTER TABLE `cliente`
  ADD PRIMARY KEY (`id_cliente`);

--
-- Índices de tabela `estoque`
--
ALTER TABLE `estoque`
  ADD PRIMARY KEY (`id_estoque`),
  ADD KEY `fk_produto_estoque` (`IdProduto`);

--
-- Índices de tabela `fornecedor`
--
ALTER TABLE `fornecedor`
  ADD PRIMARY KEY (`id_fornecedor`);

--
-- Índices de tabela `funcionario`
--
ALTER TABLE `funcionario`
  ADD PRIMARY KEY (`id_funcionario`);

--
-- Índices de tabela `pedido`
--
ALTER TABLE `pedido`
  ADD PRIMARY KEY (`id_pedido`),
  ADD KEY `fk_produto_pedido` (`idProduto`),
  ADD KEY `fk_cliente_pedido` (`idCliente`);

--
-- Índices de tabela `produto`
--
ALTER TABLE `produto`
  ADD PRIMARY KEY (`id_produto`),
  ADD KEY `fk_fornecedor_produto` (`idFornecedor`);

--
-- AUTO_INCREMENT para tabelas despejadas
--

--
-- AUTO_INCREMENT de tabela `cadastro`
--
ALTER TABLE `cadastro`
  MODIFY `id_cadastro` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=61;

--
-- AUTO_INCREMENT de tabela `cliente`
--
ALTER TABLE `cliente`
  MODIFY `id_cliente` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=61;

--
-- AUTO_INCREMENT de tabela `estoque`
--
ALTER TABLE `estoque`
  MODIFY `id_estoque` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=61;

--
-- AUTO_INCREMENT de tabela `fornecedor`
--
ALTER TABLE `fornecedor`
  MODIFY `id_fornecedor` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=61;

--
-- AUTO_INCREMENT de tabela `funcionario`
--
ALTER TABLE `funcionario`
  MODIFY `id_funcionario` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=61;

--
-- AUTO_INCREMENT de tabela `pedido`
--
ALTER TABLE `pedido`
  MODIFY `id_pedido` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=63;

--
-- AUTO_INCREMENT de tabela `produto`
--
ALTER TABLE `produto`
  MODIFY `id_produto` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=61;

--
-- Restrições para tabelas despejadas
--

--
-- Restrições para tabelas `cadastro`
--
ALTER TABLE `cadastro`
  ADD CONSTRAINT `fk_cliente_cadastro` FOREIGN KEY (`idCliente`) REFERENCES `cliente` (`id_cliente`),
  ADD CONSTRAINT `fk_funcionario_cadastro` FOREIGN KEY (`idFuncionario`) REFERENCES `funcionario` (`id_funcionario`);

--
-- Restrições para tabelas `estoque`
--
ALTER TABLE `estoque`
  ADD CONSTRAINT `fk_produto_estoque` FOREIGN KEY (`IdProduto`) REFERENCES `produto` (`id_produto`);

--
-- Restrições para tabelas `pedido`
--
ALTER TABLE `pedido`
  ADD CONSTRAINT `fk_cliente_pedido` FOREIGN KEY (`idCliente`) REFERENCES `cliente` (`id_cliente`),
  ADD CONSTRAINT `fk_produto_pedido` FOREIGN KEY (`idProduto`) REFERENCES `produto` (`id_produto`);

--
-- Restrições para tabelas `produto`
--
ALTER TABLE `produto`
  ADD CONSTRAINT `fk_fornecedor_produto` FOREIGN KEY (`idFornecedor`) REFERENCES `fornecedor` (`id_fornecedor`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
