import tkinter as tk
from tkinter import *
from tela_fornecedor_admin import tela_fornecedor_admin
from tela_produto_admin import tela_produto_admin
from tela_funcioario import tela_funcionario

class menu_admin:
    def __init__(self,root):
        self.root = root
        self.root.title("TBit Manager by TerraBytes - Menu Principal - Administrador") 
        self.create_widget()
        self.root.geometry("700x500")
        self.root.resizable( width = False, height = False)

    def create_widget(self):
        registrar_button = tk.Button(text='Registrar Funcionario', width=20, command= tela_funcionario)
        registrar_button.place(x=125, y=80)

        fornecedor_button = tk.Button(text='Fornecedores', width=20, command= tela_fornecedor_admin)
        fornecedor_button.place(x=275, y=80)

        produto_button = tk.Button(text='Produtos', width=20, command= tela_produto_admin)
        produto_button.place(x=425, y=80)

        
if __name__ == '__main__':
    root = tk.Tk()
    app = menu_admin(root)
    root.mainloop()