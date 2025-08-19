<?php
require_once 'includes/conexao.php';
require_once 'includes/cabecalho.php';

$funcionario = null;

if (isset($_GET["id"])) {
    $id = $_GET["id"];
    $sql = "SELECT nome, cargo, foto FROM funcionarios WHERE id = :id";
    $stmt = $pdo->prepare($sql);
    $stmt->bindParam(":id", $id, PDO::PARAM_INT);
    $stmt->execute();
    $funcionario = $stmt->fetch(PDO::FETCH_ASSOC);
}

if ($_SERVER["REQUEST_METHOD"] === "POST" && isset($_POST["excluir_id"])) {
    $excluir_id = $_POST["excluir_id"];
    $sql_excluir = "DELETE FROM funcionarios WHERE id = :id";
    $stmt_excluir = $pdo->prepare($sql_excluir);
    $stmt_excluir->bindParam(":id", $excluir_id, PDO::PARAM_INT);
    $stmt_excluir->execute();
    header("Location: consulta_funcionario.php");
    exit();
}
?>
<!DOCTYPE html>
<html lang="pt-br">

<head>
    <meta charset="UTF-8">
    <title>Visualizar Funcionário</title>
    <link rel="stylesheet" href="estilo.css">
</head>

<body>
    <div class="visualizar-funcionario">
        <h1>Dados do Funcionário</h1>
        <?php if ($funcionario): ?>
            <p>Nome: <?= htmlspecialchars($funcionario['nome']) ?></p>
            <p>Cargo: <?= htmlspecialchars($funcionario['cargo']) ?></p>
            <img src="data:image/jpeg;base64,<?= base64_encode($funcionario['foto']) ?>" alt="Foto"
                style="max-width:200px;">
        <?php else: ?>
            <p>Funcionário não encontrado.</p>
        <?php endif; ?>
    </div>

    <?php require_once 'includes/rodape.php'; ?>