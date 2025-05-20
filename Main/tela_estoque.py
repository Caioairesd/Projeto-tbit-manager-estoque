import customtkinter as ctk
from tkinter import ttk
from database_geral import consultar_estoque_db

class tela_estoque:

    def __init__(self,root):
        self.menu_root = root  
        self.root = ctk.CTkToplevel(root)

        #Define os parâmetros de interface da janela
        self.root.geometry("900x700")
       
        self.root.title("TBit Manager - Estoque")
      
        self.root.configure(fg_color="#A0A0A0")

        ctk.set_appearance_mode("dark")# Deixar o frame no modo escuro-dark

        largura = self.root.winfo_screenwidth()# Expandir tela largura
        altura = self.root.winfo_screenheight()# Expandir tela altura
        self.root.geometry(f"{largura}x{altura}+0+0")# definir expanção
        
        self.root.grab_set()  # Bloqueia interações na principal até fechar essa

        self.create_widgets()
        self.criar_tabelao()

    def create_widgets(self):
        self.voltar_menu_button = ctk.CTkButton(self.root, text='Voltar',text_color='black', width=90, height= 40,fg_color= '#404040', bg_color= 'gray', command=self.voltar_menu)
        self.voltar_menu_button.place(x=1700, y=900)

        self.pesquisar_produto = ctk.CTkEntry(self.root, width=350, height=30)
        self.pesquisar_produto.place(x=100, y=250)
        self.pesquisar_produto.bind("<KeyRelease>", self.filtrar_tabela)

    # CONJUNTO DE FUNÇÕES USADOS NO TREEVIEW
    def criar_tabelao(self):
        self.treeview = ttk.Treeview(self.root, columns=("id_produto", "nome_produto", "categoria_estoque", "quantidade_estoque"), show="headings")

        self.treeview.heading("id_produto", text="ID do produto")
        self.treeview.heading("nome_produto", text="Nome do produto")
        self.treeview.heading("categoria_estoque", text="Categoria do produto")
        self.treeview.heading("quantidade_estoque", text="Quantidade em estoque")

        estoque = consultar_estoque_db()
        for produto in estoque:
            self.treeview.insert("", "end", values=produto)
        
        self.treeview.place(x=100, y=300)

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
