import tkinter as tk 
from tkinter import *
from tela_fornecedor_admin import tela_fornecedor_admin
from tela_produto_admin import tela_produto_admin
from tela_funcionario import tela_funcionario_admin

class menu_admin:
    def __init__(self, root):
        self.root = root
        self.root.title("TBit Manager by TerraBytes - Menu Principal - Administrador") 
        self.create_widget()
        self.root.geometry("700x500")
        self.root.config(bg="#003366")
        self.root.resizable(width=False, height=False)

    def create_widget(self):
        registrar_button = tk.Button(self.root, text='Registrar Funcionario', width=20, command=self.button_tela_funcionario)
        registrar_button.place(x=125, y=80)

        #logo = PhotoImage(file='icon/tbit_logo_256x.png')
        #self.logo_label = tk.Label(self.root, image=logo) # Cria uma label que carrega a logo
        #self.logo_label.place(x=50, y=100) # Posiciona o label no frame esquerdo
        
        fornecedor_button = tk.Button(self.root, text='Fornecedores', width=20, command=self.button_tela_fornecedor_admin)
        fornecedor_button.place(x=275, y=80)

        produto_button = tk.Button(self.root, text='Produtos', width=20, command=self.button_tela_produto_admin)
        produto_button.place(x=425, y=80)

        logout_button = tk.Button(self.root, text='Logout', width=18, command=self.logout_admin)
        logout_button.place(x=300, y=250)

    # CLASSES CRIADAS PARA PASSAR O ROOT AS CLASSES QUE IMPORTAMOS
    def button_tela_funcionario(self):
        tela_funcionario_admin(self.root)
        
    def button_tela_produto_admin(self):
        tela_produto_admin(self.root)
    
    def button_tela_fornecedor_admin(self):
        tela_fornecedor_admin(self.root)

    def logout_admin(self):
        from main_menu import login_menu
        menu = tk.Tk()
        app = login_menu(menu)
        self.root.destroy()