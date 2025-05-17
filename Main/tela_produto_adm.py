# Importacoes necessarias
#import ctkinter as ctk
#from ctkinter import * 
import customtkinter as ctk
from tkinter import messagebox
from database_geral import registrar_produto_db, atualizar_produto_db, listar_produtos_db, deletar_produto_db, pesquisar_produto_db, listar_fornecedores_db
from tkinter import ttk

# Criando classe principal, que carrega a janela e tudo o que há nela
class tela_produto_adm:

    # Construtor da classe, carrega as informações básicas de carregamento
    def __init__(self, root):
        self.menu_root = root  
        # Definições da janela
        self.root = ctk.CTkToplevel()
        self.root.title("TBit Manager - Menu de produtos")
        self.root.resizable(width=False, height=False)
        self.root.geometry("1100x700")

       #self.root.config(bg="")
        self.root.transient(root)  # Faz com que a nova janela fique acima da principal
        self.root.grab_set()  # Bloqueia interações na principal até fechar essa
    
        # Carrega os widgets da tela
        self.criando_widgets()
        # Cria a tabela já em conexão com o MySQL
        self.criar_tabela()

    def criando_widgets(self):
        # Criando os botoes que carregam as funcoes necessarias e seus posicionamentos
        ctk.CTkButton(self.root, text="Cadastrar produto", command=self.registrar_no_banco, width=15, height=1).place(x=160, y=330) # Botao para cadastrar produto
        ctk.CTkButton(self.root, text="Alterar produto", command=self.alterar_no_banco, width=15, height=1).place(x=320, y=330) # Botao para alterar produto
        ctk.CTkButton(self.root, text="Deletar produto", command=self.deletar_do_banco, width=15, height=1).place(x=480, y=330) # Botao para deletar produto
        ctk.CTkButton(self.root, text="Cancelar operção", command=self.cancelar_operacao, width=15, height=1).place(x=640, y=330) # Botao para cancelar/voltar ao padrao
        ctk.CTkButton(self.root, text='Voltar', width=20, command=self.voltar_menu).place(x=1000, y=600)

        # Labels usados para identificar as caixas de texto e seus posicionamentos
        ctk.CTkLabel(self.root, text="Nome do Produto:",fg_color="#00284d", text_color='white').place(x=280, y=50)
        ctk.CTkLabel(self.root, text="Descrição do Produto:",fg_color="#00284d", text_color='white').place(x=280, y=90)
        ctk.CTkLabel(self.root, text="Categoria do Produto:",fg_color="#00284d", text_color='white').place(x=280, y=130)
        ctk.CTkLabel(self.root, text="Quantidade do Produto:",fg_color="#00284d", text_color='white').place(x=280, y=170)
        ctk.CTkLabel(self.root, text="Valor do Produto:",fg_color="#00284d", text_color='white').place(x=280, y=210)
        ctk.CTkLabel(self.root, text="Fornecedor do Produto:",fg_color="#00284d", text_color='white').place(x=455, y=250)
        ctk.CTkLabel(self.root, text="Pesquisar fornecedor:",fg_color="#00284d", text_color='white').place(x=160, y=250)

        # Entrys usados para o usuario digitar e seus posicionamentos
        # Entry 'nome do produto'
        self.box_nome = ctk.CTkEntry(self.root, width=150,height=30)
        self.box_nome.place(x=420, y=50)

        # Entry 'descrição do produto'
        self.box_descricao = ctk.CTkEntry(self.root, width=150,height=30)
        self.box_descricao.place(x=420, y=90)

        # Entry 'categoria do produto'
        self.box_categoria = ctk.CTkEntry(self.root, width=150,height=30)
        self.box_categoria.place(x=420, y=130)

        # Entry 'quantidade do produto'
        self.box_quantidade = ctk.CTkEntry(self.root, width=150,height=30)
        self.box_quantidade.place(x=420, y=170)

        # Entry 'valor do produto'
        self.box_valor = ctk.CTkEntry(self.root, width=150,height=30)
        self.box_valor.place(x=420, y=210)

        self.box_fornecedor = ctk.CTkEntry(self.root, width=150, height=30)
        self.box_fornecedor.place(x=295, y=250)
        self.box_fornecedor.bind("<KeyRelease>", self.filtrar_nomes)

        #COMBO box fornecedor
        self.combobox_fornecedor = ctk.CTkComboBox(self.root, values=self.buscar_fornecedores(), height=30, width=210)
        self.combobox_fornecedor.place(x=590, y=250)

        # Entry usado para pesquisar de forma individual
        self.box_pesquisar = ctk.CTkEntry(self.root, width=250, height=30, placeholder_text="Pesquise um produto pelo seu nome...")
        self.box_pesquisar.place(x=360, y=360)
        self.box_pesquisar.bind("<KeyRelease>", self.filtrar_tabela)

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
        
        self.treeview.place(x=30, y=400)

    def atualizar_tabela(self, produtos):
         for item in self.treeview.get_children():
            self.treeview.delete(item)

         for produto in produtos:
            self.treeview.insert("", "end", values=produto)

    def filtrar_tabela(self, event):
        estoque = listar_produtos_db()
        produto_pesquisado = self.box_pesquisar.get().lower()

        filtragem = [produto for produto in estoque if produto_pesquisado in produto[1].lower()]

        self.atualizar_tabela(filtragem)

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
        categoria_produto = self.box_categoria.get()

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
            confirmacao = messagebox.askyesno("Confirmacao", f"Você deseja mesmo excluir '{produto}'")

            if confirmacao == True:
                deletar_produto_db(produto)
                self.box_nome.delete(0, ctk.END)
                messagebox.showinfo("Success", "Produto excluido com sucesso!")

                estoque = listar_produtos_db()
                self.atualizar_estoque() # Lista novamente todos os itens presentes na tabela 'produto'
                self.limpar_campos() # Metodo usado para limpar os campos
            
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
        self.box_pesquisar.delete(0, ctk.END)

       
    def voltar_menu(self):
        
       # from menu_adm import menu_admin
        self.root.destroy()  # Fecha a janela atual
        self.menu_root.deiconify()


# Chama a funcao principal e coloca o programa para rodar
if __name__ == "__main__":
    root = ctk.CTk()
    app = tela_produto_adm(root)
    root.mainloop()