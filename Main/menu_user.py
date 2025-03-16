
import tkinter as tk
from tkinter import *
from tela_fornecedor_user import tela_fornecedor_user
from tela_funcioario import tela_funcionario
from tela_produto_usuario import tela_produto_usuario


class menu_usuario:
    def __init__(self,root):
    
        self.root = root
        self.root.title("TBit Manager by TerraBytes - Menu Principal - Usuario") 
#self.create_widget()
        self.root.geometry("900x700")
        self.root.resizable( width = False, height = False)

        self.create_widgets()

    def create_widgets(self):        
            #Criação de botões
            btn_funcionario_menu = tk.Button(self.root,text="Funcionários",width=15,height=2,command=self.abrir_funcionario)
            btn_produto_menu = tk.Button(self.root,text="Produto",width=15,height=2,command=self.abrir_produto)
            btn_fornecedor_menu = tk.Button(self.root,text="Fornecedores",width=15,height=2,command=self.abrir_fornecedor_user)
            btn_logout_menu = tk.Button(self.root,text="Logout",width=15,height=2,command=self.logout)
            
            pass
            
            btn_funcionario_menu.place(x=550,y=300)
            btn_produto_menu.place(x=300,y=300)
            btn_fornecedor_menu.place(x=50,y=300)
            btn_logout_menu.place(x=700,y=600)
    
    
    def abrir_fornecedor_user(self):
        tela_fornecedor_user(self.root)

    def abrir_funcionario(self):
        tela_funcionario(self.root)

    def abrir_produto(self):
        tela_produto_usuario(self.root)
    
    def logout(self):
        self.root.destroy()

if __name__ == '__main__':
    root = tk.Tk()
    app = menu_usuario(root)
    root.mainloop()

