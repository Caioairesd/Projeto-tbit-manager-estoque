#import tkinter as tk
#from tkinter import *
import customtkinter as ctk
from tela_pedido import tela_pedido
from tela_reabastecimento import tela_reabastecimento
from tela_estoque import tela_estoque



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
        btn_pedido_menu = ctk.CTkButton(self.root,text="Pedido",width=15,height=2,command=self.abrir_tela_pedido)
        btn_reabastecimento = ctk.CTkButton(self.root,text="Reabastecimento",width=15,height=2,command=self.abrir_tela_reabastecimento)
        btn_estoque = ctk.CTkButton(self.root,text="Estoque",width=15,height=2,command=self.abrir_tela_estoque)
        btn_logout = ctk.CTkButton(self.root, text='Logout', width=18, command=self.logout_usuario)
            
        pass
            
        btn_pedido_menu.place(x=275, y=120)
        btn_reabastecimento.place(x=275, y=160)
        btn_estoque.place(x=275, y=200)
        btn_logout.place(x=600, y=400)
    
    
    def abrir_tela_pedido(self):
        tela_pedido(self.root)
        self.root.withdraw()

    def abrir_tela_reabastecimento(self):
        tela_reabastecimento(self.root)
        self.root.withdraw()

    def abrir_tela_estoque(self):
        tela_estoque(self.root)
        self.root.withdraw()



    def logout_usuario(self):
        from main_menu import login_menu
        menu = ctk.CTk()
        app = login_menu(menu)
        self.root.destroy()
        menu.mainloop()
