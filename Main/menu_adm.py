import customtkinter as ctk
from tkinter import messagebox

# Imports das classes que contém as telas
from tela_fornecedor import tela_fornecedor_adm
from tela_produto import tela_produto_adm
from tela_funcionario import tela_funcionario_adm
from tela_cliente import tela_cliente
from tela_estoque import tela_estoque
from tela_pedido import tela_pedido
from tela_reabastecimento import tela_reabastecimento
from tela_dashboard import tela_dashboard

class menu_admin:
    def __init__(self, root):
        self.root = root
        self.root.title("Menu Principal - Administrador                                                                                                                             TBit Manager by TerraBytes") 
        self.root.configure(fg_color='#161B22')                                                                                                                                                                                                   
        ctk.set_appearance_mode('dark')
        
        largura = self.root.winfo_screenwidth()# Expandir tela largura
        altura = self.root.winfo_screenheight()# Expandir tela altura
        self.root.geometry(f"{largura}x{altura}+0+0")# definir expanção

        self.create_widget()

    def create_widget(self):

        self.titulo = ctk.CTkLabel(self.root, text='M E N U  P R I N C I P A L',font=("Garamond", 60), fg_color="#161B22", text_color='#58A6FF') # Cria um label para o usuario
        self.titulo.place(relx=0.5, rely=0.1, anchor='center') # Posiciona o label 
        
        self.button_frame = ctk.CTkFrame(self.root, width=400, height=400, fg_color="#2C3E50")# definir o tamanho e cor do fundo da frame
        self.button_frame.place(relx=0.5, rely=0.5, anchor='center')# definir a expanção da frame

        funcionario_button = ctk.CTkButton(self.button_frame, text='Funcionario', font=('Arial',17),text_color='#C9D1D9',width=110, height= 45 , fg_color= '#1B263B', bg_color= '#2C3E50',command=self.abrir_tela_funcionario)
        funcionario_button.place(x=60, y=70)
        
        fornecedor_button = ctk.CTkButton(self.button_frame, text='Fornecedor', font=('Arial',17),text_color='#C9D1D9',width=110, height= 45, fg_color= '#1B263B', bg_color= '#2C3E50',command=self.abrir_tela_fornecedor_admin)
        fornecedor_button.place(x=60, y=140)

        produto_button = ctk.CTkButton(self.button_frame, text='Produtos', font=('Arial',17),text_color='#C9D1D9',width=110, height= 45, fg_color= '#1B263B', bg_color= '#2C3E50',command=self.abrir_tela_produto_admin)
        produto_button.place(x=60, y=210)

        cliente_button = ctk.CTkButton(self.button_frame, text='Cliente', font=('Arial',17),text_color='#C9D1D9',width=110, height= 45, fg_color= '#1B263B', bg_color= '#2C3E50',command=self.abrir_tela_cliente)
        cliente_button.place(x=60, y=280)
        
        estoque_button = ctk.CTkButton(self.button_frame, text='Estoque', font=('Arial',17),text_color='#C9D1D9',width=110, height= 45, fg_color= '#1B263B', bg_color= '#2C3E50',command=self.abrir_tela_estoque)
        estoque_button.place(x=220, y=70)

        pedido_button = ctk.CTkButton(self.button_frame, text='Pedido', font=('Arial',17),text_color='#C9D1D9',width=110, height= 45, fg_color= '#1B263B', bg_color= '#2C3E50',command=self.abrir_tela_pedido)
        pedido_button.place(x=220, y=140)

        reabastecimento_button = ctk.CTkButton(self.button_frame, text='Reabastecimento',font=('Arial',13),text_color='#C9D1D9', width=70, fg_color= '#1B263B', bg_color= '#2C3E50',height= 45, command=self.abrir_tela_reabastecimento)
        reabastecimento_button.place(x=220, y=210)

        dashboard_button = ctk.CTkButton(self.button_frame, text='Dashboard', font=('Arial',17),text_color='#C9D1D9',width=110, height= 45,fg_color= '#1B263B', bg_color= '#2C3E50', command=self.abrir_tela_dashboard)
        dashboard_button.place(x=220, y=280)

        logout_button = ctk.CTkButton(self.root, text='Voltar',font=('Arial',13),text_color='#C9D1D9', width=90, height= 40,fg_color= '#1B263B', bg_color= '#161B22', command=self.logout_admin)
        logout_button.place(relx=0.95, rely=0.95, anchor='se')

        
    # Classes responsáveis pelas transições de telas, atribuindo root
    def abrir_tela_funcionario(self):
        tela_funcionario_adm(self.root)
        self.root.withdraw()

    def abrir_tela_produto_admin(self):
        tela_produto_adm(self.root)
        self.root.withdraw()

    def abrir_tela_fornecedor_admin(self):
        tela_fornecedor_adm(self.root)
        self.root.withdraw()       

    def abrir_tela_cliente(self):
        tela_cliente(self.root)
        self.root.withdraw()

    def abrir_tela_estoque(self):
        tela_estoque(self.root)
        self.root.withdraw()

    def abrir_tela_pedido(self):
        tela_pedido(self.root)
        self.root.withdraw()

    def abrir_tela_reabastecimento(self):
        tela_reabastecimento(self.root)
        self.root.withdraw()

    def abrir_tela_dashboard(self):
        tela_dashboard(self.root)
        self.root.withdraw()
        
    def logout_admin(self):
        confirmacao = messagebox.askyesno("Confirmação", "Você deseja sair da conta e voltar ao menu de login?")
        
        if confirmacao == True:
            from main_menu import login_menu
            root = ctk.CTk()
            app = login_menu(root)
            self.root.destroy()
            root.mainloop()    

if __name__ == '__main__':
    root = ctk.CTk()
    app = menu_admin(root)
    root.mainloop()