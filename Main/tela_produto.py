# Importacoes necessarias
#import ctkinter as ctk
#from ctkinter import * 
import customtkinter as ctk
from tkinter import messagebox, ttk
from database_geral import registrar_produto_db, atualizar_produto_db, listar_produtos_db, deletar_produto_db, listar_fornecedores_db, get_id_produto_db

# Criando classe principal, que carrega a janela e tudo o que há nela
class tela_produto_adm:

    # Construtor da classe, carrega as informações básicas de carregamento
    def __init__(self, root):
        self.menu_root = root  

        # Definições da janela
        self.root = ctk.CTkToplevel()
        self.root.configure(fg_color='#141C29')
        self.root.title("TBit Manager - Menu de produtos")

        largura = self.root.winfo_screenwidth()# Expandir tela largura
        altura = self.root.winfo_screenheight()# Expandir tela altura
        self.root.geometry(f"{largura}x{altura}+0+0")# definir expanção
        
        self.root.grab_set()  # Bloqueia interações na principal até fechar essa
    
        # Carrega os widgets da tela
        self.criando_widgets()
        # Cria a tabela já em conexão com o MySQL
        self.criar_tabela()

    def criando_widgets(self):


        self.titulo = ctk.CTkLabel(self.root, text='P R O D U T O',font=("Garamond", 60), fg_color="#141C29", text_color='#58A6FF') # Cria um abel para o usuario
        self.titulo.place(relx=0.5, y=60, anchor='center') # Posiciona o label 

        #cria o frame como fundo para deixar um fundo para as labls e caixas de textos
        self.right_frame = ctk.CTkFrame(self.root, width=700, height=700, fg_color="#2C3E50")# definir o tamanho e cor do fundo da frame
        self.right_frame.place(x=100, y=170)# definir a expanção da frame


        # Criando os botoes que carregam as funcoes necessarias e seus posicionamentos
        ctk.CTkButton(self.right_frame, text="Cadastrar", command=self.registrar_no_banco, width=90,height= 40,fg_color='#1B263B',text_color='#C9D1D9', border_color='gray').place(x=50, y=400) # Botao para cadastrar 
        ctk.CTkButton(self.right_frame, text="Editar", command=self.alterar_no_banco, width=90,height= 40,fg_color='#1B263B',text_color='#C9D1D9', border_color='gray').place(x=160, y=400) # Botao para alterar 
        ctk.CTkButton(self.right_frame, text="Excluir", command=self.deletar_do_banco, width=90,height= 40,fg_color='#1B263B',text_color='#C9D1D9', border_color='gray').place(x=270, y=400) # Botao para deletar produto
        ctk.CTkButton(self.right_frame, text="Cancelar", command=self.cancelar_operacao, width=90,height= 40,fg_color='#1B263B',text_color='#C9D1D9', border_color='gray').place(x=380, y=400) # Botao para cancelar/voltar ao padrao
        ctk.CTkButton(self.root,text='Voltar',font=('Arial',13),text_color='#C9D1D9', width=90, height= 40,fg_color= '#1B263B', bg_color= '#161B22', command=self.voltar_menu).place(x=1700, y=900)
        

        # Labels usados para identificar as caixas de texto e seus posicionamentos
        ctk.CTkLabel(self.root, text="Nome :",fg_color="#2C3E50",font=('times New Roman', 20), text_color='#C9D1D9').place(x=160, y=200)
        ctk.CTkLabel(self.root, text="Descrição :",fg_color="#2C3E50", font=('times New Roman', 20), text_color='#C9D1D9').place(x=160, y=250)
        ctk.CTkLabel(self.root, text="Categoria :",fg_color="#2C3E50", font=('times New Roman', 20), text_color='#C9D1D9').place(x=160, y=300)
        ctk.CTkLabel(self.root, text="Quantidade : ",fg_color="#2C3E50", font=('times New Roman', 20), text_color='#C9D1D9').place(x=160, y=350)
        ctk.CTkLabel(self.root, text="Valor :",fg_color="#2C3E50", font=('times New Roman', 20), text_color='#C9D1D9').place(x=160, y=400)
        ctk.CTkLabel(self.root, text="Pesquisar :",fg_color="#2C3E50", font=('times New Roman', 20), text_color='#C9D1D9').place(x=160, y=450)

        # Entrys usados para o usuario digitar e seus posicionamentos
        # Entry 'nome do produto'
        self.box_nome = ctk.CTkEntry(self.right_frame, placeholder_text="Digite o nome do produto", text_color='#C9D1D9', fg_color='#1B263B', bg_color='#2C3E50',width=200, height=30)
        self.box_nome.place(x=170, y=40)

        # Entry 'descrição do produto'
        self.box_descricao = ctk.CTkEntry(self.right_frame, placeholder_text="Digite a descrição do produto", text_color='#C9D1D9', fg_color='#1B263B', bg_color='#2C3E50',width=200, height=30)
        self.box_descricao.place(x=170, y=90)

        # Entry 'categoria do produto'
        self.box_categoria = ctk.CTkEntry(self.right_frame, placeholder_text="Digite a categoria do produto", text_color='#C9D1D9', fg_color='#1B263B', bg_color='#2C3E50',width=200, height=30)
        self.box_categoria.place(x=170, y=140)

        # Entry 'quantidade do produto'
        self.box_quantidade = ctk.CTkEntry(self.right_frame, placeholder_text="Digite a quantidade de produtos", text_color='#C9D1D9', fg_color='#1B263B', bg_color='#2C3E50',width=200, height=30)
        self.box_quantidade.place(x=170, y=190)

        # Entry 'valor do produto'
        self.box_valor = ctk.CTkEntry(self.right_frame, placeholder_text="Digite o valor do produto", text_color='#C9D1D9', fg_color='#1B263B', bg_color='#2C3E50',width=200, height=30)
        self.box_valor.place(x=170, y=240)

        # Entry 'fornecedor do produto'
        self.box_fornecedor = ctk.CTkEntry(self.right_frame, placeholder_text="Digite o nome do fornecedor", text_color='#C9D1D9', fg_color='#1B263B', bg_color='#2C3E50',width=200, height=30)
        self.box_fornecedor.place(x=170, y=290)
        self.box_fornecedor.bind("<KeyRelease>", self.filtrar_nomes)

        #COMBO box fornecedor

        self.combobox_fornecedor = ctk.CTkComboBox(self.root,height=30, width=140,text_color='#C9D1D9',fg_color='#1B263B',border_color='gray',button_color='#1B263B',button_hover_color='#1B263B',dropdown_fg_color='#161B22',dropdown_text_color='#C9D1D9',dropdown_hover_color='#1B263B',border_width=0,bg_color='#1B263B',values=self.buscar_fornecedores())
        self.combobox_fornecedor.place(x=490, y=450)

    # MÉTODOS USADOS PARA OS FORNECEDORES
    def buscar_fornecedores(self):
            busca = listar_fornecedores_db()
            fornecedores = [nome[1] for nome in busca]
            return fornecedores

    #EVENTO PARA FILTRAGEM DENTRO DA CHECK BOX
    def filtrar_nomes(self, event):
        fornecedores = listar_fornecedores_db()

        texto = self.box_fornecedor.get().lower()

        filtrados = [nome[1] for nome in fornecedores if texto in nome[1].lower()]
        self.combobox_fornecedor.configure(values=filtrados)
        self.combobox_fornecedor.set(filtrados[0])

    def get_id_fornecedor(self):
        nome_fornecedor = self.combobox_fornecedor.get()
        busca = listar_fornecedores_db()

        for fornecedor in busca:
            if nome_fornecedor == fornecedor[1]:
                id_fornecedor = fornecedor[0]
                return id_fornecedor
    # FIM DOS MÉTODOS PARA FORNECEDORES

    # MÉTODOS USADOS PARA A CRIAÇÃO E MODELAGEM DA TABELA
    def criar_tabela(self):
        # Definir estilo
        style = ttk.Style()
        style.theme_use("alt")
        style.configure("Treeview.Heading", background="#1B263B", foreground="#C9D1D9", anchor="center")
        style.configure("Treeview", background="#2C3E50", foreground="#C9D1D9", fieldbackground="gray", rowheight=25)

        self.treeview = ttk.Treeview(self.root, columns=("id_produto", "nome_produto", "descricao_produto", "categoria_produto", "quantidade_disponivel", "valor_produto", "fornecedor_produto"), show="headings", height=12)

        self.treeview.heading("id_produto", text="ID produto")
        self.treeview.heading("nome_produto", text="Nome produto")
        self.treeview.heading("descricao_produto", text="Descricao produto")
        self.treeview.heading("categoria_produto", text="Categoria produto")
        self.treeview.heading("quantidade_disponivel", text="Quantidade disp")
        self.treeview.heading("valor_produto", text="Valor produto")
        self.treeview.heading("fornecedor_produto", text="Fornecedor produto")

        self.treeview.column("id_produto", width=80)
        self.treeview.column("nome_produto", width=150)
        self.treeview.column("descricao_produto", width=250)
        self.treeview.column("categoria_produto", width=140)
        self.treeview.column("quantidade_disponivel", width=110)
        self.treeview.column("valor_produto", width=110)
        self.treeview.column("fornecedor_produto", width=120)

        estoque = listar_produtos_db()
        for cliente in estoque:
            self.treeview.insert("", "end", values=cliente)

        self.treeview.bind("<ButtonRelease-1>", self.click_na_linha)
        
        self.treeview.place(x=890, y=170, height=700)

    def atualizar_tabela(self, produtos):
         for item in self.treeview.get_children():
            self.treeview.delete(item)

         for produto in produtos:
            self.treeview.insert("", "end", values=produto)

    """def filtrar_tabela(self, event):
        estoque = listar_produtos_db()
        produto_pesquisado = self.box_pesquisar.get().lower()

        filtragem = [produto for produto in estoque if produto_pesquisado in produto[1].lower()]

        self.atualizar_tabela(filtragem)"""

    def click_na_linha(self, event):
        linha_selecionada = self.treeview.focus()

        if linha_selecionada:
            valores = self.treeview.item(linha_selecionada, "values")

            if valores:
                self.limpar_campos()

                self.box_nome.insert(0, valores[1])
                self.box_descricao.insert(0, valores[2])
                self.box_categoria.insert(0, valores[3])
                self.box_quantidade.insert(0, valores[4])
                self.box_valor.insert(0, valores[5])
                self.combobox_fornecedor.set(valores[6])

    # Método usado quando o botao 'Cadastrar' é clicado
    def registrar_no_banco(self):
        nome_produto = self.box_nome.get().title() # Pega o valor que esta dentro da box de nome
        descricao_produto = self.box_descricao.get() # Pega o valor que esta dentro da box de descricao
        valor_produto = self.box_valor.get() # Pega o valor que esta dentro da box de valor
        quantidade_produto = self.box_quantidade.get()
        categoria_produto = self.box_categoria.get().title()

        id_fornecedor = self.get_id_fornecedor()

        if nome_produto and descricao_produto and valor_produto and id_fornecedor and quantidade_produto and categoria_produto: # Verifica se todas as variaveis carregam um valor diferente de nulo
            try:
                registrar_produto_db(nome_produto, descricao_produto, categoria_produto, quantidade_produto, valor_produto, id_fornecedor) # Executa o metodo que se conecta com o banco

                self.limpar_campos() # Executa o metodo que limpa os campos

                messagebox.showinfo("Sucesso", "Produto cadastrado com sucesso!") # Mensagem lançada na tela do usuario

                estoque = listar_produtos_db() # REALIZA CONSULTA NA TABELA PRODUTOS
                self.atualizar_tabela(estoque) # ATUALIZA A TABELA PRESENTE NA TELA
            except:
                messagebox.showerror("Error 212", "Erro ao tentar cadastrar no banco de dados!")
        else:
            messagebox.showerror("Error", "Todos os campos são obrigatorios") # Mensagem lançada na tela do usuario

    def alterar_no_banco(self):
        nome_produto = self.box_nome.get().title() # Resgata as informações que estão dentro da box 'Nome'
        descricao_produto = self.box_descricao.get() # Resgata as informações que estão dentro da box 'Descricao'
        valor_produto = self.box_valor.get() # Resgata as informações que estão dentro da box 'Valor'
        categoria_produto = self.box_categoria.get().title()

        if nome_produto and descricao_produto and valor_produto and categoria_produto: # Verifica se alguma variavel esta vazia
            confirmacao = messagebox.askyesno("Confirmação", f"Você realmente deseja alterar as informações de '{nome_produto}'?") # Mensagem lançada na tela do usuario que recebe 'True' ou 'False'

            if confirmacao == True: # Verifica se o cliente clicou 'Sim'
                atualizar_produto_db(nome_produto, descricao_produto, categoria_produto, valor_produto) # Chama o metodo atualizar_produto, que faz conexao com o banco
                self.limpar_campos() # Metodo usado para limpar os campos
                messagebox.showinfo("Sucesso", "Produto atualizado com sucesso!") # Mensagem lançada na tela do usuario
                
                estoque = listar_produtos_db() 
                self.atualizar_tabela(estoque) # Lista novamente todos os itens presentes na tabela 'produto'
            else:
                messagebox.showinfo("Cancelado", "Operação de alteração cancelada!") # Mensagem lançada na tela do usuario
        else:
            messagebox.showerror("Error", "Todos os campos são obrigatorios") # Mensagem lançada na tela do usuario
    
    def deletar_do_banco(self):
        produto = self.box_nome.get()

        if produto:
            confirmacao = messagebox.askyesno("Confirmacao", f"Você deseja mesmo excluir '{produto}'?")

            if confirmacao == True:
                id_produto = get_id_produto_db(produto)
                print(id_produto)
                
                if id_produto:
                    deletar_produto_db(id_produto)

                    messagebox.showinfo("Sucesso", "Produto excluido com sucesso!")

                    estoque = listar_produtos_db()
                    self.atualizar_tabela(estoque) # Lista novamente todos os itens presentes na tabela 'produto'
                    
                    self.limpar_campos() # Metodo usado para limpar os campos

                else:
                    messagebox.showerror("Error", "Não foi encontrado produto com esse ID!")
            else:
                messagebox.showinfo("Cancelado", "Processo de exclusão cancelada!")
        else:
            messagebox.showerror("Error", "Campo 'Nome' não preenchido ou Produto não encontrado!")
       
    # Metodo que reseta tudo ao padrao
    def cancelar_operacao(self):
        confirmacao = messagebox.askyesno("Confirmação", "Você desejar mesmo cancelar a opreção?") # Janela de sim ou nao para confirmacao
        if confirmacao == True: # Verifica se o cliente clicou em 'sim'
            messagebox.showinfo("Cancelado", "Operação cancelada!")
            self.limpar_campos()
            estoque = listar_produtos_db()
            self.atualizar_tabela(estoque)
    
    # Metodo que limpa os campos
    def limpar_campos(self):
        self.box_nome.delete(0, ctk.END)
        self.box_descricao.delete(0, ctk.END)
        self.box_quantidade.delete(0, ctk.END)
        self.box_valor.delete(0, ctk.END)
        self.box_categoria.delete(0, ctk.END)
        self.box_fornecedor.delete(0, ctk.END)
       
    def voltar_menu(self):
        
       # from menu_adm import menu_admin
        self.root.destroy()  # Fecha a janela atual
        self.menu_root.deiconify()

# Chama a funcao principal e coloca o programa para rodar
if __name__ == "__main__":
    root = ctk.CTk()
    app = tela_produto_adm(root)
    root.mainloop()