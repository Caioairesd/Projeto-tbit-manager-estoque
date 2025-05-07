import tkinter as tk
#from tkinter import *
import customtkinter as ctk
from Main.tela_fornecedor_adm import tela_fornecedor_user
from Main.tela_funcionario_adm import tela_funcionario_admin
from Main.tela_produto_adm import tela_produto_usuario


class menu_usuario:
    def __init__(self,root):
    
        self.root = root
        self.root.title("TBit Manager by TerraBytes - Menu Principal - Usuario") 
#self.create_widget()
        self.root.geometry("900x700")
        #self.root.config(fg_color="black")
        self.root.resizable( width = False, height = False)

        self.create_widgets()

    def create_widgets(self):        
            #Criação de botões
            btn_produto_menu = ctk.CTkButton(self.root,text="Produto",width=15,height=2,command=self.abrir_produto)
            btn_fornecedor_menu = ctk.CTkButton(self.root,text="Fornecedores",width=15,height=2,command=self.abrir_fornecedor_user)
            btn_logout = ctk.CTkButton(self.root, text='Logout', width=18, command=self.logout_usuario)
            
            pass
            
            btn_produto_menu.place(x=300,y=300)
            btn_fornecedor_menu.place(x=450,y=300)
            btn_logout.place(x=400, y=580)
    
    
    def abrir_fornecedor_user(self):
        tela_fornecedor_user(self.root)

    def abrir_funcionario(self):
        tela_funcionario_admin(self.root)

    def abrir_produto(self):
        tela_produto_usuario(self.root)
    
    def logout_usuario(self):
        from main_menu import login_menu
        menu = ctk.CTk()
        app = login_menu(menu)
        self.root.destroy()
        menu.mainloop()
