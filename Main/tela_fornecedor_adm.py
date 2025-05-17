import customtkinter as ctk
from tkinter import messagebox
from database_geral import register_fornecedor_db,listar_fornecedor_db,update_fornecedor_db,delete_fornecedor_db,pesquisar_fornecedor_db
from tkinter import ttk

class tela_fornecedor_adm:

    def __init__(self,root):
        self.menu_root = root  
        self.root = ctk.CTkToplevel(root)

        #Define os parâmetros de interface da janela
        self.root.geometry("1000x700")
        self.root.title("TBit Manager - Menu de fornecedor")
        #self.root.configure(background="white")
        self.root.resizable(width=False,height=False)
        #self.root.attributes("-alpha",1.0)
        #self.root.config(bg="#003366")

        self.root.transient(root)  # Faz com que a nova janela fique acima da principal
        self.root.grab_set()  # Bloqueia interações na principal até fechar essa

        self.create_widgets()
        self.criar_tabela()

    def create_widgets(self):
        #Criação de labels

        #Criação de botões
        ctk.CTkButton(self.root,text="Cadastrar",width=15,height=1,command=self.create_fornecedor).place(x=160,y=280)
        ctk.CTkButton(self.root,text="Alterar",width=15,height=1,command=self.update_fornecedor).place(x=320,y=280)
        ctk.CTkButton(self.root,text="Excluir",width=15,height=1,command=self.delete_fornecedor).place(x=480,y=280)
        ctk.CTkButton(self.root,text="Cancelar",width=15,height=1,command=self.cancelar_operacao).place(x=640,y=280)
        ctk.CTkButton(self.root, text='Voltar', width=20, command=self.voltar_menu).place(x=800, y=600)
        
        #Criação de labels
        ctk.CTkLabel(self.root,text="Fornecedor:",fg_color="blue", text_color='white').place(x=300,y=30)
        ctk.CTkLabel(self.root,text="CNPJ:",fg_color="blue", text_color='white').place(x=300,y=60)
        ctk.CTkLabel(self.root,text="Email:",fg_color="blue", text_color='white').place(x=300,y=90)
        ctk.CTkLabel(self.root,text="Telefone:",fg_color="blue", text_color='white').place(x=300,y=120)
        ctk.CTkLabel(self.root,text="País:",fg_color="blue", text_color='white').place(x=300,y=150)
        ctk.CTkLabel(self.root,text="Cidade:",fg_color="blue", text_color='white').place(x=300,y=180)
        ctk.CTkLabel(self.root,text="ID:",fg_color="blue", text_color='white').place(x=300,y=210)


        #Criação de campos de entrada de dados
        self.fornecedor_entry = ctk.CTkEntry(self.root)
        self.cnpj_fornecedor_entry = ctk.CTkEntry(self.root)
        self.email_fornecedor_entry = ctk.CTkEntry(self.root)
        self.telefone_fornecedor_entry = ctk.CTkEntry(self.root)
        self.pais_fornecedor_entry = ctk.CTkEntry(self.root)
        self.cidade_fornecedor_entry = ctk.CTkEntry(self.root)
        self.id_fornecedor_entry = ctk.CTkEntry(self.root)
        self.pesquisar_entry = ctk.CTkEntry(self.root,width=300,height=30, placeholder_text="Pesquise um fornecedor pelo seu nome...")
        self.pesquisar_entry.bind("<KeyRelease>", self.filtrar_tabela)

        #Definindo localização dos campos na tela
        self.fornecedor_entry.place(x=400,y=30)
        self.cnpj_fornecedor_entry.place(x=400,y=60)
        self.email_fornecedor_entry.place(x=400,y=90)
        self.telefone_fornecedor_entry.place(x=400,y=120)
        self.pais_fornecedor_entry.place(x=400,y=150)
        self.cidade_fornecedor_entry.place(x=400,y=180)
        self.id_fornecedor_entry.place(x=400,y=210)
        self.pesquisar_entry.place(x=360,y=310)

    # CONJUNTO DE FUNÇÕES USADAS PARA A CRIAÇÃO E MODELAGEM DA TABELA
    def criar_tabela(self):
        self.treeview = ttk.Treeview(self.root, columns=("id_fornecedor", "nome_fornecedor", "cnpj_fornecedor", "email_fornecedor", "telefone_fornecedor", "pais_fornecedor", "cidade_fornecedor"), show="headings", height=15)

        self.treeview.heading("id_fornecedor", text="ID fornecedor")
        self.treeview.heading("nome_fornecedor", text="Nome fornecedor")
        self.treeview.heading("cnpj_fornecedor", text="CNPJ fornecedor")
        self.treeview.heading("email_fornecedor", text="Email fornecedor")
        self.treeview.heading("telefone_fornecedor", text="Telefone fornecedor")
        self.treeview.heading("pais_fornecedor", text="Pais residente")
        self.treeview.heading("cidade_fornecedor", text="Cidade residente")

        self.treeview.column("id_fornecedor", width=100)
        self.treeview.column("nome_fornecedor", width=130)
        self.treeview.column("cnpj_fornecedor", width=150)
        self.treeview.column("email_fornecedor", width=225)
        self.treeview.column("telefone_fornecedor", width=140)
        self.treeview.column("pais_fornecedor", width=100)
        self.treeview.column("cidade_fornecedor", width=100)

        fornecedores = listar_fornecedor_db()
        for fornecedor in fornecedores:
            self.treeview.insert("", "end", values=fornecedor)

        self.treeview.bind("<ButtonRelease-1>", self.click_na_linha)
        
        self.treeview.place(x=50, y=350)

    def atualizar_tabela(self, fornecedores):
         for item in self.treeview.get_children():
            self.treeview.delete(item)

         for fornecedor in fornecedores:
            self.treeview.insert("", "end", values=fornecedor)

    def filtrar_tabela(self, event):
        fornecedores = listar_fornecedor_db()
        fornecedor_pesquisado = self.pesquisar_entry.get().lower()

        filtragem = [fornecedor for fornecedor in fornecedores if fornecedor_pesquisado in fornecedor[1].lower()]

        self.atualizar_tabela(filtragem)

    def click_na_linha(self, event):
        linha_selecionada = self.treeview.focus()

        if linha_selecionada:
            valores = self.treeview.item(linha_selecionada, "values")

            if valores:
                self.limpar_campos()

                self.id_fornecedor_entry.insert(0, valores[0])
                self.fornecedor_entry.insert(0, valores[1])
                self.cnpj_fornecedor_entry.insert(0, valores[2])
                self.email_fornecedor_entry.insert(0, valores[3])
                self.telefone_fornecedor_entry.insert(0, valores[4])
                self.pais_fornecedor_entry.insert(0, valores[5])
                self.cidade_fornecedor_entry.insert(0, valores[6])

    #função responsável por criar um fornecedor 
    def create_fornecedor(self):
        
        #variáveis recebem o valor inserido no campo de texto
        nome_fornecedor = self.fornecedor_entry.get()
        cnpj_fornecedor = self.cnpj_fornecedor_entry.get()
        email_fornecedor = self.email_fornecedor_entry.get()
        telefone_fornecedor = self.telefone_fornecedor_entry.get()
        cidade_fornecedor = self.pais_fornecedor_entry.get()
        pais_fornecedor = self.cidade_fornecedor_entry.get()
       
        #Condicional responsável por acionar função do banco de dados
        if nome_fornecedor and cnpj_fornecedor and email_fornecedor and telefone_fornecedor and cidade_fornecedor and pais_fornecedor:
            register_fornecedor_db(nome_fornecedor,cnpj_fornecedor,email_fornecedor,telefone_fornecedor,cidade_fornecedor,pais_fornecedor)

            #Chama a função de limpar campos de texto
            self.limpar_campos()

            #Chama a função de listar para poder atualizar a lista de fornecederores exibida
            fornecedores = listar_fornecedor_db()
            self.atualizar_tabela(fornecedores)

            messagebox.showinfo("Sucesso","Fornecedor cadastrado com sucesso!")

        else:

            messagebox.showerror("Erro","Todos os campos são obrigatórios!")
    
    #função responsável por exibir e setar os valores relacionados ao id ou nome inserido ao usuário
    # como não realizamos ainda a máteria de banco de dados não é possível vincular tabela.         
    #Função responsável por atualizar os dados dos fornecedores cadastrados
    def update_fornecedor(self):

        #variáveis recebem os dados inseridos nos campos de textos
        id_fornecedor = self.id_fornecedor_entry.get() 
        nome_fornecedor=self.fornecedor_entry.get()
        cnpj_fornecedor =self.cnpj_fornecedor_entry.get()        
        email_fornecedor =self.email_fornecedor_entry.get()
        telefone_fornecedor =self.telefone_fornecedor_entry.get()
        cidade_fornecedor =self.pais_fornecedor_entry.get()
        pais_fornecedor = self.cidade_fornecedor_entry.get()
        
        if  id_fornecedor and nome_fornecedor and cnpj_fornecedor and email_fornecedor and telefone_fornecedor and cidade_fornecedor and pais_fornecedor:
            update_fornecedor_db(nome_fornecedor,cnpj_fornecedor,email_fornecedor,telefone_fornecedor,cidade_fornecedor,pais_fornecedor,id_fornecedor)
            
            messagebox.showinfo("Sucess","informações alteradas com sucesso!")
        else:
            messagebox.showerror("ERROR","Todos os campos são obrigatórios!")

        #Chama a função de limpar campos de texto
        self.limpar_campos()

        #Chama a função de listar para poder atualizar a lista de fornecederores exibida
        fornecedores = listar_fornecedor_db()
        self.atualizar_tabela(fornecedores)

    #Função responsável por deletar os fornecedores
    def delete_fornecedor(self):

        #variáveis recebem os dados inseridos nos campos de textos
        id_fornecedor = self.id_fornecedor_entry.get()
        if id_fornecedor:
            confirmacao = messagebox.askyesno("","Você realmente deseja deletar esse formecedor?")
            if confirmacao  == True:
                delete_fornecedor_db(id_fornecedor)

                self.id_fornecedor_entry.delete(0,ctk.END)
                fornecedores = listar_fornecedor_db()
                self.atualizar_tabela(fornecedores)
                messagebox.showinfo("Sucesso","Fornecedor deletado com sucesso!")
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
        self.id_fornecedor_entry.delete(0,ctk.END)
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
