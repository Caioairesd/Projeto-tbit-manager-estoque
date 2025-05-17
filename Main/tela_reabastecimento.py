import customtkinter as ctk
from tkinter import messagebox
from database_geral import consultar_estoque_db, registrar_reabastecimento_db
from tkinter import ttk

class tela_reabastecimento:

    def __init__(self,root):
        self.menu_root = root  
        self.root = ctk.CTkToplevel(root)

        #Define os parâmetros de interface da janela
        self.root.geometry("900x700")

        self.root.title("TBit Manager - Reabastecimento")
        self.root.resizable(width=False,height=False)
        
        self.root.transient(root)  # Faz com que a nova janela fique acima da principal
        self.root.grab_set()  # Bloqueia interações na principal até fechar essa

        self.voltar_menu_button = ctk.CTkButton(self.root, text='Voltar', width=20, command=self.voltar_menu)
        self.voltar_menu_button.place(x=800, y=600)

        # ELEMENTOS NÃO POSICIONADOS, SOMENTE CRIADOS PARA DESENVOLVIMENTO DO BACK
        self.combobox_produtos = ctk.CTkComboBox(self.root, height=30, width=180, values=self.produtos_combobox())
        self.pesquisar_produto_entry = ctk.CTkEntry(self.root, height=30, width=250, placeholder_text="Pesquise um produto pelo seu nome...")
        self.quantidade_entrou_entry = ctk.CTkEntry(self.root, height=30, width=150)
        self.novo_reabastecimento_button = ctk.CTkButton(self.root, text="Novo Reabastecimento", command=self.chamado_reabastecer, height=30, width=120)

        self.pesquisar_produto_entry.bind("<KeyRelease>", self.filtrar_tabela)

        self.combobox_produtos.place(x=150, y=100)
        self.quantidade_entrou_entry.place(x=350, y=100)
        self.novo_reabastecimento_button.place(x=550, y=100)
        self.pesquisar_produto_entry.place(x=100, y=260)
        
        self.criar_tabelao()

    def criar_tabelao(self):
        self.treeview = ttk.Treeview(self.root, columns=("id_produto", "nome_produto", "quantidade_estoque"), show="headings", height=15)

        self.treeview.heading("id_produto", text="ID do produto")
        self.treeview.heading("nome_produto", text="Nome do produto")
        self.treeview.heading("quantidade_estoque", text="Quantidade em estoque")

        estoque = consultar_estoque_db()
        for produto in estoque:
            self.treeview.insert("", "end", values=produto)
        
        self.treeview.bind("<ButtonRelease-1>", self.click_na_linha)

        self.treeview.place(x=100, y=300)

    def atualizar_tabela(self, produtos):
         for item in self.treeview.get_children():
            self.treeview.delete(item)

         for produto in produtos:
            self.treeview.insert("", "end", values=produto)

    def filtrar_tabela(self, event):
        estoque = consultar_estoque_db()
        produto_pesquisado = self.pesquisar_produto_entry.get().lower()

        filtragem = [produto for produto in estoque if produto_pesquisado in produto[1].lower()]

        self.atualizar_tabela(filtragem)
    
    def click_na_linha(self, event):
        linha_selecionada = self.treeview.focus()

        if linha_selecionada:
            valores = self.treeview.item(linha_selecionada, "values")
            if valores:
                self.combobox_produtos.set(valores[1])
                
    def produtos_combobox(self):
        estoque = consultar_estoque_db()
        nomes_produtos = [nome[1] for nome in estoque]
        return nomes_produtos

    def get_id_produto(self):
        produto_selecionado = self.combobox_produtos.get()
        busca = consultar_estoque_db()

        for produto in busca:
            if produto_selecionado == produto[1]:
                id_produto = produto[0]
                return id_produto

    def chamado_reabastecer(self):
        quantidade = self.quantidade_entrou_entry.get()
        id_produto = self.get_id_produto()

        if id_produto and quantidade:
                registrar_reabastecimento_db(id_produto, quantidade)
                messagebox.showinfo("Sucesso", "Chamado cadastrado! Banco de dados atualizando...")

                estoque = consultar_estoque_db()
                self.atualizar_tabela(estoque)

                self.pesquisar_produto_entry.delete(0, ctk.END)
                self.quantidade_entrou_entry.delete(0, ctk.END)
        else:
            messagebox.showerror("Error", "Ocorreu um erro na tentativa de cadastrar novo chamado!")

    def voltar_menu(self):
        
       # from menu_adm import menu_admin
        self.root.destroy()  # Fecha a janela atual
        self.menu_root.deiconify()
    
if __name__ == "__main__":
    root = ctk.CTk()
    app = tela_reabastecimento(root)
    root.mainloop()
