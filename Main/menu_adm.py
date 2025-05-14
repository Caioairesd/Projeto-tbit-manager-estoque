import customtkinter as ctk

# Imports das classes que contém as telas
from tela_fornecedor_adm import tela_fornecedor_adm
from tela_produto_adm import tela_produto_adm
from tela_funcionario_adm import tela_funcionario_adm
from tela_cliente import tela_cliente
from tela_estoque import tela_estoque
from tela_pedido import tela_pedido
from tela_reabastecimento import tela_reabastecimento
from tela_dashboard import tela_dashboard

class menu_admin:
    def __init__(self, root):
        self.root = root
        self.root.title("Menu Principal - Administrador                                                                   TBit Manager by TerraBytes") 
        self.create_widget()
        self.root.geometry("700x500")
         #self.root.geometry(f"{largura}x{altura}+0+0") 
        self.root.resizable(width=False, height=False)

    def create_widget(self):

        funcionario_button = ctk.CTkButton(self.root, text='Funcionario', width=20, command=self.abrir_tela_funcionario)
        funcionario_button.place(x=275, y=40)
        
        fornecedor_button = ctk.CTkButton(self.root, text='Fornecedor', width=80, height= 30, command=self.abrir_tela_fornecedor_admin)
        fornecedor_button.place(x=275, y=80)

        produto_button = ctk.CTkButton(self.root, text='Produtos', width=80, height= 30, command=self.abrir_tela_produto_admin)
        produto_button.place(x=275, y=120)

        cliente_button = ctk.CTkButton(self.root, text='Cliente', width=80, height= 30, command=self.abrir_tela_cliente)
        cliente_button.place(x=275, y=160)
        
        estoque_button = ctk.CTkButton(self.root, text='Estoque', width=80, height= 30, command=self.abrir_tela_estoque)
        estoque_button.place(x=275, y=200)

        pedido_button = ctk.CTkButton(self.root, text='Pedido', width=80, height= 30, command=self.abrir_tela_pedido)
        pedido_button.place(x=275, y=240)

        reabastecimento_button = ctk.CTkButton(self.root, text='Reabastecimento', width=80, height= 30, command=self.abrir_tela_reabastecimento)
        reabastecimento_button.place(x=275, y=280)

        dashboard_button = ctk.CTkButton(self.root, text='Dashboard', width=80, height= 30, command=self.abrir_tela_dashboard)
        dashboard_button.place(x=275, y=320)

        logout_button = ctk.CTkButton(self.root, text='Logout', width=80, height= 30, command=self.logout_admin)
        logout_button.place(x=600, y=400)

        

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
        from main_menu import login_menu
        root = ctk.CTk()
        app = login_menu(root)
        self.root.destroy()
        root.mainloop()    

if __name__ == '__main__':
    root = ctk.CTk()
    app = menu_admin(root)
    root.mainloop()