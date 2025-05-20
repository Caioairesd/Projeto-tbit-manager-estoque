import customtkinter as ctk
from tkinter import messagebox, ttk
from database_geral import consultar_estoque_db, registrar_reabastecimento_db

class tela_reabastecimento:

    def __init__(self,root):
        self.menu_root = root  
        self.root = ctk.CTkToplevel(root)
       
        #Define os parâmetros de interface da janela
        self.root.geometry("900x700")

        self.root.title("TBit Manager - Reabastecimento")
       
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

        self.combobox_produtos = ctk.CTkComboBox(
        self.root,                          # widget pai
        height=30,                          # altura do combobox
        width=180,                          # largura do combobox
        text_color='black',                 # cor do texto e da setinha da direita
        fg_color="#404040",                 # fundo da caixa de seleção
        border_color="#404040",             # cor da borda da caixa
        button_color="#404040",             # fundo da área da setinha
        button_hover_color="lightgray",     # cor de fundo ao passar mouse na setinha
        dropdown_fg_color="gray",           # fundo da lista suspensa
        dropdown_text_color="black",        # cor do texto das opções
        dropdown_hover_color="#404040",     # fundo da opção ao passar o mouse
    
        values=self.produtos_combobox()     # lista de strings pra popular a lista
        )
        self.combobox_produtos.place(x=20, y=20)


        self.pesquisar_produto_entry = ctk.CTkEntry(self.root, height=35, width=250, placeholder_text="Pesquise um produto pelo seu nome...", placeholder_text_color='lightgray')
        self.quantidade_entrou_entry = ctk.CTkEntry(self.root, height=35,border_color='#A0A0A0',placeholder_text='Quantidade...',placeholder_text_color='lightgray',width=150)
        self.novo_reabastecimento_button = ctk.CTkButton(self.root, text="Reabastecimento",fg_color='#404040', text_color='#000', command=self.chamado_reabastecer, height=35, width=50)

        self.pesquisar_produto_entry.bind("<KeyRelease>", self.filtrar_tabela)

        self.combobox_produtos.place(x=100, y=100)
        self.quantidade_entrou_entry.place(x=290, y=100)
        self.novo_reabastecimento_button.place(x=450, y=100)
        self.pesquisar_produto_entry.place(x=100, y=250)

    def criar_tabelao(self):
        style = ttk.Style()
        style.theme_use("alt")
        style.configure("Treeview.Heading", background="gray", foreground="black", anchor="center")
        style.configure("Treeview", background="gray", foreground="black", fieldbackground="gray", rowheight=25)

        self.treeview = ttk.Treeview(self.root, columns=("id_produto", "nome_produto", "categoria_produto", "quantidade_estoque"), show="headings", height=20)

        self.treeview.heading("id_produto",text="ID do produto")
        self.treeview.heading("nome_produto", text="Nome do produto")
        self.treeview.heading("categoria_produto", text="Categoria do produto")
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
                
    # CONJUNTO DE FUNÇÕES USADOS PARA A COMBO BOX
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
