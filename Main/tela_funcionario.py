import customtkinter as ctk
from tkinter import messagebox, ttk
from database_geral import register_funcionario_db, delete_funcionario_db, update_funcionario_db, pesquisar_funcionario_db, listar_funcionarios_db, listar_funcionarios_parcial_db

ctk.set_appearance_mode('dark')
class tela_funcionario_adm:
    def __init__(self, root):
        self.menu_root = root  
        self.root = ctk.CTkToplevel(root) 
        self.root.title("TBit Manager - Menu de funcionário")
        self.root.configure(fg_color='#141C29')

        largura = self.root.winfo_screenwidth()# Expandir tela largura
        altura = self.root.winfo_screenheight()# Expandir tela altura
        self.root.geometry(f"{largura}x{altura}+0+0")# definir expanção

        self.create_widgets()
        self.root.after(200, self.criar_tabela)  # Garante que a tabela é criada depois que a janela estiver pronta


    def create_widgets(self):
        #adciona um titulo 
        self.titulo = ctk.CTkLabel(self.root, text='F U N C I O N A R I O ',font=("Garamond", 60), fg_color="#141C29", text_color='#58A6FF') # Cria um label para o usuario
        self.titulo.place(x=680, y=60) # Posiciona o label do titulo

        #cria o frame como fundo para deixar um fundo para as labls e caixas de textos
        self.right_frame = ctk.CTkFrame(self.root, width=600, height=700, fg_color="#2C3E50")# definir o tamanho e cor do fundo da frame
        self.right_frame.place(x=50, y=160)# definir a expanção da frame



        # Labels com o texto e sem fundo
        ctk.CTkLabel(self.right_frame, text="Nome :",font=("Times New Roman", 20),fg_color="#2C3E50", text_color='#C9D1D9').place(x=90, y=40)
        ctk.CTkLabel(self.right_frame, text="Data de Nascimento :",font=("Times New Roman", 20),fg_color="#2C3E50", text_color='#C9D1D9',).place(x=90, y=90)
        ctk.CTkLabel(self.right_frame, text="Data de Admissão :",font=("Times New Roman", 20),fg_color="#2C3E50", text_color='#C9D1D9').place(x=90, y=140)
        ctk.CTkLabel(self.right_frame, text="CPF :",font=("Times New Roman", 20),fg_color="#2C3E50", text_color='#C9D1D9').place(x=90, y=190)
        ctk.CTkLabel(self.right_frame, text="Cidade :",font=("Times New Roman", 20),fg_color="#2C3E50", text_color='#C9D1D9').place(x=90, y=240)
        ctk.CTkLabel(self.right_frame, text="Estado :",font=("Times New Roman", 20),fg_color="#2C3E50", text_color='#C9D1D9').place(x=90, y=290)
        ctk.CTkLabel(self.right_frame, text="Telefone :",font=("Times New Roman", 20),fg_color="#2C3E50", text_color='#C9D1D9').place(x=90, y=340)
        ctk.CTkLabel(self.right_frame, text="Email :",font=("Times New Roman", 20),fg_color="#2C3E50", text_color='#C9D1D9').place(x=90, y=390)
        ctk.CTkLabel(self.right_frame, text="Usuario :",font=("Times New Roman", 20),fg_color="#2C3E50", text_color='#C9D1D9').place(x=90, y=440)
        ctk.CTkLabel(self.right_frame, text="Senha :",font=("Times New Roman", 20),fg_color="#2C3E50", text_color='#C9D1D9').place(x=90, y=490)
        ctk.CTkLabel(self.right_frame, text="Escolher perfil :",font=("Times New Roman", 20),fg_color="#2C3E50", text_color='#C9D1D9').place(x=90, y=540)
        

        # Caixas de textos
        self.nome_funcionario_entry  = ctk.CTkEntry(self.right_frame, text_color='#C9D1D9', fg_color='#1B263B', border_color= '#2C3E50',width=300,height=30)
        self.data_nascimento_funcionario_entry = ctk.CTkEntry(self.right_frame, text_color='#C9D1D9', fg_color='#1B263B',border_color='#2C3E50', width=100,height=30)
        self.data_admissao_funcionario_entry = ctk.CTkEntry(self.right_frame, text_color='#C9D1D9', fg_color='#1B263B',border_color='#2C3E50', width=100,height=30)
        self.cpf_funcionario_entry = ctk.CTkEntry(self.right_frame, text_color='#C9D1D9', fg_color='#1B263B',border_color='#2C3E50', width=150,height=30)
        self.cidade_funcionario_entry = ctk.CTkEntry(self.right_frame, text_color='#C9D1D9', fg_color='#1B263B',border_color='#2C3E50', width=150,height=30)
        self.uf_funcionario_entry = ctk.CTkEntry(self.right_frame, text_color='#C9D1D9', fg_color='#1B263B',border_color='#2C3E50', width=150,height=30)
        self.telefone_funcionario_entry = ctk.CTkEntry(self.right_frame, text_color='#C9D1D9', fg_color='#1B263B',border_color='#2C3E50', width=150,height=30)
        self.email_funcionario_entry = ctk.CTkEntry(self.right_frame, text_color='#C9D1D9', fg_color='#1B263B',border_color='#2C3E50', width=280,height=30)
        self.usuario_funcionario_entry = ctk.CTkEntry(self.right_frame, text_color='#C9D1D9', fg_color='#1B263B',border_color='#2C3E50',  width=120, height=30)
        self.senha_funcionario_entry = ctk.CTkEntry(self.right_frame, text_color='#C9D1D9', fg_color='#1B263B',border_color='#2C3E50', show="*", width=120,height=30)

        self.buscar_funcionario_entry = ctk.CTkEntry(self.right_frame, text_color='#C9D1D9', fg_color='#1B263B',border_color='#2C3E50', width=90,height=30)
       
        self.perfil_funcionario_combobox = ctk.CTkComboBox(self.root,fg_color="#1B263B", border_color="#2C3E50",values=["Usuario simples", "Administrador"],dropdown_hover_color='#1B263B',dropdown_text_color='#C9D1D9', width=150,height=30, dropdown_fg_color="#161B22", text_color="#C9D1D9",button_color="#1B263B", button_hover_color="#1B263B", border_width=0, bg_color='#1B263B')
        #button_color="" --> cor do botão da seta

        #Posicionamento das caixas de textos especialmente para nao dar conflito com o GET = PEGAR
        self.nome_funcionario_entry.place(x=170, y=40)#
        self.data_nascimento_funcionario_entry.place(x=270, y=90)#
        self.data_admissao_funcionario_entry.place(x=260, y=140)#
        self.cpf_funcionario_entry.place(x=190, y=190)#
        self.cidade_funcionario_entry.place(x=190, y=240)#
        self.uf_funcionario_entry.place(x=190, y=290)#
        self.telefone_funcionario_entry.place(x=190, y=340)#
        self.email_funcionario_entry.place(x=190, y=390)#
        self.usuario_funcionario_entry.place(x=190, y=440)#
        self.senha_funcionario_entry.place(x=190, y=490)#
        #Posicionamento das caixas de textos especialmente para nao dar conflito com o GET = PEGAR
        self.buscar_funcionario_entry.place(x=190, y=650)

        self.perfil_funcionario_combobox.place(x=300, y=700)
        
        #Posicionamento das caixas de textos especialmente para nao dar conflito com o GET = PEGAR
        ctk.CTkLabel(self.right_frame, text="Busca por :\n(id)   ",text_color='#C9D1D9',font=('Times New Roman', 20), fg_color="#2C3E50").place(x=90, y=650)
        self.id_funcionario_entry = ctk.CTkEntry(self.right_frame, fg_color="#2C3E50")


        # Botões de funções
        ctk.CTkButton(self.right_frame, text="CANCELAR",text_color='#C9D1D9' ,fg_color= '#1B263B', bg_color= '#2C3E50', width=90, height= 40,command=self.cancelar).place(x=420, y=580)
        ctk.CTkButton(self.right_frame, text="REGISTRAR",text_color='#C9D1D9', fg_color= '#1B263B', bg_color= '#2C3E50', width=90, height= 40,command=self.registrar_funcionario).place(x=90, y=580)
        ctk.CTkButton(self.right_frame, text="EXCLUIR",text_color='#C9D1D9', fg_color= '#1B263B', bg_color= '#2C3E50', width=90, height= 40,command=self.delete_funcionario).place(x=200, y=580)
        ctk.CTkButton(self.right_frame, text="EDITAR",text_color='#C9D1D9', fg_color= '#1B263B', bg_color= '#2C3E50', width=90, height= 40,command=self.update_funcionario).place(x=310, y=580)
        ctk.CTkButton(self.right_frame, text="BUSCAR",text_color='#C9D1D9', fg_color= '#1B263B', bg_color= '#2C3E50', width=50, height= 30,command=self.pesquisar_funcionario).place(x=300, y=650)
        ctk.CTkButton(self.root, text='Voltar',font=('Arial',13),text_color='#C9D1D9', width=90, height= 40,fg_color= '#1B263B', bg_color= '#161B22', command=self.voltar_menu).place(x=1700, y=900)


    def registrar_funcionario(self):
        nome_funcionario = self.nome_funcionario_entry.get()
        data_nascimento_funcionario_invertida = self.data_nascimento_funcionario_entry.get()
        data_admissao_funcionario_invertida = self.data_admissao_funcionario_entry.get()
        CPF = self.cpf_funcionario_entry.get()
        Cidade = self.cidade_funcionario_entry.get()
        UF = self.uf_funcionario_entry.get()
        Telefone = self.telefone_funcionario_entry.get()
        Email = self.email_funcionario_entry.get()
        Usuario = self.usuario_funcionario_entry.get()
        Senha = self.senha_funcionario_entry.get()
        perfil = self.perfil_funcionario_combobox.get()
        
        try:
            data_nascimento_funcionario = self.inverter_data(data_nascimento_funcionario_invertida)
            data_admissao_funcionario = self.inverter_data(data_admissao_funcionario_invertida)
        except:
            messagebox.showerror("Error", "Digite uma data válida: dd/mm/aaaa")

        if nome_funcionario and data_nascimento_funcionario and data_admissao_funcionario and CPF and Cidade and UF and Telefone and Email and Usuario and Senha:
            register_funcionario_db(nome_funcionario, data_nascimento_funcionario, data_admissao_funcionario, CPF, Cidade, UF, Telefone, Email, Usuario, Senha, perfil)
            self.limpar_campos()
            messagebox.showinfo("Success", "Funcionario criado com Sucesso")

            funcionarios = listar_funcionarios_parcial_db()
            self.atualizar_tabela(funcionarios)
            
        else:
            messagebox.showerror("Error", "Todos os campos são obrigatórios")

    def pesquisar_funcionario(self):
        busca = self.buscar_funcionario_entry.get()
        self.buscar_funcionario_entry.delete(0, ctk.END)

        if busca:
            id_solicitado = pesquisar_funcionario_db(busca)

            if id_solicitado:
                messagebox.showinfo("Sucesso", f"Funcionário {id_solicitado[1]} encontrado com sucesso!")
                
                self.limpar_campos() # Limpa todos os campos antes de inserir novos dados
                
                # Preenche os campos de entrada com os dados encontrados
                self.id_funcionario_entry.insert(0, id_solicitado[0])
                self.nome_funcionario_entry.insert(0, id_solicitado[1])
                self.data_nascimento_funcionario_entry.insert(0, id_solicitado[2])
                self.data_admissao_funcionario_entry.insert(0, id_solicitado[3])
                self.cpf_funcionario_entry.insert(0, id_solicitado[4])
                self.cidade_funcionario_entry.insert(0, id_solicitado[5])
                self.uf_funcionario_entry.insert(0, id_solicitado[6])
                self.telefone_funcionario_entry.insert(0, id_solicitado[7])
                self.email_funcionario_entry.insert(0, id_solicitado[8])
                self.usuario_funcionario_entry.insert(0, id_solicitado[9])
                self.senha_funcionario_entry.insert(0, id_solicitado[10])
                self.perfil_funcionario_combobox.set(id_solicitado[11])
     
            else:
                messagebox.showerror("Erro", "Funcionário não encontrado")
        else:
            messagebox.showerror("Erro", "Campo de busca vazio")

    def update_funcionario(self):
        id_funcionario = self.id_funcionario_entry.get()
        nome_funcionario = self.nome_funcionario_entry.get()
        data_nascimento_funcionario = self.data_nascimento_funcionario_entry.get()
        data_admissao_funcionario = self.data_admissao_funcionario_entry.get()
        CPF = self.cpf_funcionario_entry.get()
        Cidade = self.cidade_funcionario_entry.get()
        UF = self.uf_funcionario_entry.get()
        Telefone = self.telefone_funcionario_entry.get()
        Email = self.email_funcionario_entry.get()
        Usuario = self.usuario_funcionario_entry.get()
        Senha = self.senha_funcionario_entry.get()
        perfil = self.perfil_funcionario_combobox.get()

        if id_funcionario and nome_funcionario and data_nascimento_funcionario and data_admissao_funcionario and CPF and Cidade and UF and Telefone and Email and Usuario and Senha:
            update_funcionario_db(nome_funcionario, data_nascimento_funcionario, data_admissao_funcionario, CPF, Cidade, UF, Telefone, Email, Usuario, Senha, perfil, id_funcionario)
            messagebox.showinfo("Sucesso", "Funcionário atualizado com sucesso")
            self.limpar_campos()

            funcionarios = listar_funcionarios_parcial_db()
            self.atualizar_tabela(funcionarios)

        else:
            messagebox.showerror("Erro", "Todos os campos são obrigatórios")

    def delete_funcionario(self):
        id_funcionario = self.id_funcionario_entry.get()
        confirmacao = messagebox.askyesno("Confirmação", "Você realmente deseja deletar esse funcionário?")
        if confirmacao:
            if id_funcionario:
                delete_funcionario_db(id_funcionario)
                self.id_funcionario_entry.delete(0, ctk.END)

                funcionarios = listar_funcionarios_parcial_db()
                self.atualizar_tabela(funcionarios)

                self.limpar_campos()

                messagebox.showinfo("Sucesso", "Funcionário deletado com sucesso!")
            else:
                messagebox.showerror("Erro", "ID do funcionário é obrigatório!")

    def limpar_campos(self):
        self.nome_funcionario_entry.delete(0, ctk.END)
        self.data_nascimento_funcionario_entry.delete(0, ctk.END)
        self.data_admissao_funcionario_entry.delete(0, ctk.END)
        self.cpf_funcionario_entry.delete(0, ctk.END)
        self.cidade_funcionario_entry.delete(0, ctk.END)
        self.uf_funcionario_entry.delete(0, ctk.END)
        self.telefone_funcionario_entry.delete(0, ctk.END)
        self.email_funcionario_entry.delete(0, ctk.END)
        self.usuario_funcionario_entry.delete(0, ctk.END)
        self.senha_funcionario_entry.delete(0, ctk.END)
        self.id_funcionario_entry.delete(0, ctk.END)

    def cancelar(self):  
        confirmacao = messagebox.askyesno("Confirmação", "Você deseja mesmo cancelar a operação?")
        if confirmacao == True:
            messagebox.showinfo("Cancelar", "Ação cancelada")
            self.limpar_campos()
            funcionarios = listar_funcionarios_parcial_db()
            self.atualizar_tabela(funcionarios)

    def inverter_data(self, data_digitada):
        data = data_digitada.split("/")
        data_banco = data[2]+"/"+data[1]+"/"+data[0]

        return data_banco
            
    
    def criar_tabela(self):
        style = ttk.Style()
        style.theme_use("alt")
        style.configure("Treeview.Heading", background="#1B263B", foreground="#C9D1D9", anchor="center")
        style.configure("Treeview", background="#2C3E50", foreground="#C9D1D9", fieldbackground="gray", rowheight=25)

        self.treeview = ttk.Treeview(self.root, columns=("id_funcionario", "nome_funcionario", "data_admissao", "cidade_funcionario", "uf_funcionario", "email_funcionario", "perfil_funcionario"), show="headings", height=20)

        self.treeview.heading("id_funcionario", text="ID")
        self.treeview.heading("nome_funcionario", text="Nome")
        self.treeview.heading("data_admissao", text="Data admissão")
        self.treeview.heading("cidade_funcionario", text="Cidade")
        self.treeview.heading("uf_funcionario", text="UF")
        self.treeview.heading("email_funcionario", text="Email")
        self.treeview.heading("perfil_funcionario", text="Perfil")

        self.treeview.column("id_funcionario", width=50) # Altera a largura da coluna "id"
        self.treeview.column("nome_funcionario", width=120) # Altera a largura da coluna "nome"
        self.treeview.column("data_admissao", width=100) # Altera a largura da coluna "data admissao"
        self.treeview.column("cidade_funcionario", width=100) # Altera a largura da coluna "cidade"
        self.treeview.column("uf_funcionario", width=50) # Altera a largura da coluna "estado"
        self.treeview.column("email_funcionario", width=200) # Altera a largura da coluna "email"
        self.treeview.column("perfil_funcionario", width=150) # Altera a largura da coluna "perfil"

        funcionarios = listar_funcionarios_parcial_db()
        for funcionario in funcionarios:
            self.treeview.insert("", "end", values=funcionario)

        self.treeview.bind("<ButtonRelease-1>", self.click_na_linha)

        self.treeview.place(x=680, y=160, width=1180, height=700) # Posiciona a tabela

    def atualizar_tabela(self, funcionarios):
         for item in self.treeview.get_children():
            self.treeview.delete(item)

         for funcionario in funcionarios:
            self.treeview.insert("", "end", values=funcionario)

    def filtrar_tabela(self, event):
        funcionarios = listar_funcionarios_parcial_db()
        funcionario_pesquisado = self.buscar_funcionario_entry.get().lower()

        filtragem = [funcionario for funcionario in funcionarios if funcionario_pesquisado in funcionario[1].lower()]

        self.atualizar_tabela(filtragem)

    def click_na_linha(self, event):
        linha_selecionada = self.treeview.focus()

        if linha_selecionada:
            valores = self.treeview.item(linha_selecionada, "values")

            if valores:
                self.limpar_campos()

                self.id_funcionario_entry.insert(0, valores[0])
                self.nome_funcionario_entry.insert(0, valores[1])
                self.data_admissao_funcionario_entry.insert(0, valores[2])
                self.cidade_funcionario_entry.insert(0, valores[3])
                self.uf_funcionario_entry.insert(0, valores[4])
                self.email_funcionario_entry.insert(0, valores[5])
                self.perfil_funcionario_combobox.set(valores[6])

    def voltar_menu(self):
        
       # from menu_adm import menu_admin
        self.root.destroy()  # Fecha a janela atual
        self.menu_root.deiconify()

if __name__ == "__main__":
    root = ctk.CTk()
    app = tela_funcionario_adm(root)
    root.mainloop()