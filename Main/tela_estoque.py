import customtkinter as ctk
from tkinter import ttk
from database_geral import consultar_estoque_db

class tela_estoque:

    def __init__(self,root):
        self.menu_root = root  
        self.root = ctk.CTkToplevel(root)
        self.root.title("TBit Manager - Estoque")
      
        self.root.configure(fg_color='#161B22')

        #ctk.set_appearance_mode("dark")# Deixar o frame no modo escuro-dark

        largura = self.root.winfo_screenwidth()# Expandir tela largura
        altura = self.root.winfo_screenheight()# Expandir tela altura
        self.root.geometry(f"{largura}x{altura}+0+0")# definir expanção
        
        self.root.grab_set()  # Bloqueia interações na principal até fechar essa

        self.create_widgets()
        self.criar_tabelao()

    def create_widgets(self):

        # Título
        self.titulo = ctk.CTkLabel(self.root, text="E S T O Q U E ", font=("Garamond", 60),fg_color="#161B22", text_color="#58A6FF")
        self.titulo.place(relx=0.5, y=60, anchor="center")

        self.voltar_menu_button = ctk.CTkButton(self.root, text='Voltar', font=('Arial',13),text_color='#C9D1D9', fg_color= '#1B263B', bg_color= '#121B22', width=90, height=40, command=self.voltar_menu)
        self.voltar_menu_button.place(x=1700, y=900)

        self.pesquisar_produto = ctk.CTkEntry(self.root, placeholder_text='buscar produto...',placeholder_text_color='#C9D1D9', text_color='#C9D1D9', fg_color='#1B263B', bg_color='#1B263B',width=200, height=30)
        self.pesquisar_produto.place(x=660, y=250)
        self.pesquisar_produto.bind("<KeyRelease>", self.filtrar_tabela)

        #labels
        self.titulo = ctk.CTkLabel(self.root, text='Pesquisar :',font=("Garamond", 20), fg_color="#161B22", text_color='#C9D1D9') # Cria um label para o usuario
        self.titulo.place(x=560, y=250) # Posiciona o label 


    # CONJUNTO DE FUNÇÕES USADOS NO TREEVIEW
    def criar_tabelao(self):
        style = ttk.Style()
        style.theme_use("alt")
        style.configure("Treeview.Heading", background="#1B263B", foreground="#C9D1D9", anchor="center")
        style.configure("Treeview", background="#2C3E50", foreground="#C9D1D9", fieldbackground="gray", rowheight=25)

        self.treeview = ttk.Treeview(self.root, columns=("id_produto", "nome_produto", "categoria_estoque", "quantidade_estoque"), show="headings")

        self.treeview.heading("id_produto", text="ID do produto")
        self.treeview.heading("nome_produto", text="Nome do produto")
        self.treeview.heading("categoria_estoque", text="Categoria do produto")
        self.treeview.heading("quantidade_estoque", text="Quantidade em estoque")

        estoque = consultar_estoque_db()
        for produto in estoque:
            self.treeview.insert("", "end", values=produto)

        self.treeview.place(relx=0.5, y=510, anchor='center', height=400)

    def atualizar_tabela(self, produtos):
         for item in self.treeview.get_children():
            self.treeview.delete(item)

         for produto in produtos:
            self.treeview.insert("", "end", values=produto)

    def filtrar_tabela(self, event):
        estoque = consultar_estoque_db()
        produto_pesquisado = self.pesquisar_produto.get().lower()

        filtragem = [produto for produto in estoque if produto_pesquisado in produto[1].lower()]

        self.atualizar_tabela(filtragem)
    # FIM DO CONJUNTO

    def voltar_menu(self):
        
       # from menu_adm import menu_admin
        self.root.destroy()  # Fecha a janela atual
        self.menu_root.deiconify()
        
if __name__ == "__main__":
    root = ctk.CTk()
    app = tela_estoque(root)
    root.mainloop()