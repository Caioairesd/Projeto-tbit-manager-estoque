import customtkinter as ctk
from tkinter import ttk, messagebox
from database_geral import registrar_cliente_db, update_cliente_db, delete_cliente_db, get_clientes_db, pesquisar_cliente_db, get_id_cliente_db

class tela_cliente:

    
    def __init__(self,root):
        self.menu_root = root  
        self.root = ctk.CTkToplevel(root)
        self.root.title("TBit Manager - Menu de cliente")

        largura = self.root.winfo_screenwidth()# Expandir tela largura
        altura = self.root.winfo_screenheight()# Expandir tela altura
        self.root.geometry(f"{largura}x{altura}+0+0")# definir expanção
        self.root.configure(fg_color='#161B22')

        #ctk.set_appearance_mode("dark")# Deixar o frame no modo escuro-dark

        self.root.grab_set()  # Bloqueia interações na principal até fechar essa

        self.create_widget()
        self.criar_tabela()

    def create_widget(self):
        #Frame para funcdo
        self.right_frame = ctk.CTkFrame(self.root, width=600, height=600, fg_color="#2C3E50")# definir o tamanho e cor do fundo da frame
        self.right_frame.place(x=250, y=250)# definir a expanção da frame

        #Definir Titulo do arquivo
        self.label_text = ctk.CTkLabel(self.root, text="C L I E N T E ",font=("Garamond", 60), fg_color="#161B22", text_color='#58A6FF') # Cria um label para o texto
        self.label_text.place(x=780, y=60) # Posiciona o texto
      

        self.voltar_menu_button = ctk.CTkButton(self.root, text='Voltar',font=('Arial',13),text_color='#C9D1D9', width=90, height= 40,fg_color= '#1B263B', bg_color= '#161B22', command=self.voltar_menu)
        self.voltar_menu_button.place(x=1700, y=900)
        #label cliente id
        self.label_text = ctk.CTkLabel(self.root, text="ID :",font=("arial",22), fg_color="#2C3E50", text_color='#C9D1D9') # Cria um label para o texto
        self.label_text.place(x=350, y=300) # Posiciona o texto
        #caixa de texto Id cliente 
        self.id_cliente_entry = ctk.CTkEntry(self.root, placeholder_text="Digite o ID para cadastro...", text_color='#C9D1D9',fg_color='#1B263B', bg_color='#2C3E50',width=250, height=30)
        self.id_cliente_entry.place(x=470, y=300)
        #Nome label 
        self.label_text = ctk.CTkLabel(self.root, text="Nome :",font=("arial",22), fg_color="#2C3E50", text_color='#C9D1D9') # Cria um label para o texto
        self.label_text.place(x=350, y=350) # Posiciona o texto
        #Caixa de texto cliente nome
        self.nome_cliente_entry = ctk.CTkEntry(self.root, placeholder_text="Nome para registro do cliente...", text_color='#C9D1D9',fg_color='#1B263B', bg_color='#2C3E50',width=250, height=30)
        self.nome_cliente_entry.place(x=470, y=350)

        #Cliente label 
        self.label_text = ctk.CTkLabel(self.root, text="Descrição :",font=("arial",20), fg_color="#2C3E50", text_color='#C9D1D9') # Cria um label para o texto
        self.label_text.place(x=350, y=400) # Posiciona o texto

        #Caixa de texto Descrição cliente
        self.descricao_cliente_entry = ctk.CTkEntry(self.root, placeholder_text="Descrição para registro do cliente...", text_color='#C9D1D9',fg_color='#1B263B', bg_color='#2C3E50',width=250, height=30)
        self.descricao_cliente_entry.place(x=470, y=400)

        #Label CNPJ 
        self.label_text = ctk.CTkLabel(self.root, text="CNPJ :",font=("arial",20), fg_color="#2C3E50", text_color='#C9D1D9') # Cria um label para o texto
        self.label_text.place(x=350, y=450) # Posiciona o texto
        #Caixa de texto CNPJ
        self.cnpj_cliente_entry = ctk.CTkEntry(self.root, placeholder_text="00.000.000/0000-00", text_color='#C9D1D9',fg_color='#1B263B', bg_color='#2C3E50',width=250, height=30)
        self.cnpj_cliente_entry.place(x=470, y=450)

        #label de pesquisar pelo nome do cliente 
        self.label_text = ctk.CTkLabel(self.root, text="Pesquisar :",font=("arial",22), fg_color="#161B22", text_color='#C9D1D9') # Cria um label para o texto
        self.label_text.place(x=1000, y=200) # Posiciona o texto
        #pesquisar cliente pelo nome 
        self.pesquisar_cliente_entry = ctk.CTkEntry(self.root, placeholder_text="Pesquise um cliente pelo nome...", text_color='#C9D1D9',fg_color='#1B263B', bg_color='#2C3E50',width=250, height=30)
        self.pesquisar_cliente_entry.place(x=1110, y=200)
        self.pesquisar_cliente_entry.bind("<KeyRelease>", self.filtrar_tabela)

        self.registrar_button = ctk.CTkButton(self.root, text="CADASTRAR", width=90, height=40, bg_color='#2C3E50', fg_color='#1B263B', command=self.registrar_cliente)
        self.registrar_button.place(x=350, y=600)

        self.alterar_button = ctk.CTkButton(self.root, text="EDITAR", width=90, height=40, bg_color='#2C3E50', fg_color='#1B263B', command=self.alterar_cliente)
        self.alterar_button.place(x=455, y=600)

        self.deletar_button = ctk.CTkButton(self.root, text="EXCLUIR", width=90, height=40, bg_color='#2C3E50', fg_color='#1B263B', command=self.deletar_cliente)
        self.deletar_button.place(x=560, y=600)

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
            confirmacao = messagebox.askyesno("","Você realmente deseja deletar esse cliente?")

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
        style = ttk.Style()
        style.theme_use("alt")
        style.configure("Treeview.Heading", background="#1B263B", foreground="#C9D1D9", anchor="center")
        style.configure("Treeview", background="#2C3E50", foreground="#C9D1D9", fieldbackground="gray", rowheight=30)


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
        
        self.treeview.place(x=1000, y=250, height=600)

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