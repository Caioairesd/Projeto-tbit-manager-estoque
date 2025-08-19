from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Inicia o servicção do ChromeDriver
servico = webdriver.ChromeService(executable_path="C:/xampp/htdocs/Projeto-tbit-manager-estoque/chromedriver-win64/chromedriver.exe")
driver = webdriver.Chrome(service=servico)

try:
    # 1. Abre a página do app de estoque
    driver.get("file:///C:/xampp/htdocs/Projeto-tbit-manager-estoque/Selenium/criar.php")

    # 2. Encontra os campos de input e preenche com os dados do produto
    campo_nome = driver.find_element(By.ID, 'nome')
    campo_data_n = driver.find_element(By.ID, 'data_nascimento')
    campo_data_a = driver.find_element(By.ID, 'data_admissao')
    campo_cpf = driver.find_element(By.ID, 'cpf')
    campo_cidade = driver.find_element(By.ID, 'cidade')
    campo_uf = driver.find_element(By.ID, 'uf')
    campo_telefone = driver.find_element(By.ID, 'telefone')
    campo_email = driver.find_element(By.ID, 'email')
    campo_usuario = driver.find_element(By.ID, 'usuario')
    campo_senha = driver.find_element(By.ID, 'senha')
    campo_perfil = driver.find_element(By.ID, 'perfil')

    botao_cadastrar = driver.find_element(By.ID, 'cadastrar')

    campo_nome.send_keys("Caio Aires")
    campo_data_n.send_keys("30/01/2008")
    campo_data_a.send_keys("17/02/2025")
    campo_cpf.send_keys("000.000.000-00")
    campo_cidade.send_keys("Joinville")
    campo_uf.send_keys("SC")
    campo_telefone.send_keys("4002-8922")
    campo_email.send_keys("caio@gmail.com")
    campo_usuario.send_keys("caio_aires")
    campo_senha.send_keys("1234")
    campo_perfil.send_keys("ADM")

    # 3. Clica no botão para adicionar
    botao_cadastrar.click()
    time.sleep(2) # Pausa para a pagina atualizar
    # 4. Validação: Verifica se o novo produto existe na tabela
    tabela = driver.find_element(By.ID, 'table')

    if "Caio Aires" in tabela.text and "30/01/2008" in tabela.text and "17/02/2025" in tabela.text and "000.000.000-00" in tabela.text and "Joinville" in tabela.text and "SC" in tabela.text and "4002-8922" in tabela.text and "caio@gmail.com" in tabela.text and "caio_aires" in tabela.text and "1234" in tabela.text and "ADM" in tabela.text:
        print("Teste de cadastro de produto: SUCESSO!")
    else:
        print("Teste de cadastro de produto: FALHA!")

finally:
    # Fecha o navegador
    driver.quit()