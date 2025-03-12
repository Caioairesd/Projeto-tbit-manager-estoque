# Importacoes necessarias
from tkinter import * 
from tkinter import messagebox
from tkinter import ttk
from db_produto import registrar_produto, atualizar_produto, listar_produtos, deletar_produto, pesquisar_produto

# Criando classe principal, que carrega a janela e tudo o que há nela
class crud_produtos:
    def __init__(self, root):
        # Definições da janela
        self.root = root
        self.root.title("TBit Manager - Produtos")
        self.root.resizable(width=False, height=False)
        self.root.geometry("900x750")
    
        # Carrega os widgets da tela
        self.criando_widgets()

    def criando_widgets(self):
        # Frame que carrega os botoes
        frame_botoes = Frame(self.root, width=900, height=250)
        frame_botoes.grid(row=1)

        # Labels vazios para divisoes
        Label(frame_botoes, text="", height=4).grid(row=1, column=1)
        Label(frame_botoes, text="", width=10).grid(row=1, column=1)
        Label(frame_botoes, text="", width=7).grid(row=3, column=3)
        Label(frame_botoes, text="", width=7).grid(row=5, column=5)
        Label(frame_botoes, text="", width=7).grid(row=7, column=7)
        
        # Botoes que ficam na parte de cima do layout, carrega as funcoes
        Button(frame_botoes, text="Cadastrar produto", command=self.registrar_no_banco, width=18, height=1).grid(row=2, column=2) # Botao para cadastrar produto
        Button(frame_botoes, text="Alterar produto", command=self.alterar_no_banco, width=18, height=1).grid(row=2, column=4) # Botao para alterar produto
        Button(frame_botoes, text="Deletar produto", command=self.deletar_do_banco, width=18, height=1).grid(row=2, column=6) # Botao para deletar produto
        Button(frame_botoes, text="Listar produtos", command=self.listar_do_banco, width=18, height=1).grid(row=2, column=8) # Botao para listar produtos
        
        # Criando frame que carrega itens de cadastro
        frame_cadastrar = Frame(self.root, width=900, height=300)
        frame_cadastrar.grid(row=2)

        # Labels vazios para divisoes
        Label(frame_cadastrar, text="", height=2).grid(row=2)
        Label(frame_cadastrar, text="", height=1).grid(row=4)
        Label(frame_cadastrar, text="", height=1).grid(row=6)
        Label(frame_cadastrar, text="", height=1).grid(row=8)
        Label(frame_cadastrar, text="", height=1).grid(row=10)
        Label(frame_cadastrar, text="", height=1).grid(row=12)

        # Botao para pesqusiar um produto especifico
        Button(frame_cadastrar, text="Pesquisar produto \ne autopreencher", command=self.pesquisar_produto_especifico, width=18, height=2).grid(row=1, column=3, rowspan=1)

        self.box_pesquisar = Entry(frame_cadastrar, width=40)
        self.box_pesquisar.grid(row=1, column=1, columnspan=2)

        # Label e entry para 'nome' do produto
        Label(frame_cadastrar, text="Nome do Produto:").grid(row=3, column=1)
        self.box_nome = Entry(frame_cadastrar, width=25)
        self.box_nome.grid(row=3, column=3)

        # Label e entry para 'descricao' do produto
        Label(frame_cadastrar, text="Descrição do Produto:").grid(row=5, column=1)
        self.box_descricao = Entry(frame_cadastrar, width=25)
        self.box_descricao.grid(row=5, column=3)

        # Label e entry para 'quantidade' do produto
        Label(frame_cadastrar, text="Quantidade do Produto:").grid(row=7, column=1)
        self.box_quantidade = Entry(frame_cadastrar, width=25)
        self.box_quantidade.grid(row=7, column=3)

        # Label e entry para 'valor' do produto
        Label(frame_cadastrar, text="Valor do Produto:").grid(row=9, column=1)
        self.box_valor = Entry(frame_cadastrar, width=25)
        self.box_valor.grid(row=9, column=3)

        # Frame usado para carregar o 'text_area'
        frame_text_area = Frame(self.root, width=900, height=200)
        frame_text_area.grid(row=3)

        # Labels vazios para divisoes
        Label(frame_text_area, text="", width=5).grid(column=1)

        # Text area usado para retornar dados ja existentes
        self.text_area = Text(frame_text_area,height=13,width=100)
        self.text_area.grid(row=2,column=2,columnspan=5)

    # Método usado quando o botao 'Cadastrar' é clicado
    def registrar_no_banco(self):
        nome_produto = self.box_nome.get().title() # Pega o valor que esta dentro da box de nome
        descricao_produto = self.box_descricao.get() # Pega o valor que esta dentro da box de descricao
        quantidade_produto = self.box_quantidade.get() # Pega o valor que esta dentro da box de quantidade
        valor_produto = self.box_valor.get() # Pega o valor que esta dentro da box de valor

        if nome_produto and descricao_produto and quantidade_produto and valor_produto: # Verifica se todas as variaveis carregam um valor diferente de nulo
            registrar_produto(nome_produto, descricao_produto, quantidade_produto, valor_produto) # Executa o metodo que se conecta com o banco

            self.limpar_campos() # Executa o metodo que limpa os bancos

            messagebox.showinfo("Sucesso", "Produto cadastrado com sucesso!")
        else:
            messagebox.showerror("Error", "Todos os campos são obrigatorios")

    def alterar_no_banco(self):
        nome_produto = self.box_nome.get()
        descricao_produto = self.box_descricao.get()
        quantidade_produto = self.box_quantidade.get()
        valor_produto = self.box_valor.get()

        if nome_produto and descricao_produto and quantidade_produto and valor_produto:
            atualizar_produto(nome_produto, descricao_produto, quantidade_produto, valor_produto)

            self.limpar_campos()

            messagebox.showinfo("Sucesso", "Produto atualizado com sucesso!")
        else:
            messagebox.showerror("Error", "Todos os campos são obrigatorios")

    def listar_do_banco(self):
            produtos = listar_produtos()
            self.text_area.delete(1.0, END)

            for produto in produtos:
                self.text_area.insert(END, f"-Nome: {produto[1]}, Descrição: {produto[2]}, Quantidade: {produto[3]}, Valor: {produto[4]}\n")
    
    def deletar_do_banco(self):
        produto = self.box_nome.get()
        if produto:
            deletar_produto(produto)
            self.box_nome.delete(0, END)
            messagebox.showinfo("Success", "Produto excluido com sucesso!")
        else:
            messagebox.showerror("Error", "Campo 'Nome' não preenchido ou Produto não encontrado!")

    def pesquisar_produto_especifico(self):
        pesquisa = self.box_pesquisar.get().title()
        self.box_pesquisar.delete(0, END)

        if pesquisa:
            produto_retornado = pesquisar_produto(pesquisa)

            if produto_retornado:
                messagebox.showinfo("Success", f"Produto '{produto_retornado[1]}' encontrado com sucesso, verifique a caixa de texto!")
                self.text_area.delete(1.0, END)
                self.text_area.insert(END, f"Nome: {produto_retornado[1]}, Descrição: {produto_retornado[2]}, Quantidade: {produto_retornado[3]}, Valor: {produto_retornado[4]}")
                
                self.box_nome.insert(0, produto_retornado[1])
                self.box_descricao.insert(0, produto_retornado[2])
                self.box_quantidade.insert(0, produto_retornado[3])
                self.box_valor.insert(0, produto_retornado[4])

            else:
                messagebox.showerror("Error", "Produto não encontrado ou não cadastrado!")
        else:
            messagebox.showerror("Error", "Campo 'Pesquisar' não preenchido!")
        
    def limpar_campos(self):
        self.box_nome.delete(0, END)
        self.box_descricao.delete(0, END)
        self.box_quantidade.delete(0, END)
        self.box_valor.delete(0, END)    

if __name__ == "__main__":
    root = Tk()
    app = crud_produtos(root)
    root.mainloop()