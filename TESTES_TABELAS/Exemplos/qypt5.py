import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLineEdit, QTableView
from PyQt5.QtCore import Qt, QSortFilterProxyModel
from PyQt5.QtGui import QStandardItemModel, QStandardItem

class TabelaComFiltro(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Tabela com Filtro")
        self.resize(400, 300)

        layout = QVBoxLayout(self)

        # Campo de filtro
        self.filtro = QLineEdit()
        self.filtro.setPlaceholderText("Filtrar por nome...")
        self.filtro.textChanged.connect(self.aplicar_filtro)
        layout.addWidget(self.filtro)

        # Modelo de dados
        self.modelo = QStandardItemModel()
        self.modelo.setHorizontalHeaderLabels(["Nome", "Idade", "Profissão"])

        # Inserindo dados
        dados = [
            ("Ana", 25, "Engenheira"),
            ("João", 30, "Médico"),
            ("Maria", 22, "Estudante"),
            ("Carlos", 28, "Designer"),
        ]
        for nome, idade, profissao in dados:
            self.modelo.appendRow([
                QStandardItem(nome),
                QStandardItem(str(idade)),
                QStandardItem(profissao)
            ])

        # Modelo proxy com filtro
        self.proxy = QSortFilterProxyModel()
        self.proxy.setSourceModel(self.modelo)
        self.proxy.setFilterKeyColumn(0)  # Coluna do nome
        self.proxy.setFilterCaseSensitivity(Qt.CaseInsensitive)

        # Tabela
        self.tabela = QTableView()
        self.tabela.setModel(self.proxy)
        self.tabela.setSortingEnabled(True)
        layout.addWidget(self.tabela)

    def aplicar_filtro(self, texto):
        self.proxy.setFilterRegExp(texto)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    janela = TabelaComFiltro()
    janela.show()
    sys.exit(app.exec_())