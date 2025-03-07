# Importacoes necessarias
from tkinter import * 
from tkinter import messagebox
from tkinter import ttk
from db_produto import registrar_produto

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
        margem_de_cima = Label(frame_botoes, text="", height=2).grid(row=1, column=1)
        margem_da_esquerda = Label(frame_botoes, text="", width=10).grid(row=1, column=1)
        divisao1 = Label(frame_botoes, text="", width=7).grid(row=3, column=3)
        divisao2 = Label(frame_botoes, text="", width=7).grid(row=5, column=5)
        divisao3 = Label(frame_botoes, text="", width=7).grid(row=7, column=7)
        
        # Botoes necessarios
        botao_menu_cadastrar = Button(frame_botoes, text="Cadastrar produto", command=self.menu_cadastrar, width=18, height=1).grid(row=2, column=2)
        botao_menu_alterar = Button(frame_botoes, text="Alterar produto", width=18, height=1).grid(row=2, column=4)
        botao_menu_deletar = Button(frame_botoes, text="Deletar produto", width=18, height=1).grid(row=2, column=6)
        botao_menu_pesquisar = Button(frame_botoes, text="Pesquisar produto", width=18, height=1).grid(row=2, column=8)
        
    def menu_cadastrar(self):
        # Criando frame que carrega itens de cadastro
        frame_cadastrar = Frame(self.root, width=900, height=500)
        frame_cadastrar.grid(row=2)

        # Labels vazios para divisoes
        divisao = Label(frame_cadastrar, text="", height=1).grid(row=2)
        divisao = Label(frame_cadastrar, text="", height=1).grid(row=4)
        divisao = Label(frame_cadastrar, text="", height=1).grid(row=6)
        divisao = Label(frame_cadastrar, text="", height=2).grid(row=8)
        divisao = Label(frame_cadastrar, text="", height=1).grid(row=10)

        # Label e entry para 'nome' do produto
        label_nome = Label(frame_cadastrar, text="Nome do Produto:").grid(row=1, column=1)
        self.box_nome = Entry(frame_cadastrar, width=25).grid(row=1, column=3)

        # Label e entry para 'descricao' do produto
        label_descricao = Label(frame_cadastrar, text="Descrição do Produto:").grid(row=3, column=1)
        self.box_descricao = Entry(frame_cadastrar, width=25).grid(row=3, column=3)

        # Label e entry para 'quantidade' do produto
        label_quantidade = Label(frame_cadastrar, text="Quantidade do Produto:").grid(row=5, column=1)
        self.box_quantidade = Entry(frame_cadastrar, width=25).grid(row=5, column=3)
        
        # Label e entry para 'valor' do produto
        label_valor = Label(frame_cadastrar, text="Valor do Produto:").grid(row=7, column=1)
        self.box_valor = Entry(frame_cadastrar, width=25).grid(row=7, column=3)

        # Botoes 'registrar' e 'voltar'
        botao_registrar_produto = Button(frame_cadastrar, text="REGISTRAR", command=self.registrar_no_banco, width=12, height=1).grid(row=9, column=2)
        botao_voltar = Button(frame_cadastrar, text="VOLTAR", width=12, height=1).grid(row=11, column=2)

    def registrar_no_banco(self):
        nome_produto = self.box_nome.get()
        descricao_produto = self.box_descricao.get()
        quantidade_produto = self.box_quantidade.get()
        valor_produto = self.box_valor.get()

        if nome_produto and descricao_produto and quantidade_produto and valor_produto:
            registrar_produto(nome_produto, descricao_produto, quantidade_produto, valor_produto)

            self.box_nome.delete(0, Tk.END)
            self.box_descricao.delete(0, Tk.END)
            self.box_quantidade.delete(0, Tk.END)
            self.box_valor.delete(0, Tk.END)

            messagebox.showinfo("Sucesso", "Produto cadastrado com sucesso!")
        else:
            messagebox.showerror("Error", "Todos os campos são obrigatorios")

if __name__ == "__main__":
    root = Tk()
    app = crud_produtos(root)
    root.mainloop()