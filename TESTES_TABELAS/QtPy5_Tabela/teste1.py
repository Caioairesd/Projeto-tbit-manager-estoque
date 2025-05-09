import sys
from PyQt5.QtWidgets import *

app = QApplication(sys.argv)

widget = QWidget()
widget.setWindowTitle("Primeiro teste")
widget.resize(600, 600)

label = QLabel("Olá, de novo, abu, teste", parent=widget)
label.move(150, 150)

combobox = QComboBox(parent=widget)
combobox.insertItem(1, "Teste 1")
combobox.insertItem(2, "Teste 2")
combobox.move(140, 170)

table = QTableView(parent=widget)

widget.show()
sys.exit(app.exec_())

