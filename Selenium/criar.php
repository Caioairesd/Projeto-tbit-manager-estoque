<?php
require_once 'includes/conexao.php';
require_once 'includes/cabecalho.php';

$msg = '';

if ($_SERVER["REQUEST_METHOD"] === "POST") {
    $nome = $_POST['nome'];
    $data_nascimento = $_POST['data_nascimento'];
    $data_admissao = $_POST['data_admissao'];
    $cpf = $_POST['cpf'];
    $cidade = $_POST['cidade'];
    $uf = $_POST['uf'];
    $telefone = $_POST['telefone'];
    $email = $_POST['email'];
    $usuario = $_POST['usuario'];
    $senha = $_POST['senha'];
    $perfil = $_POST['perfil'];

    $sql = 'INSERT INTO funcionarios (nome_completo, data_nascimento, data_admissao, cpf, cidade, uf, telefone, email, usuario, senha, perfil) VALUES (:nome_completo, :data_nascimento, :data_admissao, :cpf, :cidade, :uf, :telefone, :email, :usuario, :senha, :perfil)';
    $stmt = $pdo->prepare($sql);

    $stmt->bindParam(':nome_completo', $nome);
    $stmt->bindParam(':data_nascimento', $data_nascimento);
    $stmt->bindParam(':data_admissao', $data_admissao);
    $stmt->bindParam(':cpf', $cpf);
    $stmt->bindParam(':cidade', $cidade);
    $stmt->bindParam(':uf', $uf);
    $stmt->bindParam(':telefone', $telefone);
    $stmt->bindParam(':email', $email);
    $stmt->bindParam(':usuario', $usuario);
    $stmt->bindParam(':senha', $senha);
    $stmt->bindParam(':perfil', $perfil);

    try {
        $stmt->execute();
        $msg = '<div class="sucesso">✅ Funcionário cadastrado com sucesso!</div>';
    } catch (PDOException $e) {
        $msg = '<div class="erro">❌ Erro ao cadastrar funcionário!</span></div>';
    }
}
?>

<div class="pagina-wrapper">
    <div class="container">
        <div class="titulo">
            <h1>Cadastrar Funcionário</h1>
        </div>
        <?= $msg ?>

        <form method="post" action="criar.php">
            <label for="nome">Nome completo:</label>
            <input type="text" id="nome" name="nome" required>

            <label for="data_nascimento">Data de Nascimento:</label>
            <input type="date" id="data_nascimento" name="data_nascimento" required>

            <label for="data_admissao">Data de Admissão:</label>
            <input type="date" id="data_admissao" name="data_admissao" required>

            <label for="cpf">CPF:</label>
            <input type="text" id="cpf" name="cpf" required>

            <label for="cidade">Cidade:</label>
            <input type="text" id="cidade" name="cidade" required>

            <label for="uf">UF:</label>
            <input type="text" id="uf" name="uf" required>

            <label for="telefone">Telefone:</label>
            <input type="text" id="telefone" name="telefone" required>

            <label for="email">E-mail:</label>
            <input type="email" id="email" name="email" required>

            <label for="usuario">Usuario:</label>
            <input type="text" id="usuario" name="usuario" required>

            <label for="senha">Senha:</label>
            <input type="password" id="senha" name="senha" required>

            <label for="perfil">Perfil do Usuário:</label>
            <select name="perfil" id="perfil">
                <option>ADM</option>
                <option>Funcionário</option>
            </select>

            <button type="submit" name="cadastrar" id="cadastrar">Cadastrar</button>
        </form>
    </div>
</div>

<table name="table" id="table"></table>

<script>
    setTimeout(() => {
        const msg = document.querySelector('.sucesso, .erro');
        if (msg) {
            msg.style.transition = 'opacity 0.5s ease';
            msg.style.opacity = '0';
            setTimeout(() => {
                msg.style.display = 'none';
            }, 500); // espera a transição terminar
        }
    }, 4000);
</script>


<?php require_once 'includes/rodape.php'; ?>