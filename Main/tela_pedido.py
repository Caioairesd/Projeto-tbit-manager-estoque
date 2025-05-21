import customtkinter as ctk
from datetime import date
from tkinter import ttk, messagebox
from database_geral import get_pedidos_db, fazer_pedido_db, get_id_nome_clientes_db, get_id_nome_produtos_db

class tela_pedido:

    def __init__(self,root):
        self.menu_root = root  
        self.root = ctk.CTkToplevel(root)
        self.root.configure(fg_color='#141C29')

        #ctk.set_appearance_mode("dark")# Deixar o frame no modo escuro-dark

        largura = self.root.winfo_screenwidth()# Expandir tela largura
        altura = self.root.winfo_screenheight()# Expandir tela altura
        self.root.geometry(f"{largura}x{altura}+0+0")# definir expanção
        
        self.root.title("TBit Manager - Pedido")
        self.root.grab_set()  # Bloqueia interações na principal até fechar essa

        self.create_widgets()
        self.root.after(200, self.criar_tabelao)  # Garante que a tabela é criada depois que a janela estiver pronta

    def create_widgets(self):

        self.titulo = ctk.CTkLabel(self.root, text='P E D I D O ',font=("Garamond", 60), fg_color="#141C29", text_color='#58A6FF') # Cria um label para o usuario
        self.titulo.place(x=820, y=60) # Posiciona o label do titulo
        
        #cria o frame como fundo para deixar um fundo para as labls e caixas de textos
        self.right_frame = ctk.CTkFrame(self.root, width=700, height=400, fg_color="#2C3E50")# definir o tamanho e cor do fundo da frame
        self.right_frame.place(x=150, y=300)# definir a expanção da frame


        self.voltar_menu_button = ctk.CTkButton(self.root, text='Voltar',font=('Arial',13),text_color='#C9D1D9', width=90, height= 40,fg_color= '#1B263B', bg_color= '#161B22', command=self.voltar_menu)
        self.voltar_menu_button.place(x=1700, y=900)

        self.fazer_pedido_button = ctk.CTkButton(self.root, text="Novo pedido",text_color='#C9D1D9', fg_color='#1B263B',bg_color='#2C3E50', width=40,height=35, command=self.fazer_pedido)
        self.fazer_pedido_button.place(x=580, y=470)

        self.nome_produto_entry = ctk.CTkEntry(self.root, placeholder_text="Pesquisar produto...", text_color='#C9D1D9', fg_color='#1B263B', bg_color='#2C3E50', width=200, height=30)
        self.nome_produto_entry.place(x=350, y=410)
        self.nome_produto_entry.bind("<KeyRelease>", self.filtrar_nomes_produtos)

        self.nome_cliente_entry = ctk.CTkEntry(self.root, placeholder_text="Pesquisar cliente...", text_color='#C9D1D9', fg_color='#1B263B', bg_color='#2C3E50',width=200, height=30)
        self.nome_cliente_entry.place(x=350, y=350)
        self.nome_cliente_entry.bind("<KeyRelease>", self.filtrar_nomes_clientes)

        self.nome_produto_combobox = ctk.CTkComboBox(self.root, values=self.listar_produtos(),width=140, height=30, fg_color='#1B263B', dropdown_hover_color='#1B263B', dropdown_text_color='#C9D1D9',dropdown_fg_color="#161B22", text_color="#C9D1D9", button_color="#1B263B", button_hover_color="#1B263B",border_width=0, bg_color='#1B263B')
        self.nome_produto_combobox.place(x=580, y=410)

        self.nome_cliente_combobox = ctk.CTkComboBox(self.root, values=self.listar_clientes(),width=140, height=30, fg_color='#1B263B', dropdown_hover_color='#1B263B', dropdown_text_color='#C9D1D9',dropdown_fg_color="#161B22", text_color="#C9D1D9", button_color="#1B263B", button_hover_color="#1B263B",border_width=0, bg_color='#1B263B')
        self.nome_cliente_combobox.place(x=580, y=350)


        self.forma_pag_combobox = ctk.CTkComboBox(self.root,values=["Cartão Débito", "Cartão Crédito", "PIX", "Boleto"],fg_color='#1B263B',width=125,height=30,dropdown_hover_color='#1B263B',dropdown_text_color='#C9D1D9',dropdown_fg_color="#161B22",text_color="#C9D1D9",button_color="#1B263B",button_hover_color="#1B263B",border_width=0,bg_color='#1B263B')
        self.forma_pag_combobox.place(x=420, y=530)


        self.quantidade_desejada = ctk.CTkEntry(self.root, placeholder_text="Quantidade de produto...", text_color='#C9D1D9', fg_color='#1B263B', bg_color='#2C3E50',width=200, height=30)
        self.quantidade_desejada.place(x=350, y=470)
        
        #criação das labels
        ctk.CTkLabel(self.root, text="Quantidade : ",font=("Times New Roman", 20),fg_color="#2C3E50", text_color='#C9D1D9').place(x=220, y=470)
        ctk.CTkLabel(self.root, text="Produto : ",font=("Times New Roman", 20),fg_color="#2C3E50", text_color='#C9D1D9').place(x=220, y=410)
        ctk.CTkLabel(self.root, text="Cliente :",font=("Times New Roman", 20),fg_color="#2C3E50", text_color='#C9D1D9').place(x=220, y=350)
        ctk.CTkLabel(self.root, text="Forma de pagamento : ",font=("Times New Roman", 20),fg_color="#2C3E50", text_color='#C9D1D9').place(x=220, y=530)

    def fazer_pedido(self):
        quantidade = int(self.quantidade_desejada.get())

        if quantidade:
            try:
                id_produto = self.get_id_produto()
                id_cliente = self.get_id_cliente()
                forma_pag = self.forma_pag_combobox.get()

                data_sistema = date.today()

                nota_fiscal = self.gerar_nota_fiscal()

                fazer_pedido_db(nota_fiscal, data_sistema, forma_pag, quantidade, id_produto, id_cliente)
                messagebox.showinfo("Sucesso", "Pedido cadastrado com sucesso!")

                self.nome_cliente_entry.delete(0, ctk.END)
                self.quantidade_desejada.delete(0, ctk.END)
                self.nome_produto_entry.delete(0, ctk.END)

                pedidos = get_pedidos_db()
                self.atualizar_tabela(pedidos)

            except Exception as e:
                messagebox.showerror("Erro", f"Ocorreu erro ao cadastrar no banco de dados:\n{e}")
        else:
            messagebox.showerror("Error", "Insira um valor INTEIRO na quantidade!")

    def gerar_nota_fiscal(self):
        quant_linhas = len(self.treeview.get_children())
        numero_nf = quant_linhas + 1

        if numero_nf < 10:
            nova_nf = f"NF000{numero_nf}"
        elif numero_nf < 100:
            nova_nf = f"NF00{numero_nf}"
        else:
            nova_nf = f"NF0{numero_nf}"

        return nova_nf

    # CONJUNTO DE FUNÇÕES USADAS PARA A COMBO BOX!!!
    def listar_clientes(self):
        busca = get_id_nome_clientes_db()
        clientes = [nome[1] for nome in busca]
        return clientes

    def listar_produtos(self):
        busca = get_id_nome_produtos_db()
        produtos = [nome[1] for nome in busca]
        return produtos
    
    def filtrar_nomes_clientes(self, event):
        clientes = get_id_nome_clientes_db()

        texto = self.nome_cliente_entry.get().lower()

        filtrados = [nome[1] for nome in clientes if texto in nome[1].lower()]
        self.nome_cliente_combobox.configure(values=filtrados)
        self.nome_cliente_combobox.set(filtrados[0])
    
    def filtrar_nomes_produtos(self, event):
        produtos = get_id_nome_produtos_db()

        texto = self.nome_produto_entry.get().lower()

        filtrados = [nome[1] for nome in produtos if texto in nome[1].lower()]
        self.nome_produto_combobox.configure(values=filtrados)
        self.nome_produto_combobox.set(filtrados[0])

    def get_id_cliente(self):
        nome_cliente = self.nome_cliente_combobox.get()
        busca = get_id_nome_clientes_db()

        for cliente in busca:
            if nome_cliente == cliente[1]:
                id_cliente = cliente[0]
                return id_cliente
    
    def get_id_produto(self):
        nome_produto = self.nome_produto_combobox.get()
        busca = get_id_nome_produtos_db()

        for produto in busca:
            if nome_produto == produto[1]:
                id_produto = produto[0]
                return id_produto
    # FIM DO CONJUNTO DE FUNÇÕES PARA COMBO BOX

    # CONJUNTO DE FUNÇÕES USADOS PARA A CRIAÇÃO E MODELAGEM DA TABELA
    def criar_tabelao(self):
        style = ttk.Style()
        style.theme_use("alt")
        style.configure("Treeview.Heading", background="#1B263B", foreground="#C9D1D9", anchor="center")
        style.configure("Treeview", background="#2C3E50", foreground="#C9D1D9", fieldbackground="gray", rowheight=25)

        self.treeview = ttk.Treeview(self.root, columns=("id_pedido", "nf_pedido", "data_pedido", "forma_pagamento", "cliente_pediu", "produto_pedido", "quantidade_pedida"), show="headings", height=15)

        self.treeview.heading("id_pedido", text="ID") # Altera o nome no cabeçalho da coluna "id_pedido"
        self.treeview.heading("nf_pedido", text="NF") # Altera o nome no cabeçalho da coluna "nf_pedido"
        self.treeview.heading("data_pedido", text="Data realizado") # Altera o nome no cabeçalho da coluna "data_pedido"
        self.treeview.heading("forma_pagamento", text="Forma de pagamento")
        self.treeview.heading("cliente_pediu", text="Cliente")
        self.treeview.heading("produto_pedido", text="Produto")
        self.treeview.heading("quantidade_pedida", text="Quantidade")

        self.treeview.column("id_pedido", width=50) # Altera o tamanho da coluna "id_pedido" (em pixels(px))
        self.treeview.column("nf_pedido", width=80) # Altera o tamanho da coluna "nf_pedido" (em pixels(px))
        self.treeview.column("data_pedido", width=100) # Altera o tamanho da coluna "data_pedido" (em pixels(px))
        self.treeview.column("forma_pagamento", width=130)
        self.treeview.column("cliente_pediu", width=120)
        self.treeview.column("produto_pedido", width=140)
        self.treeview.column("quantidade_pedida", width=80)

        pedidos = get_pedidos_db() # Resgata os dados existentes dentro da tabela "Pedido"

        for pedido in pedidos:
            self.treeview.insert("", "end", values=pedido) # Para cada linha de pedido, ele adiciona na tabela as informações

        self.treeview.place(x=1050, y=300) # Posiciona o ponto inicial da tabela na tela

    def atualizar_tabela(self, pedidos):
         for item in self.treeview.get_children():
            self.treeview.delete(item)

         for pedido in pedidos:
            self.treeview.insert("", "end", values=pedido)

    """def filtrar_tabela(self, event):
        pedidos = get_pedidos_db()
        produto_pesquisado = self.pesquisar_produto_entry.get().lower()

        filtragem = [produto for produto in estoque if produto_pesquisado in produto[1].lower()]

        self.atualizar_tabela(filtragem)"""

    def limpar_campos(self):
        self.nome_cliente_entry.delete(0, ctk.END)
        self.nome_produto_entry.delete(0, ctk.END)

    def voltar_menu(self):
        
       # from menu_adm import menu_admin
        self.root.destroy()  # Fecha a janela atual
        self.menu_root.deiconify()

if __name__ == "__main__":
    root = ctk.CTk()
    app = tela_pedido(root)
    root.mainloop()