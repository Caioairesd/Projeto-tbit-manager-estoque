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
        self.root.configure(fg_color="#A0A0A0")

        
        largura = self.root.winfo_screenwidth()# Expandir tela largura
        altura = self.root.winfo_screenheight()# Expandir tela altura
        self.root.geometry(f"{largura}x{altura}+0+0")# definir expanção

        ctk.set_appearance_mode("dark")


        self.create_widgets()

    def create_widgets(self):

        self.label_text = ctk.CTkLabel(self.root, text="M E N U  P R I N C I P A L - U S U Á R I O",font=("Garamond", 60), fg_color="#A0A0A0", text_color='black') # Cria um label para o texto
        self.label_text.place(x=400, y=60) # Posiciona o texto
      

        self.right_frame = ctk.CTkFrame(self.root, width=400, height=300, fg_color="gray")# definir o tamanho e cor do fundo da frame
        self.right_frame.place(x=750, y=325)# definir a expanção da frame
        #Criação de botões
        btn_pedido_menu = ctk.CTkButton(self.root,text="Pedido",text_color= 'black',width=90,fg_color= '#404040',bg_color='gray',height=40,command=self.abrir_tela_pedido)
        btn_reabastecimento = ctk.CTkButton(self.root,text="Reabastecimento",text_color= 'black',width=90,fg_color= '#404040',bg_color='gray',height=40,command=self.abrir_tela_reabastecimento)
        btn_estoque = ctk.CTkButton(self.root,text="Estoque",text_color= 'black',width=90,height=40,fg_color= '#404040',bg_color='gray',command=self.abrir_tela_estoque)
        btn_logout = ctk.CTkButton(self.root, text='Voltar', text_color= 'black',width=90,height=40,fg_color= '#404040',command=self.logout_usuario)
        pass
            

        btn_pedido_menu.place(x=800, y=400)
        btn_reabastecimento.place(x=800, y=450)
        btn_estoque.place(x=800, y=500)
        btn_logout.place(x=1700, y=900)
    
    
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