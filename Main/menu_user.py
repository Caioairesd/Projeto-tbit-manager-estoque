import customtkinter as ctk
from tela_pedido import tela_pedido
from tela_reabastecimento import tela_reabastecimento
from tela_estoque import tela_estoque

class menu_usuario:
    def __init__(self,root):
    
        self.root = root
        self.root.title(" Menu Principal - Usuario") 
        self.root.configure(fg_color='#161B22')
        ctk.set_appearance_mode("dark")

        largura = self.root.winfo_screenwidth()# Expandir tela largura
        altura = self.root.winfo_screenheight()# Expandir tela altura
        self.root.geometry(f"{largura}x{altura}+0+0")# definir expanção

        self.create_widgets()

    def create_widgets(self):

        self.label_text = ctk.CTkLabel(self.root, text="M E N U  P R I N C I P A L ",font=("Garamond", 60), fg_color="#161B22", text_color='#58A6FF') # Cria um label para o texto
        self.label_text.place(relx=0.51, y=60, anchor='center')# Posiciona o texto
      

        self.right_frame = ctk.CTkFrame(self.root, width=400, height=200, fg_color="#2C3E50")# definir o tamanho e cor do fundo da frame
        self.right_frame.place(relx=0.5, y=440, anchor='center')# definir a expanção da frame
        #Criação de botões
        btn_pedido_menu = ctk.CTkButton(self.root,text="Pedido",font=('Arial',13),text_color='#C9D1D9',width=110, height= 45 , fg_color= '#1B263B', bg_color= '#2C3E50',command=self.abrir_tela_pedido)
        btn_reabastecimento = ctk.CTkButton(self.root,text="Reabastecimento",font=('Arial',13),text_color='#C9D1D9',width=110, height= 45 , fg_color= '#1B263B', bg_color= '#2C3E50',command=self.abrir_tela_reabastecimento)
        btn_estoque = ctk.CTkButton(self.root,text="Estoque",font=('Arial',13),text_color='#C9D1D9',width=110, height= 45 , fg_color= '#1B263B', bg_color= '#2C3E50',command=self.abrir_tela_estoque)
        btn_logout = ctk.CTkButton(self.root, text='Voltar',font=('Arial',13),text_color='#C9D1D9', width=90, height= 40,fg_color= '#1B263B', bg_color= '#161B22',command=self.logout_usuario)
        pass
            

        btn_pedido_menu.place(x=775, y=400)
        btn_reabastecimento.place(x=903, y=400)
        btn_estoque.place(x=1035, y=400)
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