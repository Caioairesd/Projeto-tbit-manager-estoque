
import customtkinter as ctk
from tkinter import messagebox, ttk
from database_geral import consultar_estoque_db, registrar_reabastecimento_db

class tela_reabastecimento:

    def __init__(self,root):
        self.menu_root = root  
        self.root = ctk.CTkToplevel(root)   
        #Define os parâmetros de interface da janela

        self.root.title("TBit Manager - Reabastecimento")
       
        self.root.configure(fg_color='#141C29')

        #ctk.set_appearance_mode("dark")# Deixar o frame no modo escuro-dark

        largura = self.root.winfo_screenwidth()# Expandir tela largura
        altura = self.root.winfo_screenheight()# Expandir tela altura
        self.root.geometry(f"{largura}x{altura}+0+0")# definir expanção

        self.root.grab_set()  # Bloqueia interações na principal até fechar essa

        self.create_widgets()
        self.criar_tabelao()

    def create_widgets(self):

        self.label_text = ctk.CTkLabel(self.root, text="R E A B A S T E C I M E N T O ",font=("Garamond", 60), fg_color="#141C29", text_color='#58A6FF') # Cria um label para o texto
        self.label_text.place(x=570, y=60) # Posiciona o texto
      

        self.right_frame = ctk.CTkFrame(self.root, width=800, height=150, fg_color="#2C3E50")# definir o tamanho e cor do fundo da frame
        self.right_frame.place(x=560, y=170)# definir a expanção da frame

        self.voltar_menu_button = ctk.CTkButton(self.root, text='Voltar',font=('Arial',13),text_color='#C9D1D9', width=90, height= 40,fg_color= '#1B263B', bg_color= '#161B22', command=self.voltar_menu)
        self.voltar_menu_button.place(x=1700, y=900)

        self.combobox_produtos = ctk.CTkComboBox(self.root,height=30,width=140,text_color='#C9D1D9',fg_color='#1B263B',border_color='gray',button_color='#1B263B',button_hover_color='#1B263B',dropdown_fg_color='#161B22',dropdown_text_color='#C9D1D9', dropdown_hover_color='#1B263B', border_width=0,                     bg_color='#1B263B',                 values=self.produtos_combobox()    )
       


        self.pesquisar_produto_entry = ctk.CTkEntry(self.root, height=35, width=150, placeholder_text="Pesquisar produto", text_color='#C9D1D9', fg_color='#1B263B', bg_color='#2C3E50',  border_color='#2C3E50',placeholder_text_color='gray')

        self.quantidade_entrou_entry = ctk.CTkEntry(self.root, height=35, width=150, placeholder_text='Quantidade de produto', text_color='#C9D1D9', fg_color='#1B263B', bg_color='#2C3E50', border_color='#2C3E50', placeholder_text_color='gray')

        self.novo_reabastecimento_button = ctk.CTkButton(self.root, text="ADCIONAR", fg_color='#1B263B', text_color='#C9D1D9', bg_color='#2C3E50', hover_color='#161B22', width=100, height=30, command=self.chamado_reabastecer)


        self.pesquisar_produto_entry.bind("<KeyRelease>", self.filtrar_tabela)

        self.combobox_produtos.place(x=1200, y=180)
        self.quantidade_entrou_entry.place(x=700, y=200)
        self.novo_reabastecimento_button.place(x=870, y=202)
        self.pesquisar_produto_entry.place(x=700, y=250)

        #labels
        self.titulo = ctk.CTkLabel(self.root, text='Pesquisar :',font=("Garamond", 20), fg_color="#2C3E50", text_color='#C9D1D9') # Cria um label para o usuario
        self.titulo.place(x=580, y=250) # Posiciona o label 

        self.titulo = ctk.CTkLabel(self.root, text='Quantidade : ',font=("Garamond", 20), fg_color="#2C3E50", text_color='#C9D1D9') # Cria um label para o usuario
        self.titulo.place(x=580, y=200) # Posiciona o label 

    def criar_tabelao(self):
        # Definir estilo
        style = ttk.Style()
        style.theme_use("alt")
        style.configure("Treeview.Heading", background="#1B263B", foreground="#C9D1D9", anchor="center")
        style.configure("Treeview", background="#2C3E50", foreground="#C9D1D9", fieldbackground="gray", rowheight=25)


        self.treeview = ttk.Treeview(self.root, columns=("id_produto", "nome_produto", "categoria_produto", "quantidade_estoque"), show="headings", height=20)

        self.treeview.heading("id_produto",text="ID do produto")
        self.treeview.heading("nome_produto", text="Nome do produto")
        self.treeview.heading("categoria_produto", text="Categoria do produto")
        self.treeview.heading("quantidade_estoque", text="Quantidade em estoque")

        estoque = consultar_estoque_db()
        for produto in estoque:
            self.treeview.insert("", "end", values=produto)
        
        self.treeview.bind("<ButtonRelease-1>", self.click_na_linha)

        self.treeview.place(relx=0.5, y=620, anchor='center')


    def atualizar_tabela(self, produtos):
         for item in self.treeview.get_children():
            self.treeview.delete(item)

         for produto in produtos:
            self.treeview.insert("", "end", values=produto)

    def filtrar_tabela(self, event):
        estoque = consultar_estoque_db()
        produto_pesquisado = self.pesquisar_produto_entry.get().lower()

        filtragem = [produto for produto in estoque if produto_pesquisado in produto[1].lower()]

        self.atualizar_tabela(filtragem)
    
    def click_na_linha(self, event):
        linha_selecionada = self.treeview.focus()

        if linha_selecionada:
            valores = self.treeview.item(linha_selecionada, "values")
            if valores:
                self.combobox_produtos.set(valores[1])
                
    # CONJUNTO DE FUNÇÕES USADOS PARA A COMBO BOX
    def produtos_combobox(self):
        estoque = consultar_estoque_db()
        nomes_produtos = [nome[1] for nome in estoque]
        return nomes_produtos

    def get_id_produto(self):
        produto_selecionado = self.combobox_produtos.get()
        busca = consultar_estoque_db()

        for produto in busca:
            if produto_selecionado == produto[1]:
                id_produto = produto[0]
                return id_produto

    def chamado_reabastecer(self):
        quantidade = self.quantidade_entrou_entry.get()
        id_produto = self.get_id_produto()

        if id_produto and quantidade:
                registrar_reabastecimento_db(id_produto, quantidade)
                messagebox.showinfo("Sucesso", "Chamado cadastrado! Banco de dados atualizando...")

                estoque = consultar_estoque_db()
                self.atualizar_tabela(estoque)

                self.pesquisar_produto_entry.delete(0, ctk.END)
                self.quantidade_entrou_entry.delete(0, ctk.END)
        else:
            messagebox.showerror("Error", "Ocorreu um erro na tentativa de cadastrar novo chamado!")

    def voltar_menu(self):
        
       # from menu_adm import menu_admin
        self.root.destroy()  # Fecha a janela atual
        self.menu_root.deiconify()
    
if __name__ == "__main__":
    root = ctk.CTk()
    app = tela_reabastecimento(root)
    root.mainloop()
