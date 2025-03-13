import tkinter as tk
from tkinter import messagebox
from db_fornecedor import register_fornecedor,listar_fornecedor_db,update_fornecedor,delete_fornecedor,pesquisar_fornecedor_db

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
        self.listar_fornecedor()

    def create_widgets(self):
        #Criação de labels

        #Criação de botões
        tk.Button(self.root,text="Cadastrar",width=15,height=1,command=self.create_fornecedor).place(x=50,y=240)

        tk.Button(self.root,text="Alterar",width=15,height=1,command=self.update_fornecedor).place(x=250,y=240)
        tk.Button(self.root,text="Excluir",width=15,height=1,command=self.delete_fornecedor).place(x=500,y=240)
       
        tk.Button(self.root,text="pesquisar e inserir dados",width=30,height=1,command=self.pesquisar_fornecedor).place(x=135,y=415)

        tk.Label(self.root,text="Fornecedor:").place(x=15,y=0)
        tk.Label(self.root,text="Marca:").place(x=15,y=30)
        tk.Label(self.root,text="Email:").place(x=15,y=60)
        tk.Label(self.root,text="Telefone:").place(x=15,y=90)
        tk.Label(self.root,text="Cidade:").place(x=15,y=120)
        tk.Label(self.root,text="País:").place(x=15,y=150)
        tk.Label(self.root,text="ID:").place(x=15,y=180)


        #Criação de campos de entrada de dados
        self.fornecedor_entry = tk.Entry(self.root)
        self.marca_fornecedor_entry = tk.Entry(self.root)
        self.email_fornecedor_entry = tk.Entry(self.root)
        self.telefone_fornecedor_entry = tk.Entry(self.root)
        self.cidade_fornecedor_entry = tk.Entry(self.root)
        self.pais_fornecedor_entry = tk.Entry(self.root)
        self.id_fornecedor_entry = tk.Entry(self.root)
        self.pesquisar_entry = tk.Entry(self.root,width=40)

        #Definindo localização dos campos na tela
        self.fornecedor_entry.place(x=100,y=0)
        self.marca_fornecedor_entry.place(x=100,y=30)
        self.email_fornecedor_entry.place(x=100,y=60)
        self.telefone_fornecedor_entry.place(x=100,y=90)
        self.cidade_fornecedor_entry.place(x=100,y=120)
        self.pais_fornecedor_entry.place(x=100,y=150)
        self.id_fornecedor_entry.place(x=100,y=180)
        self.pesquisar_entry.place(x=360,y=417)

        self.search_area = tk.Text(self.root,height=15,width=80)
        self.search_area.place(x=135,y=450)

    def create_fornecedor(self):
        nome_fornecedor = self.fornecedor_entry.get()
        marca_fornecedor = self.marca_fornecedor_entry.get()
        email_fornecedor = self.email_fornecedor_entry.get()
        telefone_fornecedor = self.telefone_fornecedor_entry.get()
        cidade_fornecedor = self.cidade_fornecedor_entry.get()
        pais_fornecedor = self.pais_fornecedor_entry.get()
       
        
        if nome_fornecedor and marca_fornecedor and email_fornecedor and telefone_fornecedor and cidade_fornecedor and pais_fornecedor:
            register_fornecedor(nome_fornecedor,marca_fornecedor,email_fornecedor,telefone_fornecedor,cidade_fornecedor,pais_fornecedor)
            self.fornecedor_entry.delete(0,tk.END)
            self.marca_fornecedor_entry.delete(0,tk.END)
            self.email_fornecedor_entry.delete(0,tk.END)
            self.telefone_fornecedor_entry.delete(0,tk.END)
            self.cidade_fornecedor_entry.delete(0,tk.END)
            self.pais_fornecedor_entry.delete(0,tk.END)
            self.id_fornecedor_entry.delete(0,tk.END)

            self.listar_fornecedor()

            messagebox.showinfo("Sucesso","Fornecedor cadastrado com sucesso!")

        else:

            messagebox.showerror("Erro","Todos os campos são obrigatórios!")

    def listar_fornecedor(self):
        
        fornecedores = listar_fornecedor_db()
        self.search_area.delete(1.0,tk.END)

        for fornecedor in fornecedores:
                    self.search_area.insert(tk.END,f"ID: {fornecedor[0]},Fornecedor: {fornecedor[1]},Marca:{fornecedor[2]},Email:{fornecedor[3]},Telefone:{fornecedor[4]},Cidade:{fornecedor[5]},Cidade:{fornecedor[6]}\n")

    def pesquisar_fornecedor(self):         
       
        pesquisa = self.pesquisar_entry.get()

        self.pesquisar_entry.delete(0,tk.END)

        if pesquisa:

            id_solicitado = pesquisar_fornecedor_db(pesquisa)

            if id_solicitado:

                
                messagebox.showinfo("Sucesso!","{}Fornecedor encontrado com sucesso!\nVerifique a caixa de texto".format(id_solicitado))
                self.search_area.delete(1.0,tk.END)
                self.search_area.insert(tk.END,f"ID: {id_solicitado[0]},id_solicitado: {id_solicitado[1]},Marca:{id_solicitado[2]},Email:{id_solicitado[3]},Telefone:{id_solicitado[4]},Cidade:{id_solicitado[5]},Cidade:{id_solicitado[6]}\n")

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


    def update_fornecedor(self):
        id_fornecedor = self.id_fornecedor_entry.get() 
        nome_fornecedor=self.fornecedor_entry.get()
        marca_fornecedor =self.marca_fornecedor_entry.get()        
        email_fornecedor =self.email_fornecedor_entry.get()
        telefone_fornecedor =self.telefone_fornecedor_entry.get()
        cidade_fornecedor =self.cidade_fornecedor_entry.get()
        pais_fornecedor = self.pais_fornecedor_entry.get()
        
        if  id_fornecedor and nome_fornecedor and marca_fornecedor and email_fornecedor and telefone_fornecedor and cidade_fornecedor and pais_fornecedor:
            update_fornecedor(nome_fornecedor,marca_fornecedor,email_fornecedor,telefone_fornecedor,cidade_fornecedor,pais_fornecedor,id_fornecedor)
            self.fornecedor_entry.delete(0,tk.END)
            self.marca_fornecedor_entry.delete(0,tk.END)
            self.email_fornecedor_entry.delete(0,tk.END)
            self.telefone_fornecedor_entry.delete(0,tk.END)
            self.cidade_fornecedor_entry.delete(0,tk.END)
            self.pais_fornecedor_entry.delete(0,tk.END)

            self.listar_fornecedor()
            
            messagebox.showinfo("Sucess","informações alteradas com sucesso!")
        else:
            messagebox.showerror("ERROR","Todos os campos são obrigatórios!")

    def delete_fornecedor(self):
        id_fornecedor = self.id_fornecedor_entry.get()
        if id_fornecedor:
            delete_fornecedor(id_fornecedor)

            self.id_fornecedor_entry.delete(0,tk.END)
            self.listar_fornecedor()
            messagebox.showinfo("Sucesso","Fornecedor deletado com sucesso!")
        else:
            messagebox.showerror("Erro","ID do fornecedor é obrigatório!")

    
          

if __name__ == "__main__":
    root = tk.Tk()
    app = crud_fornecedor(root)
    root.mainloop()
