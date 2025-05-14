#import tkinter as tk
#from tkinter import *
import customtkinter as ctk
from tela_pedido import tela_pedido
from tela_reabastecimento import tela_reabastecimento
from tela_estoque import tela_estoque

class menu_usuario:
    def __init__(self,root):
    
        self.root = root
        self.root.title(" Menu Principal - Usuario") 
        #self.create_widget()
        self.root.configure(fg_color="gray")
        self.root.geometry("600x400")
        self.root.resizable( width = False, height = False)

        #self.create_widget()
        #ctk.set_appearance_mode("dark")
        ctk.set_default_color_theme("dark-blue")  # ou "green", "dark-blue"

        self.create_widgets()

    def create_widgets(self):  
        

        
        #Criação de botões
        btn_pedido_menu = ctk.CTkButton(self.root,text="Pedido",text_color= 'black',width=80,fg_color= '#D3D3D3',height=35,command=self.abrir_tela_pedido)
        btn_reabastecimento = ctk.CTkButton(self.root,text="Reabastecimento",text_color= 'black',width=80,fg_color= '#D3D3D3',height=35,command=self.abrir_tela_reabastecimento)
        btn_estoque = ctk.CTkButton(self.root,text="Estoque",text_color= 'black',width=80,height=35,fg_color= '#D3D3D3',command=self.abrir_tela_estoque)
        btn_logout = ctk.CTkButton(self.root, text='Logout', text_color= 'black',width=80,height=35,fg_color= 'darkgray',command=self.logout_usuario)
        pass
            

        btn_pedido_menu.place(x=100, y=120)
        btn_reabastecimento.place(x=100, y=160)
        btn_estoque.place(x=100, y=200)
        btn_logout.place(x=500, y=345)
    
    
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
    
if __name__ == '__main__':
    root = ctk.CTk()
    app = menu_usuario(root)
    root.mainloop()