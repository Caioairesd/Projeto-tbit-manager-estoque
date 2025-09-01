from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import time

# Função para teste automatizado
def selenium_test(driver, nome, data_n, data_a, cpf, cidade, uf, telefone, email, usuario, senha, perfil):

    # 1. Abre a página do app de estoque
    driver.get("http://localhost:8080/Projeto-tbit-manager-estoque/Selenium/criar.php")

    driver.implicitly_wait(3)

    # 2. Encontra os campos de input e preenche com os dados do produto
    campo_nome = driver.find_element(By.ID, "nome_completo")
    campo_data_n = driver.find_element(By.ID, "data_nascimento")
    campo_data_a = driver.find_element(By.ID, "data_admissao")
    campo_cpf = driver.find_element(By.ID, "cpf")
    campo_cidade = driver.find_element(By.ID, "cidade")
    campo_uf = driver.find_element(By.ID, "uf")
    campo_telefone = driver.find_element(By.ID, "telefone")
    campo_email = driver.find_element(By.ID, "email")
    campo_usuario = driver.find_element(By.ID, "usuario")
    campo_senha = driver.find_element(By.ID, "senha")
    campo_perfil = driver.find_element(By.ID, "perfil")

    botao_cadastrar = driver.find_element(By.ID, "cadastrar_usuario")

    campo_nome.send_keys(nome)
    campo_data_n.send_keys(data_n)
    campo_data_a.send_keys(data_a)
    campo_cpf.send_keys(cpf)
    campo_cidade.send_keys(cidade)
    campo_uf.send_keys(uf)
    campo_telefone.send_keys(telefone)
    campo_email.send_keys(email)
    campo_usuario.send_keys(usuario)
    campo_senha.send_keys(senha)
    campo_perfil.send_keys(perfil)

    # 3. Clica no botão para adicionar
    time.sleep(5)
    botao_cadastrar.click()
    time.sleep(2) # Pausa para a pagina atualizar

    # 4. Acessa a página onde a tabela está
    driver.get("http://localhost:8080/Projeto-tbit-manager-estoque/Selenium/listar.php")

    # 5. Espera a tabela aparecer
    time.sleep(3)

    data_n_invert = inverter_data(data_n)
    data_a_invert = inverter_data(data_a)

    # 6. Verifica se os dados do funcionário aparecem
    tabela = driver.find_element(By.ID, "tabela_funcionarios")
    dados_esperados = [
        nome, data_n_invert, data_a_invert, cpf,
        cidade, uf, telefone, email,
        usuario, senha, perfil
    ]

    if all(dado in tabela.text for dado in dados_esperados):
        return print("Teste de cadastro de funcionário: SUCESSO!")
    else:
        return print("Teste de cadastro de funcionário: FALHA!")

# Função para inverter datas
def inverter_data(data):
    test_date = data.split("-")
    return test_date[2]+"-"+test_date[1]+"-"+test_date[0]

# Entradas que vão ser testadas:
nome_completo = "Caio Aires"
data_nascimento = "30-01-2008"
data_admissao = "17-02-2025"
cpf = "000.000.000-00"
cidade = "Joinville"
uf = "SC"
telefone = "4002-8922"
email = "caio@gmail.com"
usuario = "caio_aires"
senha = "1234"
perfil = "ADM"

# Inicia o servicção do ChromeDriver
servico = webdriver.ChromeService(executable_path="C:/xampp/htdocs/Projeto-tbit-manager-estoque/chromedriver-win64/chromedriver.exe")
driver = webdriver.Chrome(service=servico)

try:
    selenium_test(driver, nome_completo, data_nascimento, data_admissao, cpf, cidade, uf, telefone, email, usuario, senha, perfil)

finally:
    driver.quit()