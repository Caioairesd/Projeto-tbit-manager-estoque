from tkinter import *
from tkintertable import TableCanvas, TableModel

# Janela principal
root = Tk()
root.geometry("600x400")
root.title("Tabela com tkintertable")

# Frame para colocar a tabela
frame = Frame(root)
frame.pack(fill=BOTH, expand=1)

# Modelo de dados
dados = {
    '1': {'Nome': 'Ana', 'Idade': 25, 'Profissão': 'Engenheira'},
    '2': {'Nome': 'João', 'Idade': 30, 'Profissão': 'Médico'},
    '3': {'Nome': 'Maria', 'Idade': 22, 'Profissão': 'Estudante'},
    '4': {'Nome': 'Carlos', 'Idade': 28, 'Profissão': 'Designer'}
}

# Criando o modelo da tabela
model = TableModel()
model.importDict(dados)

# Criando a tabela e inserindo no frame
tabela = TableCanvas(frame, model=model, editable=True)
tabela.show()

root.mainloop()