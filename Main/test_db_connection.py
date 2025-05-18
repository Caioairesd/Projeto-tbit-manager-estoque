import mysql.connector

MYSQL_HOST = 'localhost'
MYSQL_USER = 'root'
MYSQL_PASSWORD = 'root'
MYSQL_DATABASE = 'tbit_db'

try:
    conn = mysql.connector.connect(
        host=MYSQL_HOST,
        user=MYSQL_USER,
        password=MYSQL_PASSWORD,
        database=MYSQL_DATABASE
    )
    if conn.is_connected():
        print("Conexão com o banco de dados realizada com sucesso!")
    conn.close()
except mysql.connector.Error as err:
    print(f"Erro ao conectar ao banco de dados: {err}")