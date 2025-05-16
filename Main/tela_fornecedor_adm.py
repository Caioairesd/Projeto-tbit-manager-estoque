import customtkinter as ctk
from tkinter import messagebox
from database_geral import register_fornecedor_db,listar_fornecedor_db,update_fornecedor_db,delete_fornecedor_db,pesquisar_fornecedor_db

class tela_fornecedor_adm:

    def __init__(self,root):
        self.menu_root = root  
        self.root = ctk.CTkToplevel(root)
        self.root.configure(fg_color='#A0A0A0')
        #Define os parâmetros de interface da janela
        largura = self.root.winfo_screenwidth()# Expandir tela largura
        altura = self.root.winfo_screenheight()# Expandir tela altura
        self.root.geometry(f"{largura}x{altura}+0+0")# definir expanção
        #ctk.set_appearance_mode('dark')
    
        self.root.title("TBit Manager - Menu de fornecedor")
     
    
       

       
        self.root.grab_set()  # Bloqueia interações na principal até fechar essa

        self.create_widgets()
        self.listar_fornecedor()

    def create_widgets(self):
        
        self.titulo = ctk.CTkLabel(self.root, text='F O R N E C E D O R - A D M I N I S T R A D O R',font=("Garamond", 60), fg_color="#A0A0A0", text_color='black') # Cria um label para o usuario
        self.titulo.place(x=280, y=60) # Posiciona o label 

        #cria o frame como fundo para deixar um fundo para as labls e caixas de textos
        self.right_frame = ctk.CTkFrame(self.root, width=800, height=800, fg_color="gray")# definir o tamanho e cor do fundo da frame
        self.right_frame.place(x=600, y=160)# definir a expanção da frame


        #Criação de botões
        ctk.CTkButton(self.root,text="Cadastrar",width=90,height=40,text_color='black', fg_color='#404040', bg_color='gray',command=self.create_fornecedor).place(x=650,y=590)
        ctk.CTkButton(self.root,text="Alterar",width=90,height=40,text_color='black', fg_color='#404040',command=self.update_fornecedor).place(x=320,y=400)
        ctk.CTkButton(self.root,text="Excluir",width=90,height=40,text_color='black', fg_color='#404040',command=self.delete_fornecedor).place(x=480,y=400)
        ctk.CTkButton(self.root,text="Cancelar",width=90,height=40,text_color='black', fg_color='#404040',command=self.cancelar_operacao).place(x=0,y=400)
        ctk.CTkButton(self.root,text="Pesquisar por\n(Nome ou ID)",text_color='black',fg_color='#404040',width=90,height=40,command=self.pesquisar_fornecedor).place(x=135,y=355)
        ctk.CTkButton(self.root, text='Voltar', width=90, height=40, text_color='black',fg_color='#404040', command=self.voltar_menu).place(x=1700, y=900)
        
        #Criação de labels
        ctk.CTkLabel(self.root,text="Fornecedor :",fg_color="gray",text_color='black',font=('Times New Roman', 23)).place(x=650,y=230)
        ctk.CTkLabel(self.root,text="CNPJ :",fg_color="gray", text_color='black', font=('Times New Roman', 23)).place(x=650,y=280)
        ctk.CTkLabel(self.root,text="Email :",fg_color="gray", text_color='black', font=('Times New Roman', 23)).place(x=650,y=330)
        ctk.CTkLabel(self.root,text="Telefone :",fg_color="gray", text_color='black', font=('Times New Roman', 23)).place(x=650,y=380)
        ctk.CTkLabel(self.root,text="Cidade :",fg_color="gray", text_color='black', font=('Times New Roman', 23)).place(x=650,y=430)
        ctk.CTkLabel(self.root,text="País :",fg_color="gray", text_color='black', font=('Times New Roman', 23)).place(x=650,y=480)
        ctk.CTkLabel(self.root,text="id :",fg_color="gray", text_color='black', font=('Times New Roman', 23)).place(x=650,y=530)


        #Criação de campos de entrada de dados
        self.fornecedor_entry = ctk.CTkEntry(self.root, fg_color='lightgray',bg_color='gray')
        self.marca_fornecedor_entry = ctk.CTkEntry(self.root,fg_color='lightgray',bg_color='gray')
        self.email_fornecedor_entry = ctk.CTkEntry(self.root,fg_color='lightgray',bg_color='gray')
        self.telefone_fornecedor_entry = ctk.CTkEntry(self.root,fg_color='lightgray',bg_color='gray')
        self.cidade_fornecedor_entry = ctk.CTkEntry(self.root,fg_color='lightgray',bg_color='gray')
        self.pais_fornecedor_entry = ctk.CTkEntry(self.root,fg_color='lightgray',bg_color='gray')
        self.id_fornecedor_entry = ctk.CTkEntry(self.root,fg_color='lightgray',bg_color='gray')
        self.pesquisar_entry = ctk.CTkEntry(self.root,width=300,height=30)

        #Definindo localização dos campos na tela
        self.fornecedor_entry.place(x=780,y=230)
        self.marca_fornecedor_entry.place(x=780,y=280)
        self.email_fornecedor_entry.place(x=780,y=330)
        self.telefone_fornecedor_entry.place(x=780,y=380)
        self.cidade_fornecedor_entry.place(x=780,y=430)
        self.pais_fornecedor_entry.place(x=780,y=480)
        self.id_fornecedor_entry.place(x=780,y=530)
        self.pesquisar_entry.place(x=360,y=360)

        #Criação da área de texto responsável por exibir informações dos fornecedores
        self.search_area = ctk.CTkTextbox(self.root,height=15,width=80)
        self.search_area.place(x=135,y=400)

    #função responsável por criar um fornecedor 
    def create_fornecedor(self):
        
        #variáveis recebem o valor inserido no campo de texto
        nome_fornecedor = self.fornecedor_entry.get()
        marca_fornecedor = self.marca_fornecedor_entry.get()
        email_fornecedor = self.email_fornecedor_entry.get()
        telefone_fornecedor = self.telefone_fornecedor_entry.get()
        cidade_fornecedor = self.cidade_fornecedor_entry.get()
        pais_fornecedor = self.pais_fornecedor_entry.get()
       
        #Condicional responsável por acionar função do banco de dados
        if nome_fornecedor and marca_fornecedor and email_fornecedor and telefone_fornecedor and cidade_fornecedor and pais_fornecedor:
            register_fornecedor_db(nome_fornecedor,marca_fornecedor,email_fornecedor,telefone_fornecedor,cidade_fornecedor,pais_fornecedor)

            #Chama a função de limpar campos de texto
            self.limpar_campos()

            #Chama a função de listar para poder atualizar a lista de fornecederores exibida
            self.listar_fornecedor()

            messagebox.showinfo("Sucesso","Fornecedor cadastrado com sucesso!")

        else:

            messagebox.showerror("Erro","Todos os campos são obrigatórios!")
    
    #função responsável por exibir/listar os fornecedores cadastrados no banco de dados          
    def listar_fornecedor(self):
        
        fornecedores = listar_fornecedor_db()
        self.search_area.delete(1.0,ctk.END)

        for fornecedor in fornecedores:
                    self.search_area.insert(ctk.END,f"ID: {fornecedor[0]},Fornecedor: {fornecedor[1]},Marca:{fornecedor[2]},Email:{fornecedor[3]},Telefone:{fornecedor[4]},Cidade:{fornecedor[5]},Cidade:{fornecedor[6]}\n")

    #função responsável por exibir e setar os valores relacionados ao id ou nome inserido ao usuário
    # como não realizamos ainda a máteria de banco de dados não é possível vincular tabela.         
    def pesquisar_fornecedor(self):         
        
        #pesquisa recebe valor inserido no campo de texto de id
        pesquisa = self.pesquisar_entry.get()

        self.pesquisar_entry.delete(0,ctk.END)

            
        if pesquisa:

            id_solicitado = pesquisar_fornecedor_db(pesquisa)

            if id_solicitado:

                
                messagebox.showinfo("Sucesso!","{}Fornecedor encontrado com sucesso!\nVerifique a caixa de texto".format(id_solicitado))
                #Retira de exibição os fornecedores cadastrados deixando somente o pesquisado           
                self.search_area.delete(1.0,ctk.END)

                #Insere os dados do fornecedor pesquisado no campo de exibição
                self.search_area.insert(ctk.END,f"ID: {id_solicitado[0]},Fornecedor: {id_solicitado[1]},Marca:{id_solicitado[2]},Email:{id_solicitado[3]},Telefone:{id_solicitado[4]},Cidade:{id_solicitado[5]},Cidade:{id_solicitado[6]}\n")

                #Insere os dados do fornecedor pesquisado nos campos de texto para possível edição  
                self.id_fornecedor_entry.insert(0,id_solicitado[0])
                self.fornecedor_entry.insert(0,id_solicitado[1])
                self.marca_fornecedor_entry.insert(0,id_solicitado[2])
                self.email_fornecedor_entry.insert(0,id_solicitado[3])
                self.telefone_fornecedor_entry.insert(0,id_solicitado[4])
                self.cidade_fornecedor_entry.insert(0,id_solicitado[5])
                self.pais_fornecedor_entry.insert(0,id_solicitado[6])
            else:
                messagebox.showerror("Erro","Fornecedor não encontrado!")
        else:
            messagebox.showerror("Erro","Campo de pesquisa deve estar preenchido!")

    #Função responsável por atualizar os dados dos fornecedores cadastrados
    def update_fornecedor(self):

        #variáveis recebem os dados inseridos nos campos de textos
        id_fornecedor = self.id_fornecedor_entry.get() 
        nome_fornecedor=self.fornecedor_entry.get()
        marca_fornecedor =self.marca_fornecedor_entry.get()        
        email_fornecedor =self.email_fornecedor_entry.get()
        telefone_fornecedor =self.telefone_fornecedor_entry.get()
        cidade_fornecedor =self.cidade_fornecedor_entry.get()
        pais_fornecedor = self.pais_fornecedor_entry.get()
        
        if  id_fornecedor and nome_fornecedor and marca_fornecedor and email_fornecedor and telefone_fornecedor and cidade_fornecedor and pais_fornecedor:
            update_fornecedor_db(nome_fornecedor,marca_fornecedor,email_fornecedor,telefone_fornecedor,cidade_fornecedor,pais_fornecedor,id_fornecedor)
            
            messagebox.showinfo("Sucess","informações alteradas com sucesso!")
        else:
            messagebox.showerror("ERROR","Todos os campos são obrigatórios!")

        #Chama a função de limpar campos de texto
        self.limpar_campos()

        #Chama a função de listar para poder atualizar a lista de fornecederores exibida
        self.listar_fornecedor()

    #Função responsável por deletar os fornecedores
    def delete_fornecedor(self):

        #variáveis recebem os dados inseridos nos campos de textos
        id_fornecedor = self.id_fornecedor_entry.get()
        confirmacao = messagebox.askyesno("","Você realmente deseja deletar esse formecedor?")
        if confirmacao  == True:
            if id_fornecedor:
                delete_fornecedor_db(id_fornecedor)

                self.id_fornecedor_entry.delete(0,ctk.END)
                self.listar_fornecedor()
                messagebox.showinfo("Sucesso","Fornecedor deletado com sucesso!")
            else:
                messagebox.showerror("Erro","ID do fornecedor é obrigatório!")

            #Função responsável por limpar os campos de texto
    def limpar_campos(self):
        self.fornecedor_entry.delete(0,ctk.END)
        self.marca_fornecedor_entry.delete(0,ctk.END)
        self.email_fornecedor_entry.delete(0,ctk.END)
        self.telefone_fornecedor_entry.delete(0,ctk.END)
        self.cidade_fornecedor_entry.delete(0,ctk.END)
        self.pais_fornecedor_entry.delete(0,ctk.END)
        self.id_fornecedor_entry.delete(0,ctk.END)

    #Função responsável por cancelar a operação
    def cancelar_operacao(self):

        confirmacao = messagebox.askyesno("Confirmação de cancelamento","Você realmente deseja cancelar a operação?")

        if confirmacao == True:
            
            self.limpar_campos()
            self.listar_fornecedor()

    def voltar_menu(self):
        
       # from menu_adm import menu_admin
        self.root.destroy()  # Fecha a janela atual
        self.menu_root.deiconify()
        
          

if __name__ == "__main__":
    root = ctk.CTk()
    app = tela_fornecedor_adm(root)
    root.mainloop()
