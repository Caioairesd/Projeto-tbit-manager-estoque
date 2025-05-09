from tkinter import *
from tkinter import ttk

app = Tk()
app.title("Tabelas")
app.geometry("600x300")

listaNomes = [['1', 'Eberth', 'Front-end'], ['2', 'Daniel', 'DB'], ['3', 'Caio V', 'Back-end'], ['4', 'Kaio G', 'Back-end']]

treeview = ttk.Treeview(app, columns=('id', 'nome', 'funcao'), show='headings', )

treeview.column('id', minwidth=0, width=150)
treeview.column('nome', minwidth=0, width=250)
treeview.column('funcao', minwidth=0, width=150)

treeview.heading('id', text='ID do Escravo')
treeview.heading('nome', text='Nome do Escravo')
treeview.heading('funcao', text='Funcao do Escravo')

treeview.pack()

for lista in listaNomes:
    treeview.insert("", "end", values=(lista))

app.mainloop()