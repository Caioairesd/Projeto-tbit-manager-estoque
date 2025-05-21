import customtkinter as ctk
from tkinter import messagebox, ttk
from database_geral import register_fornecedor_db,listar_fornecedor_db,update_fornecedor_db,delete_fornecedor_db,pesquisar_fornecedor_db, get_id_cnpj_db
from mysql.connector import Error

class tela_fornecedor_adm:

    def __init__(self,root):
        self.menu_root = root  
        self.root = ctk.CTkToplevel(root)
        self.root.configure(fg_color='#141C29')



        #Define os parâmetros de interface da janela
        largura = self.root.winfo_screenwidth()# Expandir tela largura
        altura = self.root.winfo_screenheight()# Expandir tela altura
        self.root.geometry(f"{largura}x{altura}+0+0")# definir expanção
        #ctk.set_appearance_mode('dark')
    
        self.root.title("TBit Manager - Menu de fornecedor")
      
        self.root.grab_set()  # Bloqueia interações na principal até fechar essa

        self.create_widgets()
        self.criar_tabela()

    def create_widgets(self):
        
        self.titulo = ctk.CTkLabel(self.root, text='F O R N E C E D O R ',font=("Garamond", 60), fg_color="#141C29", text_color='#58A6FF') # Cria um label para o usuario
        self.titulo.place(relx=0.5, y=60, anchor='n')
 

        #cria o frame como fundo para deixar um fundo para as labls e caixas de textos
        self.right_frame = ctk.CTkFrame(self.root, width=600, height=600, fg_color="#2C3E50")# definir o tamanho e cor do fundo da frame
        self.right_frame.place(x=200, y=160)# definir a expanção da frame

        #Criação de labels
        ctk.CTkLabel(self.right_frame,text="Fornecedor :",fg_color="#2C3E50",text_color='#C9D1D9',font=('Times New Roman', 23)).place(x=100,y=50)
        ctk.CTkLabel(self.right_frame,text="CNPJ :",fg_color="#2C3E50", text_color='#C9D1D9', font=('Times New Roman', 23)).place(x=100,y=100)
        ctk.CTkLabel(self.right_frame,text="Email :",fg_color="#2C3E50", text_color='#C9D1D9', font=('Times New Roman', 23)).place(x=100,y=150)
        ctk.CTkLabel(self.right_frame,text="Telefone :",fg_color="#2C3E50", text_color='#C9D1D9', font=('Times New Roman', 23)).place(x=100,y=200)
        ctk.CTkLabel(self.right_frame,text="Cidade :",fg_color="#2C3E50", text_color='#C9D1D9', font=('Times New Roman', 23)).place(x=100,y=250)
        ctk.CTkLabel(self.right_frame,text="País :",fg_color="#2C3E50", text_color='#C9D1D9', font=('Times New Roman', 23)).place(x=100,y=300)
        ctk.CTkLabel(self.right_frame,text="Buscar por id:  ",fg_color="#2C3E50", text_color='#C9D1D9', font=('Times New Roman', 20)).place(x=100,y=500)

        #Criação de botões

        ctk.CTkButton(self.right_frame,text="Cadastrar",width=90,height=40,text_color='#C9D1D9', fg_color='#1B263B', bg_color='#2C3E50',command=self.create_fornecedor).place(x=100,y=420)
        ctk.CTkButton(self.right_frame,text="Alterar",width=90,height=40,text_color='#C9D1D9', fg_color='#1B263B',bg_color='#2C3E50',command=self.update_fornecedor).place(x=210,y=420)
        ctk.CTkButton(self.right_frame,text="Excluir",width=90,height=40,text_color='#C9D1D9', fg_color='#1B263B',bg_color='#2C3E50',command=self.delete_fornecedor).place(x=320,y=420)
        ctk.CTkButton(self.right_frame,text="Cancelar",width=90,height=40,text_color='#C9D1D9', fg_color='#1B263B',bg_color='#2C3E50',command=self.cancelar_operacao).place(x=430,y=420)
        ctk.CTkButton(self.root, text='Voltar',font=('Arial',13),text_color='#C9D1D9', width=90, height= 40,fg_color= '#1B263B', bg_color= '#161B22',command=self.voltar_menu).place(x=1700, y=900)

        #Criação de campos de entrada de dados
        self.fornecedor_entry = ctk.CTkEntry(self.right_frame, text_color='#C9D1D9', fg_color='#1B263B', placeholder_text='Nome fornecedor..',width=200,height=30)
        self.cnpj_fornecedor_entry = ctk.CTkEntry(self.right_frame, text_color='#C9D1D9', fg_color='#1B263B', placeholder_text='CNPJ fornecedor...',width=200,height=30)
        self.email_fornecedor_entry = ctk.CTkEntry(self.right_frame, text_color='#C9D1D9', fg_color='#1B263B', placeholder_text='Email fornecdor...',width=200,height=30)
        self.telefone_fornecedor_entry = ctk.CTkEntry(self.right_frame, text_color='#C9D1D9', fg_color='#1B263B', placeholder_text='Telefone fornecedor...',width=200,height=30)
        self.cidade_fornecedor_entry = ctk.CTkEntry(self.right_frame, text_color='#C9D1D9', fg_color='#1B263B', placeholder_text='Cidade fornecedor..',width=200,height=30)
        self.pais_fornecedor_entry = ctk.CTkEntry(self.right_frame, text_color='#C9D1D9', fg_color='#1B263B', placeholder_text='Pais fornecedor...',width=200,height=30)
        self.pesquisar_entry = ctk.CTkEntry(self.right_frame, text_color='#C9D1D9', fg_color='#1B263B', placeholder_text='Pesquisar fornecedor...',width=200,height=30)

        #Definindo localização dos campos na tela
        self.fornecedor_entry.place(x=240,y=50)
        self.cnpj_fornecedor_entry.place(x=240,y=100)
        self.email_fornecedor_entry.place(x=240,y=150)
        self.telefone_fornecedor_entry.place(x=240,y=200)
        self.cidade_fornecedor_entry.place(x=240,y=250)
        self.pais_fornecedor_entry.place(x=240,y=300)
        self.pesquisar_entry.place(x=240,y=500)


        ctk.CTkButton(self.right_frame, text="Buscar", width=90, height=30,
              text_color='#C9D1D9', fg_color='#1B263B', bg_color='#2C3E50',
              command=self.pesquisar_fornecedor).place(x=450, y=500)
        
        ctk.CTkLabel(self.right_frame, text="ID :", fg_color="#2C3E50", text_color='#C9D1D9', font=('Times New Roman', 23)).place(x=100, y=350)
        self.id_fornecedor_entry = ctk.CTkEntry(self.right_frame, text_color='#C9D1D9', fg_color='#1B263B', placeholder_text='ID fornecedor...', width=200, height=30)
        self.id_fornecedor_entry.place(x=240, y=350)


    # CONJUNTO DE FUNÇÕES USADAS PARA A CRIAÇÃO E MODELAGEM DA TABELA
    def criar_tabela(self):
        # Definir estilo
        style = ttk.Style()
        style.theme_use("alt")
        style.configure("Treeview.Heading", background="#1B263B", foreground="#C9D1D9", anchor="center")
        style.configure("Treeview", background="#2C3E50", foreground="#C9D1D9", fieldbackground="gray", rowheight=25)

        self.treeview = ttk.Treeview(self.root, columns=("id_fornecedor", "nome_fornecedor", "cnpj_fornecedor", "email_fornecedor", "telefone_fornecedor", "pais_fornecedor", "cidade_fornecedor"), show="headings", height=15)

        self.treeview.heading("id_fornecedor", text="ID")
        self.treeview.heading("nome_fornecedor", text="Nome")
        self.treeview.heading("cnpj_fornecedor", text="CNPJ")
        self.treeview.heading("email_fornecedor", text="Email")
        self.treeview.heading("telefone_fornecedor", text="Telefone")
        self.treeview.heading("pais_fornecedor", text="Pais")
        self.treeview.heading("cidade_fornecedor", text="Cidade")

        self.treeview.column('id_fornecedor', width=50)
        self.treeview.column("nome_fornecedor", width=100) # Altera a largura da coluna "nome"
        self.treeview.column("cnpj_fornecedor", width=120) # Altera a largura da coluna "cnpj"
        self.treeview.column("email_fornecedor", width=210) # Altera a largura da coluna "email"
        self.treeview.column("telefone_fornecedor", width=120) # Altera a largura da coluna "telefone"
        self.treeview.column("pais_fornecedor", width=100) # Altera a largura da coluna "pais"
        self.treeview.column("cidade_fornecedor", width=100) # Altera a largura da coluna "cidade"

        fornecedores = listar_fornecedor_db()
        for fornecedor in fornecedores:
            self.treeview.insert("", "end", values=fornecedor)

        self.treeview.bind("<ButtonRelease-1>", self.click_na_linha)
        
        self.treeview.place(x=900, y=160, width=850, height=600) # Posiciona a tabela

    def atualizar_tabela(self, fornecedores):
         for item in self.treeview.get_children():
            self.treeview.delete(item)

         for fornecedor in fornecedores:
            self.treeview.insert("", "end", values=fornecedor)

    """def filtrar_tabela(self, event=None):
        fornecedores = listar_fornecedor_db()
        fornecedor_pesquisado = self.pesquisar_entry.get().lower()

        filtragem = [fornecedor for fornecedor in fornecedores if fornecedor_pesquisado in str(fornecedor[1]).lower() or fornecedor_pesquisado in str(fornecedor[0]).lower()]

        self.atualizar_tabela(filtragem)

        self.pesquisar_entry.bind("<Return>", self.filtrar_tabela)"""

    def click_na_linha(self, event):
        linha_selecionada = self.treeview.focus()

        if linha_selecionada:
            valores = self.treeview.item(linha_selecionada, "values")

            if valores:
                self.limpar_campos()

                self.id_fornecedor_entry.delete(0, ctk.END)
                self.id_fornecedor_entry.insert(0, valores[0])

                self.fornecedor_entry.delete(0, ctk.END)

                self.fornecedor_entry.insert(0, valores[1])

                self.cnpj_fornecedor_entry.delete(0, ctk.END)
                self.cnpj_fornecedor_entry.insert(0, valores[2])

                self.email_fornecedor_entry.delete(0, ctk.END)
                self.email_fornecedor_entry.insert(0, valores[3])

                self.telefone_fornecedor_entry.delete(0, ctk.END)
                self.telefone_fornecedor_entry.insert(0, valores[4])

                self.pais_fornecedor_entry.delete(0, ctk.END)
                self.pais_fornecedor_entry.insert(0, valores[5])

                self.cidade_fornecedor_entry.delete(0, ctk.END)
                self.cidade_fornecedor_entry.insert(0, valores[6])

    #função responsável por criar um fornecedor 
    def create_fornecedor(self):
        nome_fornecedor = self.fornecedor_entry.get()
        cnpj_fornecedor = self.cnpj_fornecedor_entry.get()
        email_fornecedor = self.email_fornecedor_entry.get()
        telefone_fornecedor = self.telefone_fornecedor_entry.get()
        cidade_fornecedor = self.cidade_fornecedor_entry.get()
        pais_fornecedor = self.pais_fornecedor_entry.get()
        if nome_fornecedor and cnpj_fornecedor and email_fornecedor and telefone_fornecedor and cidade_fornecedor and pais_fornecedor:
            register_fornecedor_db(nome_fornecedor, cnpj_fornecedor, email_fornecedor, telefone_fornecedor, cidade_fornecedor, pais_fornecedor)
            self.limpar_campos()
            fornecedores = listar_fornecedor_db()
            self.atualizar_tabela(fornecedores)
            messagebox.showinfo("Sucesso", "Fornecedor cadastrado com sucesso!")
        else:
            messagebox.showerror("Erro", "Todos os campos são obrigatórios!")

    def pesquisar_fornecedor(self):
        # Usado para atualizar os campos de texto
        pesquisa = self.pesquisar_entry.get()

        if pesquisa:
            fornecedor = pesquisar_fornecedor_db(pesquisa)

            if fornecedor:
                messagebox.showinfo("Sucesso", f"Fornecedor {fornecedor[1]} foi encontrado! Atualizando campos...")

                self.id_fornecedor_entry.delete(0, ctk.END)

                self.id_fornecedor_entry.insert(ctk.END, fornecedor[0])
                self.fornecedor_entry.insert(ctk.END, fornecedor[1])
                self.cnpj_fornecedor_entry.insert(ctk.END, fornecedor[2])
                self.email_fornecedor_entry.insert(ctk.END, fornecedor[3])
                self.telefone_fornecedor_entry.insert(ctk.END, fornecedor[4])
                self.cidade_fornecedor_entry.insert(ctk.END, fornecedor[5])
                self.pais_fornecedor_entry.insert(ctk.END, fornecedor[6])
            else:
                messagebox.showerror("Error", "Não foi encontrado nenhum fornecedor com esse nome ou ID!")
        else:
            messagebox.showerror("Error", "Preencha o campo de pesquisa!")
    
    #função responsável por exibir e setar os valores relacionados ao id ou nome inserido ao usuário
    # como não realizamos ainda a máteria de banco de dados não é possível vincular tabela.         
    #Função responsável por atualizar os dados dos fornecedores cadastrados
    def update_fornecedor(self):
        id_fornecedor = self.id_fornecedor_entry.get()
        nome_fornecedor = self.fornecedor_entry.get()
        cnpj_fornecedor = self.cnpj_fornecedor_entry.get()
        email_fornecedor = self.email_fornecedor_entry.get()
        telefone_fornecedor = self.telefone_fornecedor_entry.get()
        cidade_fornecedor = self.cidade_fornecedor_entry.get()
        pais_fornecedor = self.pais_fornecedor_entry.get()


        #variáveis recebem os dados inseridos nos campos de textos
        nome_fornecedor=self.fornecedor_entry.get()
        cnpj_fornecedor =self.cnpj_fornecedor_entry.get()        
        email_fornecedor =self.email_fornecedor_entry.get()
        telefone_fornecedor =self.telefone_fornecedor_entry.get()
        cidade_fornecedor =self.pais_fornecedor_entry.get()
        pais_fornecedor = self.cidade_fornecedor_entry.get()
        
        if  nome_fornecedor and cnpj_fornecedor and email_fornecedor and telefone_fornecedor and cidade_fornecedor and pais_fornecedor:
            
            confirmacao = messagebox.askyesno("Confirmação", f"Você deseja mesmo alterar o fornecedor '{cnpj_fornecedor}'?")
            if confirmacao == True:
                update_fornecedor_db(nome_fornecedor,cnpj_fornecedor,email_fornecedor,telefone_fornecedor,cidade_fornecedor,pais_fornecedor)

                messagebox.showinfo("Sucess","informações alteradas com sucesso!")
        else:
            messagebox.showerror("Error","Todos os campos são obrigatórios!")

        self.limpar_campos()

        fornecedores = listar_fornecedor_db()
        self.atualizar_tabela(fornecedores)


    # USADO PARA O DELETE
    def get_id_fornecedor(self):
        cnpj_fornecedor = self.cnpj_fornecedor_entry.get()
        busca = get_id_cnpj_db()

        for fornecedor in busca:
            if cnpj_fornecedor == fornecedor[1]:
                id_fornecedor = fornecedor[0]
                return id_fornecedor

    #Função responsável por deletar os fornecedores
    def delete_fornecedor(self):

        #variáveis recebem os dados inseridos nos campos de textos
        id_fornecedor = self.get_id_fornecedor()
        if id_fornecedor:
            confirmacao = messagebox.askyesno("","Você realmente deseja deletar esse fornecedor?")
            if confirmacao  == True:

                try:
                    delete_fornecedor_db(id_fornecedor)

                    self.limpar_campos()

                    fornecedores = listar_fornecedor_db()
                    self.atualizar_tabela(fornecedores)
                
                    messagebox.showinfo("Sucesso","Fornecedor deletado com sucesso!")
                except Error as erro:
                    messagebox.showerror("Erro", f"Erro ao executar a operação no banco de dados:\n{erro}")

        else:
            messagebox.showerror("Erro","ID do fornecedor é obrigatório!")


    #Função responsável por limpar os campos de texto
    def limpar_campos(self):
        self.fornecedor_entry.delete(0,ctk.END)
        self.cnpj_fornecedor_entry.delete(0,ctk.END)
        self.email_fornecedor_entry.delete(0,ctk.END)
        self.telefone_fornecedor_entry.delete(0,ctk.END)
        self.pais_fornecedor_entry.delete(0,ctk.END)
        self.cidade_fornecedor_entry.delete(0,ctk.END)
        self.pesquisar_entry.delete(0, ctk.END)

    #Função responsável por cancelar a operação
    def cancelar_operacao(self):

        confirmacao = messagebox.askyesno("Confirmação de cancelamento","Você realmente deseja cancelar a operação?")

        if confirmacao == True:
            
            self.limpar_campos()
            fornecedores = listar_fornecedor_db()
            self.atualizar_tabela(fornecedores)

    def voltar_menu(self):
        
       # from menu_adm import menu_admin
        self.root.destroy()  # Fecha a janela atual
        self.menu_root.deiconify()
        
          

if __name__ == "__main__":
    root = ctk.CTk()
    app = tela_fornecedor_adm(root)
    root.mainloop()