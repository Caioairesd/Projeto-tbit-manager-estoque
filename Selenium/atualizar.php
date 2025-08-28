<?php
require_once 'includes/conexao.php';
require_once 'includes/cabecalho.php';

$msg = '';
$id = $_GET['id'] ?? null;

if (!$id) {
    echo '<span class="erro">ID inválido.</span>';
    exit;
}

// Buscar dados atuais
$sql = 'SELECT * FROM funcionarios WHERE id = :id';
$stmt = $pdo->prepare($sql);
$stmt->bindParam(':id', $id, PDO::PARAM_INT);
$stmt->execute();
$funcionario = $stmt->fetch(PDO::FETCH_ASSOC);

if ($_SERVER["REQUEST_METHOD"] === "POST") {
    $nome = $_POST['nome'];
    $cargo = $_POST['cargo'];

    if (!empty($_FILES['foto']['tmp_name'])) {
        function redimensionar($imagem, $largura, $altura)
        {
            list($larguraOriginal, $alturaOriginal) = getimagesize($imagem);
            $nova_imagem = imagecreatetruecolor($largura, $altura);
            $imagemOriginal = imagecreatefromjpeg($imagem);
            imagecopyresampled($nova_imagem, $imagemOriginal, 0, 0, 0, 0, $largura, $altura, $larguraOriginal, $alturaOriginal);
            ob_start();
            imagejpeg($nova_imagem);
            $dadosImagem = ob_get_clean();
            imagedestroy($nova_imagem);
            imagedestroy($imagemOriginal);
            return $dadosImagem;
        }

        $foto = redimensionar($_FILES['foto']['tmp_name'], 300, 400);
        $sql = 'UPDATE funcionarios SET nome = :nome, cargo = :cargo, foto = :foto WHERE id = :id';
        $stmt = $pdo->prepare($sql);
        $stmt->bindParam(':foto', $foto, PDO::PARAM_LOB);
    } else {
        $sql = 'UPDATE funcionarios SET nome = :nome, cargo = :cargo WHERE id = :id';
        $stmt = $pdo->prepare($sql);
    }

    $stmt->bindParam(':nome', $nome);
    $stmt->bindParam(':cargo', $cargo);
    $stmt->bindParam(':id', $id, PDO::PARAM_INT);

    if ($stmt->execute()) {
        $msg = '<span class="sucesso">Funcionário atualizado com sucesso!</span>';
    } else {
        $msg = '<span class="erro">Erro ao atualizar funcionário!</span>';
    }
}
?>

<!DOCTYPE html>
<html lang="pt-br">

<head>
    <meta charset="UTF-8" />
    <title>Editar Funcionário</title>
    <link rel="stylesheet" href="estilo.css" />
</head>

<body>
    <script>
        setTimeout(() => {
            const msg = document.querySelector('.mensagem');
            if (msg) {
                msg.style.transition = 'opacity 0.5s ease';
                msg.style.opacity = '0';
                setTimeout(() => {
                    msg.style.display = 'none';
                }, 500); // espera a transição terminar
            }
        }, 4000);
    </script>

    <div class="pagina-wrapper">
        <div class="container">
            <div class="setTimeout"></div>
            <div class="titulo">
                <h1>Editar Funcionário</h1>
            </div>
            <?php if ($msg): ?>
                <div class="mensagem"><?= $msg ?></div>
            <?php endif; ?>

            <form method="post" enctype="multipart/form-data">
                <label for="nome">Nome:</label>
                <input type="text" id="nome" name="nome" value="<?= htmlspecialchars($funcionario['nome']) ?>" required>

                <label for="cargo">Cargo:</label>
                <input type="text" id="cargo" name="cargo" value="<?= htmlspecialchars($funcionario['cargo']) ?>"
                    required>

                <label for="foto">Nova Imagem (opcional):</label>
                <input type="file" id="foto" name="foto" accept="image/*">

                <div class="butoes">
                    <button type="submit">Atualizar</button>
                </div>
            </form>
        </div>
    </div>

    <?php require_once 'includes/rodape.php'; ?>