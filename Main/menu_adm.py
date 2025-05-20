import customtkinter as ctk

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
        self.root.title("Menu Principal - Administrador                                                                                                                                                                                                     TBit Manager by TerraBytes") 
        ctk.set_appearance_mode('dark')
        
        self.root.configure(fg_color='#161B22')
        
        largura = self.root.winfo_screenwidth()# Expandir tela largura
        altura = self.root.winfo_screenheight()# Expandir tela altura
        self.root.geometry(f"{largura}x{altura}+0+0")# definir expanção

        self.create_widget()
    def create_widget(self):

        self.titulo = ctk.CTkLabel(self.root, text='M E N U  P R I N C I P A L',font=("Garamond", 60), fg_color="#161B22", text_color='#58A6FF') # Cria um label para o usuario
        self.titulo.place(x=630, y=60) # Posiciona o label 
        
        self.right_frame = ctk.CTkFrame(self.root, width=400, height=400, fg_color="#2C3E50")# definir o tamanho e cor do fundo da frame
        self.right_frame.place(x=725, y=350)# definir a expanção da frame

        funcionario_button = ctk.CTkButton(self.root, text='Funcionario', font=('Arial',17),text_color='#C9D1D9',width=110, height= 45 , fg_color= '#1B263B', bg_color= '#2C3E50',command=self.abrir_tela_funcionario)
        funcionario_button.place(x=760, y=400)
        
        fornecedor_button = ctk.CTkButton(self.root, text='Fornecedor', font=('Arial',17),text_color='#C9D1D9',width=110, height= 45, fg_color= '#1B263B', bg_color= '#2C3E50',command=self.abrir_tela_fornecedor_admin)
        fornecedor_button.place(x=760, y=460)

        produto_button = ctk.CTkButton(self.root, text='Produtos', font=('Arial',17),text_color='#C9D1D9',width=110, height= 45, fg_color= '#1B263B', bg_color= '#2C3E50',command=self.abrir_tela_produto_admin)
        produto_button.place(x=760, y=520)

        cliente_button = ctk.CTkButton(self.root, text='Cliente', font=('Arial',17),text_color='#C9D1D9',width=110, height= 45, fg_color= '#1B263B', bg_color= '#2C3E50',command=self.abrir_tela_cliente)
        cliente_button.place(x=760, y=580)
        
        estoque_button = ctk.CTkButton(self.root, text='Estoque', font=('Arial',17),text_color='#C9D1D9',width=110, height= 45, fg_color= '#1B263B', bg_color= '#2C3E50',command=self.abrir_tela_estoque)
        estoque_button.place(x=980, y=400)

        pedido_button = ctk.CTkButton(self.root, text='Pedido', font=('Arial',17),text_color='#C9D1D9',width=110, height= 45, fg_color= '#1B263B', bg_color= '#2C3E50',command=self.abrir_tela_pedido)
        pedido_button.place(x=980, y=460)

        reabastecimento_button = ctk.CTkButton(self.root, text='Reabastecimento',font=('Arial',13),text_color='#C9D1D9', width=70, fg_color= '#1B263B', bg_color= '#2C3E50',height= 45, command=self.abrir_tela_reabastecimento)
        reabastecimento_button.place(x=980, y=520)

        dashboard_button = ctk.CTkButton(self.root, text='Dashboard', font=('Arial',17),text_color='#C9D1D9',width=110, height= 45,fg_color= '#1B263B', bg_color= '#2C3E50', command=self.abrir_tela_dashboard)
        dashboard_button.place(x=980, y=580)

        logout_button = ctk.CTkButton(self.root, text='Voltar',font=('Arial',13),text_color='#C9D1D9', width=90, height= 40,fg_color= '#1B263B', bg_color= '#161B22', command=self.logout_admin)
        logout_button.place(x=1700, y=900)

        
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