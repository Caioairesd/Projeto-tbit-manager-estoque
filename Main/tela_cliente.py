import customtkinter as ctk
from tkinter import ttk, messagebox
from database_geral import registrar_cliente_db, update_cliente_db, delete_cliente_db, get_clientes_db, pesquisar_cliente_db

class tela_cliente:

    
    def __init__(self,root):
        self.menu_root = root  
        self.root = ctk.CTkToplevel(root)
        self.root.title("TBit Manager - Menu de cliente")

        largura = self.root.winfo_screenwidth()# Expandir tela largura
        altura = self.root.winfo_screenheight()# Expandir tela altura
        self.root.geometry(f"{largura}x{altura}+0+0")# definir expanção
        self.root.configure(fg_color='#A0A0A0')

        #ctk.set_appearance_mode("dark")# Deixar o frame no modo escuro-dark

        self.root.grab_set()  # Bloqueia interações na principal até fechar essa

        self.create_widget()
        self.criar_tabela()

    def create_widget(self):

        self.voltar_menu_button = ctk.CTkButton(self.root, text='Voltar', width=20, command=self.voltar_menu)
        self.voltar_menu_button.place(x=825, y=650)

        self.id_cliente_entry = ctk.CTkEntry(self.root, placeholder_text="Digite o ID para pesquisa...", width=250, height=30)
        self.id_cliente_entry.place(x=100, y=100)

        self.nome_cliente_entry = ctk.CTkEntry(self.root, placeholder_text="Nome para registro do cliente...", width=250, height=30)
        self.nome_cliente_entry.place(x=100, y=150)

        self.descricao_cliente_entry = ctk.CTkEntry(self.root, placeholder_text="Descrição para registro do cliente...", width=250, height=30)
        self.descricao_cliente_entry.place(x=100, y=200)

        self.cnpj_cliente_entry = ctk.CTkEntry(self.root, placeholder_text="00.000.000/0000-00", width=250, height=30)
        self.cnpj_cliente_entry.place(x=100, y=250)

        self.pesquisar_cliente_entry = ctk.CTkEntry(self.root, placeholder_text="Pesquise um cliente pelo seu nome...", width=250, height=30)
        self.pesquisar_cliente_entry.place(x=600, y=250)
        self.pesquisar_cliente_entry.bind("<KeyRelease>", self.filtrar_tabela)

        self.registrar_button = ctk.CTkButton(self.root, text="Registrar cliente", width=150, height=30, command=self.registrar_cliente)
        self.registrar_button.place(x=400, y=100)

        self.alterar_button = ctk.CTkButton(self.root, text="Alterar cliente", width=150, height=30, command=self.alterar_cliente)
        self.alterar_button.place(x=400, y=150)

        self.deletar_button = ctk.CTkButton(self.root, text="Deletar cliente", width=150, height=30, command=self.deletar_cliente)
        self.deletar_button.place(x=400, y=200)

    def registrar_cliente(self):
        nome_cliente = self.nome_cliente_entry.get()
        descricao_cliente = self.descricao_cliente_entry.get()
        cnpj_cliente = self.cnpj_cliente_entry.get()
        
        if nome_cliente and descricao_cliente and cnpj_cliente:
            try:
                registrar_cliente_db(nome_cliente, descricao_cliente, cnpj_cliente)
                messagebox.showinfo("Sucesso", "Cadastro do cliente foi efetuado com sucesso!")

                banco = get_clientes_db()
                self.limpar_campos()
                self.atualizar_tabela(banco)
            except:
                messagebox.showerror("Error", "Erro na tentativa de cadastrar um novo cliente!")
        else:
            messagebox.showinfo("Error", "Preencha todos os campos!")

    def alterar_cliente(self):
        id_cliente = self.id_cliente_entry.get()
        nome_cliente = self.nome_cliente_entry.get()
        descricao_cliente = self.descricao_cliente_entry.get()
        cnpj_cliente = self.cnpj_cliente_entry.get()

        if nome_cliente and descricao_cliente and cnpj_cliente:
            try:
                update_cliente_db(nome_cliente, descricao_cliente, cnpj_cliente, id_cliente)
                messagebox.showinfo("Sucesso", "Informações alteradas com sucesso!")

                banco = get_clientes_db()
                self.atualizar_tabela(banco)
                self.limpar_campos()
            except:
                messagebox.showerror("Error", "Erro na tentativa de alterar informações!")
        else:
            messagebox.showerror("Erro", "Preencha todos os campos!")
    
    def deletar_cliente(self):
        id_cliente = self.id_cliente_entry.get()
        if id_cliente:
            confirmacao = messagebox.askyesno("","Você realmente deseja deletar esse formecedor?")
            if confirmacao  == True:
                delete_cliente_db(id_cliente)
                self.id_cliente_entry.delete(0,ctk.END)
                messagebox.showinfo("Sucesso","Cliente deletado com sucesso!")

                banco = get_clientes_db()
                self.atualizar_tabela(banco)
                self.limpar_campos()
        else:
            messagebox.showerror("Erro","ID do cliente é obrigatório!")

    def pesquisar_cliente(self):
        id_cliente = self.id_cliente_entry.get()
        if id_cliente:
            busca = pesquisar_cliente_db(id_cliente)

            if busca:
                messagebox.showinfo("Sucesso", f"Cliente '{busca[1]} encontrado!'")
                return f"ID: {busca[0]}, Nome: {busca[1]}, Descrição: {busca[2]}, CNPJ: {busca[3]}"

    def listar_clientes(self):
        clientes = get_clientes_db()

        for cliente in clientes:
            return f"ID: {cliente[0]}, Nome: {cliente[1]}, Descrição: {cliente[2]}, CNPJ: {cliente[3]}"

    def limpar_campos(self):
        self.id_cliente_entry.delete(0, ctk.END)
        self.cnpj_cliente_entry.delete(0, ctk.END)
        self.nome_cliente_entry.delete(0, ctk.END)
        self.descricao_cliente_entry.delete(0, ctk.END)
        self.pesquisar_cliente_entry.delete(0, ctk.END)

        self.pesquisar_cliente_entry.configure(placeholder_text="Pesquise um cliente pelo seu nome...")

     # FUNÇÕES USADAS PARA A TABELA
    def criar_tabela(self):
        self.treeview = ttk.Treeview(self.root, columns=("id_cliente", "nome_cliente", "descricao_cliente", "cnpj_cliente"), show="headings", height=15)

        self.treeview.heading("id_cliente", text="ID do cliente")
        self.treeview.heading("nome_cliente", text="Nome do cliente")
        self.treeview.heading("descricao_cliente", text="Descricao do cliente")
        self.treeview.heading("cnpj_cliente", text="CNPJ do cliente")

        self.treeview.column("id_cliente", width=100)
        self.treeview.column("nome_cliente", width=150)
        self.treeview.column("descricao_cliente", width=300)
        self.treeview.column("cnpj_cliente", width=250)

        estoque = get_clientes_db()
        for cliente in estoque:
            self.treeview.insert("", "end", values=cliente)

        self.treeview.bind("<ButtonRelease-1>", self.click_na_linha)
        
        self.treeview.place(x=50, y=300)

    def atualizar_tabela(self, clientes):
         for item in self.treeview.get_children():
            self.treeview.delete(item)

         for cliente in clientes:
            self.treeview.insert("", "end", values=cliente)

    def filtrar_tabela(self, event):
        estoque = get_clientes_db()
        cliente_pesquisado = self.pesquisar_cliente_entry.get().lower()

        filtragem = [cliente for cliente in estoque if cliente_pesquisado in cliente[1].lower()]

        self.atualizar_tabela(filtragem)

    def click_na_linha(self, event):
        linha_selecionada = self.treeview.focus()

        if linha_selecionada:
            valores = self.treeview.item(linha_selecionada, "values")

            if valores:
                self.limpar_campos()

                self.id_cliente_entry.insert(0, valores[0])
                self.nome_cliente_entry.insert(0, valores[1])
                self.descricao_cliente_entry.insert(0, valores[2])
                self.cnpj_cliente_entry.insert(0, valores[3])
    # FIM DAS FUNÇÕES DE TABELA

    def voltar_menu(self):
        
       # from menu_adm import menu_admin
        self.root.destroy()  # Fecha a janela atual
        self.menu_root.deiconify()

if __name__ == "__main__":
    root = ctk.CTk()
    app = tela_cliente(root)
    root.mainloop()
