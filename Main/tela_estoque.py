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
        self.root.resizable(width=False,height=False)
        
        self.root.transient(root)  # Faz com que a nova janela fique acima da principal
        self.root.grab_set()  # Bloqueia interações na principal até fechar essa

        self.voltar_menu_button = ctk.CTkButton(self.root, text='Voltar', width=20, command=self.voltar_menu)
        self.voltar_menu_button.place(x=800, y=600)

        self.pesquisar_produto = ctk.CTkEntry(self.root, width=350, height=30)
        self.pesquisar_produto.place(x=100, y=250)
        self.pesquisar_produto.bind("<KeyRelease>", self.filtrar_tabela)

        self.criar_tabelao()

    # CONJUNTO DE FUNÇÕES USADOS NO TREEVIEW
    def criar_tabelao(self):
        self.treeview = ttk.Treeview(self.root, columns=("id_produto", "nome_produto", "quantidade_estoque"), show="headings")

        self.treeview.heading("id_produto", text="ID do produto")
        self.treeview.heading("nome_produto", text="Nome do produto")
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
