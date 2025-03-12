import tkinter as tk
from tkinter import messagebox
from db_fornecedor import register_fornecedor,read_fornecedor,update_fornecedor,delete_fornecedor

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
        tk.Button(self.root,text="Cadastrar",width=15,height=1,command=self.create_fornecedor).place(x=50,y=240)

        tk.Button(self.root,text="Alterar",width=15,height=1,command=self.update_fornecedor).place(x=250,y=240)
        tk.Button(self.root,text="Excluir",width=15,height=1,command=self.delete_fornecedor).place(x=500,y=240)
        tk.Button(self.root,text="Pesquisar",width=15,height=1,command=self.read_fornecedor).place(x=750,y=240)
        
        tk.Label(self.root,text="Fornecedor:").place(x=15,y=0)
        tk.Label(self.root,text="Marca:").place(x=15,y=30)
        tk.Label(self.root,text="Email:").place(x=15,y=60)
        tk.Label(self.root,text="Telefone:").place(x=15,y=90)
        tk.Label(self.root,text="Cidade:").place(x=15,y=120)
        tk.Label(self.root,text="País:").place(x=15,y=150)
        tk.Label(self.root,text="ID:").place(x=15,y=180)

        self.fornecedor_entry = tk.Entry(self.root)
        self.marca_entry = tk.Entry(self.root)
        self.email_entry = tk.Entry(self.root)
        self.telefone_entry = tk.Entry(self.root)
        self.cidade_entry = tk.Entry(self.root)
        self.pais_entry = tk.Entry(self.root)
        self.id_fornecedor_entry = tk.Entry(self.root)

        self.fornecedor_entry.place(x=100,y=0)
        self.marca_entry.place(x=100,y=30)
        self.email_entry.place(x=100,y=60)
        self.telefone_entry.place(x=100,y=90)
        self.cidade_entry.place(x=100,y=120)
        self.pais_entry.place(x=100,y=150)
        self.id_fornecedor_entry.place(x=100,y=180)

        self.search_area = tk.Text(self.root,height=10,width=80)
        self.search_area.place(x=135,y=300)

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
            self.id_fornecedor_entry.delete(0,tk.END)

            messagebox.showinfo("Sucesso","Fornecedor cadastrado com sucesso!")

        else:

            messagebox.showerror("Erro","Todos os campos são obrigatórios!")
    def read_fornecedor(self):
        
        fornecedores = read_fornecedor()
        self.search_area.delete(1.0,tk.END)

        for fornecedor in fornecedores:
                    self.search_area.insert(tk.END,f"ID: {fornecedor[0]},Fornecedor: {fornecedor[1]},Marca:{fornecedor[2]},Email:{fornecedor[3]},Telefone:{fornecedor[4]},Cidade:{fornecedor[5]},Cidade:{fornecedor[6]}\n")
                        
       

    def update_fornecedor(self):
        id_fornecedor = self.id_fornecedor_entry.get() 
        nome_fornecedor=self.fornecedor_entry.get()
        marca_fornecedor =self.marca_entry.get()        
        email_fornecedor =self.email_entry.get()
        telefone_fornecedor =self.telefone_entry.get()
        cidade_fornecedor =self.cidade_entry.get()
        pais_fornecedor = self.pais_entry.get()
        
        if  id_fornecedor and nome_fornecedor and marca_fornecedor and email_fornecedor and telefone_fornecedor and cidade_fornecedor and pais_fornecedor:
            update_fornecedor(nome_fornecedor,marca_fornecedor,email_fornecedor,telefone_fornecedor,cidade_fornecedor,pais_fornecedor,id_fornecedor)
            self.fornecedor_entry.delete(0,tk.END)
            self.marca_entry.delete(0,tk.END)
            self.email_entry.delete(0,tk.END)
            self.telefone_entry.delete(0,tk.END)
            self.cidade_entry.delete(0,tk.END)
            self.pais_entry.delete(0,tk.END)
            
            messagebox.showinfo("Sucess","informações alteradas com sucesso!")
        else:
            messagebox.showerror("ERROR","Todos os campos são obrigatórios!")
    def delete_fornecedor(self):
        id_fornecedor = self.id_fornecedor_entry.get()
        if id_fornecedor:
            delete_fornecedor(id_fornecedor)

            self.id_fornecedor_entry.delete(0,tk.END)
            messagebox.showinfo("Sucesso","Fornecedor deletado com sucesso!")
        else:
            messagebox.showerror("Erro","ID do fornecedor é obrigatório!")
        
        






if __name__ == "__main__":
    root = tk.Tk()
    app = crud_fornecedor(root)
    root.mainloop()
