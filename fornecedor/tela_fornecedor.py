import tkinter as tk
from tkinter import messagebox
from db_fornecedor import register_fornecedor

class crud_fornecedor:

    def __init__(self,root):
        self.root = root

        #Define os parâmetros de interface da janela
        self.root.geometry("900x750")
        self.root.title("TBit Manager - Menu Fornecedor")
        #self.root.configure(background="white")
        self.root.resizable(width=False,height=False)
        #self.root.attributes("-alpha",1.0)

        self.create_widgets()

    def create_widgets(self):
        #Criação de labels
        tk.Button(self.root,text="Cadastrar",width=15,height=1,command=self.create_fornecedor).place(x=50,y=180)

        #botao_alterar_fornecedor = tk.Button(self.root,text="Alterar",width=20,height=2).place(x=375,y=200)
        #botao_excluir_fornecedor = tk.Button(self.root,text="Excluir",width=20,height=2).place(x=375,y=300)
        #botao_listar_fornecedor = tk.Button(self.root,text="Pesquisar fornecedor",width=20,height=2).place(x=375,y=400)
        
        tk.Label(self.root,text="Fornecedor:").place(x=15,y=150)
        tk.Label(self.root,text="Marca:").place(x=15,y=120)
        tk.Label(self.root,text="Email:").place(x=15,y=90)
        tk.Label(self.root,text="Telefone:").place(x=15,y=60)
        tk.Label(self.root,text="Cidade:").place(x=15,y=30)
        tk.Label(self.root,text="País:").place(x=15,y=0)

        self.fornecedor_entry = tk.Entry(self.root)
        self.marca_entry = tk.Entry(self.root)
        self.email_entry = tk.Entry(self.root)
        self.telefone_entry = tk.Entry(self.root)
        self.cidade_entry = tk.Entry(self.root)
        self.pais_entry = tk.Entry(self.root)

        self.fornecedor_entry.place(x=100,y=150)
        self.marca_entry.place(x=100,y=120)
        self.email_entry.place(x=100,y=90)
        self.telefone_entry.place(x=100,y=60)
        self.cidade_entry.place(x=100,y=30)
        self.pais_entry.place(x=100,y=0)

    def create_fornecedor(self):
        nome_fornecedor = self.fornecedor_entry.get()
        marca_fornecedor = self.marca_entry.get()
        email_fornecedor = self.email_entry.get()
        telefone_fornecedor = self.telefone_entry.get()
        cidade_fornecedor = self.cidade_entry.get()
        pais_fornecedor = self.pais_entry.get()

        
        if nome_fornecedor and marca_fornecedor and email_fornecedor and telefone_fornecedor and cidade_fornecedor and pais_fornecedor:
            register_fornecedor(nome_fornecedor,marca_fornecedor,email_fornecedor,telefone_fornecedor,cidade_fornecedor,pais_fornecedor)
            self.fornecedor_entry.delete(0,tk.END)
            self.marca_entry.delete(0,tk.END)
            self.email_entry.delete(0,tk.END)
            self.telefone_entry.delete(0,tk.END)
            self.cidade_entry.delete(0,tk.END)
            self.pais_entry.delete(0,tk.END)

            messagebox.showinfo("Sucesso","Fornecedor cadastrado com sucesso!")

        else:

            messagebox.showerror("Erro","Todos os campos são obrigatórios!")






if __name__ == "__main__":
    root = tk.Tk()
    app = crud_fornecedor(root)
    root.mainloop()
