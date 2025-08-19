<?php
// Configurações do banco de dados
$host = "localhost"; // Endereço do servidor
$dbname = "empresa"; // Nome do banco
$usuario = "root"; // Usuário do banco
$senha = ""; // Senha do banco

try {
    // Criando a conexão PDO
    $pdo = new PDO("mysql:host=$host;dbname=$dbname;charset=utf8", $usuario, $senha);

    // Definindo o modo de erro do PDO para exceções
    $pdo->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);

    // (Opcional) Exibir mensagem de sucesso
    // echo "Conexão realizada com sucesso!";
} catch (PDOException $e) {
    // Se der erro, exibe a mensagem
    echo "Erro na conexão: " . $e->getMessage();
    exit;
}
?>