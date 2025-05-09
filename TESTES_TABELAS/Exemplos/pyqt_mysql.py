from PyQt5.QtWidgets import QApplication, QMainWindow, QTableView
from PyQt5.QtSql import QSqlDatabase, QSqlTableModel
import sys

db = QSqlDatabase.addDatabase("QMYSQL")
db.setHostName("localhost")
db.setDatabaseName("tbit_db")
db.setUserName("root")
db.setPassword("")
db.open()

class TabelaBD(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Tabela MySQL")
        self.resize(600, 400)

        model = QSqlTableModel()
        model.setTable("nome_da_tabela")
        model.select()

        table_view = QTableView()
        table_view.setModel(model)
        self.setCentralWidget(table_view)

app = QApplication(sys.argv)
janela = TabelaBD()
janela.show()
sys.exit(app.exec_())