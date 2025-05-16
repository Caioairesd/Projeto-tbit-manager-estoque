# Importacoes necessarias
#import ctkinter as ctk
#from ctkinter import * 
import customtkinter as ctk
from tkinter import messagebox
from database_geral import registrar_produto_db, atualizar_produto_db, listar_produtos_db, deletar_produto_db, pesquisar_produto_db

# Criando classe principal, que carrega a janela e tudo o que há nela
class tela_produto_adm:

    # Construtor da classe, carrega as informações básicas de carregamento
    def __init__(self, root):
        self.menu_root = root  
        # Definições da janela
        self.root = ctk.CTkToplevel()
        self.root.configure(fg_color='#A0A0A0')
        self.root.title("TBit Manager - Menu de produtos")
        self.root.resizable(width=False, height=False)
        self.root.geometry("900x700")

       #self.root.config(bg="")
        self.root.transient(root)  # Faz com que a nova janela fique acima da principal
        self.root.grab_set()  # Bloqueia interações na principal até fechar essa
    
        # Carrega os widgets da tela
        self.criando_widgets()
        # Lista todos os produtos ja cadastrados
        self.listar_do_banco()

    def criando_widgets(self):
        # Criando os botoes que carregam as funcoes necessarias e seus posicionamentos
        ctk.CTkButton(self.root, text="Cadastrar produto", command=self.registrar_no_banco, width=15, height=1).place(x=160, y=280) # Botao para cadastrar produto
        ctk.CTkButton(self.root, text="Alterar produto", command=self.alterar_no_banco, width=15, height=1).place(x=320, y=280) # Botao para alterar produto
        ctk.CTkButton(self.root, text="Deletar produto", command=self.deletar_do_banco, width=15, height=1).place(x=480, y=280) # Botao para deletar produto
        ctk.CTkButton(self.root, text="Cancelar operção", command=self.cancelar_operacao, width=15, height=1).place(x=640, y=280) # Botao para cancelar/voltar ao padrao
        ctk.CTkButton(self.root, text="Pesquisar produto e\nAutopreencher (ID ou NOME)", command=self.pesquisar_produto_especifico, width=30, height=2).place(x=135, y=355)
        ctk.CTkButton(self.root, text='Voltar', width=20, command=self.voltar_menu).place(x=800, y=600)

        # Labels usados para identificar as caixas de texto e seus posicionamentos
        ctk.CTkLabel(self.root, text="Nome do Produto:",fg_color="#00284d", text_color='white').place(x=280, y=50)
        ctk.CTkLabel(self.root, text="Descrição do Produto:",fg_color="#00284d", text_color='white').place(x=280, y=90)
        ctk.CTkLabel(self.root, text="Quantidade do Produto:",fg_color="#00284d", text_color='white').place(x=280, y=130)
        ctk.CTkLabel(self.root, text="Valor do Produto:",fg_color="#00284d", text_color='white').place(x=280, y=170)

        # Entrys usados para o usuario digitar e seus posicionamentos
        # Entry 'nome do produto'
        self.box_nome = ctk.CTkEntry(self.root, width=25,height=30)
        self.box_nome.place(x=420, y=50)

        # Entry 'descrição do produto'
        self.box_descricao = ctk.CTkEntry(self.root, width=25,height=30)
        self.box_descricao.place(x=420, y=90)

        # Entry 'quantidade do produto'
        self.box_quantidade = ctk.CTkEntry(self.root, width=25,height=30)
        self.box_quantidade.place(x=420, y=130)

        # Entry 'valor do produto'
        self.box_valor = ctk.CTkEntry(self.root, width=25,height=30)
        self.box_valor.place(x=420, y=170)
        
        # Entry usado para pesquisar de forma individual
        self.box_pesquisar = ctk.CTkEntry(self.root, width=40, height=30)
        self.box_pesquisar.place(x=360, y=360 )

        # Text area usado para retornar dados ja existentes
        self.text_area = ctk.CTkTextbox(self.root, width=80, height=15)
        self.text_area.place(x=135, y=400)

    # Método usado quando o botao 'Cadastrar' é clicado
    def registrar_no_banco(self):
        nome_produto = self.box_nome.get().title() # Pega o valor que esta dentro da box de nome
        descricao_produto = self.box_descricao.get() # Pega o valor que esta dentro da box de descricao
        quantidade_produto = self.box_quantidade.get() # Pega o valor que esta dentro da box de quantidade
        valor_produto = self.box_valor.get() # Pega o valor que esta dentro da box de valor

        if nome_produto and descricao_produto and quantidade_produto and valor_produto: # Verifica se todas as variaveis carregam um valor diferente de nulo
            registrar_produto_db(nome_produto, descricao_produto, quantidade_produto, valor_produto) # Executa o metodo que se conecta com o banco

            self.limpar_campos() # Executa o metodo que limpa os bancos

            messagebox.showinfo("Sucesso", "Produto cadastrado com sucesso!") # Mensagem lançada na tela do usuario

            self.listar_do_banco() # Lista novamente todos os itens presentes na tabela 'produto'
        else:
            messagebox.showerror("Error", "Todos os campos são obrigatorios") # Mensagem lançada na tela do usuario

    def alterar_no_banco(self):
        nome_produto = self.box_nome.get() # Resgata as informações que estão dentro da box 'Nome'
        descricao_produto = self.box_descricao.get() # Resgata as informações que estão dentro da box 'Descricao'
        quantidade_produto = self.box_quantidade.get() # Resgata as informações que estão dentro da box 'Quantidade'
        valor_produto = self.box_valor.get(

        ) # Resgata as informações que estão dentro da box 'Valor'

        if nome_produto and descricao_produto and quantidade_produto and valor_produto: # Verifica se alguma variavel esta vazia
            confirmacao = messagebox.askyesno("Confirmação", f"Você realmente deseja alterar as informações de '{nome_produto}'?") # Mensagem lançada na tela do usuario que recebe 'True' ou 'False'

            if confirmacao == True: # Verifica se o cliente clicou 'Sim'
                atualizar_produto_db(nome_produto, descricao_produto, quantidade_produto, valor_produto) # Chama o metodo atualizar_produto, que faz conexao com o banco
                self.limpar_campos() # Metodo usado para limpar os campos
                messagebox.showinfo("Sucesso", "Produto atualizado com sucesso!") # Mensagem lançada na tela do usuario
                self.listar_do_banco() # Lista novamente todos os itens presentes na tabela 'produto'
                self.box_nome.delete(0, ctk.END) 
            else:
                messagebox.showinfo("Cancelado", "Operação de alteração cancelada!") # Mensagem lançada na tela do usuario
        else:
            messagebox.showerror("Error", "Todos os campos são obrigatorios") # Mensagem lançada na tela do usuario

    # Metodo usado para resgatar todos os itens presentes no banco
    def listar_do_banco(self):
            produtos = listar_produtos_db()
            self.text_area.delete(1.0, ctk.END)

            for produto in produtos:
                self.text_area.insert(ctk.END, f"-ID: {produto[0]} | Nome: {produto[1]} | Descrição: {produto[2]} | Quantidade: {produto[3]} | Valor: {produto[4]}\n")
    
    def deletar_do_banco(self):
        produto = self.box_nome.get()
        if produto:
            confirmacao = messagebox.askyesno("Confirmacao", f"Você deseja mesmo excluir '{produto}'")

            if confirmacao == True:
                deletar_produto_db(produto)
                self.box_nome.delete(0, ctk.END)
                messagebox.showinfo("Success", "Produto excluido com sucesso!")

                self.listar_do_banco() # Lista novamente todos os itens presentes na tabela 'produto'
                self.limpar_campos() # Metodo usado para limpar os campos
            
            else:
                messagebox.showinfo("Cancelado", "Processo de exclusão cancelada!")
        else:
            messagebox.showerror("Error", "Campo 'Nome' não preenchido ou Produto não encontrado!")

    def pesquisar_produto_especifico(self):
        pesquisa = self.box_pesquisar.get().title()
        self.box_pesquisar.delete(0, ctk.END)
        self.limpar_campos() # Metodo usado para limpar os campos

        if pesquisa:
            produto_retornado = pesquisar_produto_db(pesquisa)

            if produto_retornado:
                messagebox.showinfo("Success", f"Produto '{produto_retornado[1]}' encontrado com sucesso, verifique a caixa de texto!")
                self.text_area.delete(1.0, ctk.END)
                self.text_area.insert(ctk.END, f"ID: {produto_retornado[0]} | Nome: {produto_retornado[1]} | Descrição: {produto_retornado[2]} | Quantidade: {produto_retornado[3]} | Valor: {produto_retornado[4]}")
                
                self.box_nome.insert(0, produto_retornado[1]) # Retorna as informações recebidas na caixa 'Nome'
                self.box_descricao.insert(0, produto_retornado[2]) # Retorna as informações recebidas na caixa 'Descricao'
                self.box_quantidade.insert(0, produto_retornado[3]) # Retorna as informações recebidas na caixa 'Quantidade'
                self.box_valor.insert(0, produto_retornado[4]) # Retorna as informações recebidas na caixa 'Valor'

            else:
                messagebox.showerror("Error", "Produto não encontrado ou não cadastrado!")
                self.limpar_campos() # Metodo usado para limpar os campos
                self.listar_do_banco() # Lista novamente todos os itens presentes na tabela 'produto'
        else:
            messagebox.showerror("Error", "Campo 'Pesquisar' não preenchido!")
        
    # Metodo que reseta tudo ao padrao
    def cancelar_operacao(self):
        confirmacao = messagebox.askyesno("Confirmação", "Você desejar mesmo cancelar a opreção?") # Janela de sim ou nao para confirmacao
        if confirmacao == True: # Verifica se o cliente clicou em 'sim'
            messagebox.showinfo("Cancelado", "Operação cancelada!")
            self.limpar_campos()
            self.listar_do_banco()
    
    # Metodo que limpa os campos
    def limpar_campos(self):
        self.box_nome.delete(0, ctk.END)
        self.box_descricao.delete(0, ctk.END)
        self.box_quantidade.delete(0, ctk.END)
        self.box_valor.delete(0, ctk.END)    

    
       
    def voltar_menu(self):
        
       # from menu_adm import menu_admin
        self.root.destroy()  # Fecha a janela atual
        self.menu_root.deiconify()

# Chama a funcao principal e coloca o programa para rodar
if __name__ == "__main__":
    root = ctk.CTk()
    app = tela_produto_adm(root)
    root.mainloop()