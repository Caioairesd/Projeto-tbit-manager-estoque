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
        self.root.title("Menu Principal - Administrador                                                                                                                                                                                                     TBit Manager by TerraBytes") 
        ctk.set_appearance_mode('dark')
        self.create_widget()
        self.root.configure(fg_color="#A0A0A0")

        largura = self.root.winfo_screenwidth()# Expandir tela largura
        altura = self.root.winfo_screenheight()# Expandir tela altura
        self.root.geometry(f"{largura}x{altura}+0+0")# definir expanção


    def create_widget(self):

        
        

        self.titulo = ctk.CTkLabel(self.root, text='M E N U  P R I N C I P A L - A D M I N I S T R A D O R',font=("Garamond", 60), fg_color="#A0A0A0", text_color='black') # Cria um label para o usuario
        self.titulo.place(x=280, y=60) # Posiciona o label 
        
        self.right_frame = ctk.CTkFrame(self.root, width=500, height=500, fg_color="gray")# definir o tamanho e cor do fundo da frame
        self.right_frame.place(x=700, y=350)# definir a expanção da frame




        funcionario_button = ctk.CTkButton(self.root, text='Funcionario', text_color='black',width=80, height= 40, fg_color= '#404040', bg_color= 'gray',command=self.abrir_tela_funcionario)
        funcionario_button.place(x=740, y=40)
        
        fornecedor_button = ctk.CTkButton(self.root, text='Fornecedor', text_color='black',width=80, height= 40, fg_color= '#404040', bg_color= 'gray',command=self.abrir_tela_fornecedor_admin)
        fornecedor_button.place(x=275, y=80)

        produto_button = ctk.CTkButton(self.root, text='Produtos', text_color='black',width=80, height= 40, fg_color= '#404040', bg_color= 'gray',command=self.abrir_tela_produto_admin)
        produto_button.place(x=275, y=120)

        cliente_button = ctk.CTkButton(self.root, text='Cliente', text_color='black',width=80, height= 40, fg_color= '#404040', bg_color= 'gray',command=self.abrir_tela_cliente)
        cliente_button.place(x=275, y=160)
        
        estoque_button = ctk.CTkButton(self.root, text='Estoque', text_color='black',width=80, height= 40, fg_color= '#404040', bg_color= 'gray',command=self.abrir_tela_estoque)
        estoque_button.place(x=275, y=200)

        pedido_button = ctk.CTkButton(self.root, text='Pedido', text_color='black',width=80, height= 40, fg_color= '#404040', bg_color= 'gray',command=self.abrir_tela_pedido)
        pedido_button.place(x=275, y=240)

        reabastecimento_button = ctk.CTkButton(self.root, text='Reabastecimento',text_color='black', width=80, fg_color= '#404040', bg_color= 'gray',height= 40, command=self.abrir_tela_reabastecimento)
        reabastecimento_button.place(x=275, y=280)

        dashboard_button = ctk.CTkButton(self.root, text='Dashboard', text_color='black',width=80, height= 40,fg_color= '#404040', bg_color= 'gray', command=self.abrir_tela_dashboard)
        dashboard_button.place(x=275, y=320)

        logout_button = ctk.CTkButton(self.root, text='Logout',text_color='black', width=100, height= 40,fg_color= '#404040', bg_color= 'gray', command=self.logout_admin)
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