import customtkinter as ctk
from database_geral import fazer_pedido_db, get_id_nome_clientes_db, get_id_nome_produtos_db
from tkinter import messagebox

class tela_pedido:

    def __init__(self,root):
        self.menu_root = root  
        self.root = ctk.CTkToplevel(root)

        #Define os parâmetros de interface da janela
        self.root.geometry("900x700")

        self.root.title("TBit Manager - Pedido")
        self.root.resizable(width=False,height=False)

        self.root.transient(root)  # Faz com que a nova janela fique acima da principal
        self.root.grab_set()  # Bloqueia interações na principal até fechar essa

        voltar_menu_button = ctk.CTkButton(self.root, text='Voltar', width=20, command=self.voltar_menu)
        voltar_menu_button.place(x=800, y=600)

        self.fazer_pedido_button = ctk.CTkButton(self.root, text="Novo pedido", width=150, height=30, command=self.fazer_pedido)
        self.fazer_pedido_button.place(x=300, y=300)

        self.nome_produto_entry = ctk.CTkEntry(self.root, placeholder_text="Pesquise o produto que você deseja...", width=250, height=30)
        self.nome_produto_entry.place(x=100, y=100)
        self.nome_produto_entry.bind("<KeyRelease>", self.filtrar_nomes_produtos)

        self.nome_cliente_entry = ctk.CTkEntry(self.root, placeholder_text="Pesquise o cliente que você deseja...", width=250, height=30)
        self.nome_cliente_entry.place(x=400, y=100)
        self.nome_cliente_entry.bind("<KeyRelease>", self.filtrar_nomes_clientes)

        self.nome_produto_combobox = ctk.CTkComboBox(self.root, width=250, height=30, values=self.listar_produtos())
        self.nome_produto_combobox.place(x=100, y=150)

        self.nome_cliente_combobox = ctk.CTkComboBox(self.root, width=250, height=30, values=self.listar_clientes())
        self.nome_cliente_combobox.place(x=400, y=150)

        self.quantidade_desejada = ctk.CTkEntry(self.root, placeholder_text="Digite a quantidade desejada pelo cliente...", width=250, height=30)
        self.quantidade_desejada.place(x=250, y=200)

    def fazer_pedido(self):
        quantidade = int(self.quantidade_desejada.get())

        if quantidade:
            try:
                id_produto = self.get_id_produto()
                id_cliente = self.get_id_cliente()
                fazer_pedido_db(quantidade, id_produto, id_cliente)
                messagebox.showinfo("Sucesso", "Pedido cadastrado com sucesso!")
            except:
                messagebox.showerror("Error", "Ocorreu erro ao cadastrar no banco de dados! Tente novamente...")
        else:
            messagebox.showerror("Error", "Insira um valor INTEIRO na quantidade!")

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

        texto = self.nome_cliente_entry.get().lower()

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
    # FIM DO CONJUNTO DE FUNÇÕES 

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
