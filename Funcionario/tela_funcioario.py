import tkinter as tk
from tkinter import messagebox
from crud_funcionario import login_funcionario,excluir_funcionario, editar_funcionario, buscar_funcionario
from tkinter import *


class CRUDfuncionario:
    def __init__(self, root):
        self.root = root
        self.root.title("CRUD FUNCIONARIO                                                                                                                                                                       TerraBytes")
        self.root.geometry("900x700")
        self.root.resizable(width=False, height=False)

       
        self.root.config(bg="lightgray")

        self.tela_funcionario()
       
        
       
 
    def tela_funcionario(self):

        #Labels com o texto e sem fundo
       
        tk.Label(self.root, text="Nome:", bg="lightgray").place(x=30, y=20)
        tk.Label(self.root, text="Data de Nascimento:", bg="lightgray").place(x=30, y=60)
        tk.Label(self.root, text="Data de admissão:",  bg="lightgray").place(x=30, y=100)
        tk.Label(self.root, text="CPF:", bg="lightgray").place(x=30, y=140)
        tk.Label(self.root, text="Cidade:", bg="lightgray").place(x=30, y=180)
        tk.Label(self.root, text="Estado:", bg="lightgray").place(x=30, y=220)
        tk.Label(self.root, text="Telefone:", bg="lightgray").place(x=30, y=260)
        tk.Label(self.root, text="Email:", bg="lightgray").place(x=30, y=300)
        tk.Label(self.root, text="Usuario:", bg="lightgray").place(x=30, y=340)
        tk.Label(self.root, text="Senha:", bg="lightgray").place(x=30, y=380)
        

        

        # Caixas cinza escuro 
        
        self.nome_entry  = tk.Entry(self.root, bg="darkgray")
        self.Data_de_nascimento_entry = tk.Entry(self.root, bg="darkgray")
        self.Data_de_Admissao_entry = tk.Entry(self.root, bg="darkgray")
        self.CPF_entry = tk.Entry(self.root, bg="darkgray")
        self.Cidade_entry = tk.Entry(self.root, bg="darkgray")
        self.UF_entry = tk.Entry(self.root, bg="darkgray")
        self.Telefone_entry = tk.Entry(self.root, bg="darkgray")
        self.Email_entry = tk.Entry(self.root, bg="darkgray")
        self.Usuario_entry = tk.Entry(self.root, bg="darkgray")
        self.Senha_entry = tk.Entry(self.root, bg="darkgray", show="*") 


        #caixas de texto

        self.nome_entry.place(x=180, y=20, width=250)
        self.Data_de_nascimento_entry.place(x=180, y=60, width=250)
        self.Data_de_Admissao_entry.place(x=180, y=100, width=250)
        self.CPF_entry.place(x=180, y=140, width=250)
        self.Cidade_entry.place(x=180, y=180, width=250)
        self.UF_entry.place(x=180, y=220, width=250)
        self.Telefone_entry.place(x=180, y=260, width=250)
        self.Email_entry.place(x=180, y=300, width=250)
        self.Usuario_entry.place(x=180, y=340, width=250)
        self.Senha_entry.place(x=180, y=380, width=250)


        tk.Label(self.root, text="ID:", bg="lightgray").place(x=290, y=463)
        self.funcionario_id_entry = tk.Entry(self.root, bg="darkgray")
        self.funcionario_id_entry.place(x=310, y=465, width=70 )

        #botôes de funcões
        tk.Button(self.root, text="CRIAR", command=self.login_funcionario).place(x=30, y=460)
        tk.Button(self.root, text="EXCLUIR", command=self.excluir_funcionario).place(x=90, y=460)
        tk.Button(self.root, text="EDITAR", command=self.editar_funcionario).place(x=160, y=460)
        tk.Button(self.root, text="BUSCAR", command=self.buscar_funcionario).place(x=225, y=460)

    def login_funcionario(self):

        nome = self.nome_entry.get()
        Data_de_nascimento = self.Data_de_nascimento_entry.get()
        Data_de_admissao = self.Data_de_Admissao_entry.get()
        CPF = self.CPF_entry.get()
        Cidade = self.Cidade_entry.get()
        UF = self.UF_entry.get()
        Telefone = self.Telefone_entry.get()
        Email = self.Email_entry.get()
        Usuario = self.Usuario_entry.get()
        Senha = self.Senha_entry.get()
        if nome and Data_de_nascimento and Data_de_admissao and CPF and Cidade and UF and Telefone and Email and Usuario and Senha :
           
            login_funcionario(nome, Data_de_nascimento, Data_de_admissao, CPF, Cidade, UF, Telefone, Email, Usuario, Senha) 
            self.nome_entry.delete(0, tk.END)
            self.Data_de_nascimento_entry.delete(0, tk.END)
            self.Data_de_Admissao_entry.delete(0, tk.END)
            self.CPF_entry.delete(0, tk.END)
            self.Cidade_entry.delete(0, tk.END)
            self.UF_entry.delete(0, tk.END)
            self.Telefone_entry.delete(0, tk.END)
            self.Email_entry.delete(0, tk.END)
            self.Usuario_entry.delete(0, tk.END)
            self.Senha_entry.delete(0, tk.END)

            messagebox.showinfo("Success", "Funcionario criado com Sucesso")
           
        else:
            messagebox.showerror("Error", "Todos os campos são obrigatórios")


        
    def editar_funcionario(self):

        
        funcionario_id = self.funcionario_id_entry.get()
        nome = self.nome_entry.get()
        nascimento = self.Data_de_nascimento_entry.get()    
        admissao = self.Data_de_Admissao_entry.get()  
        CPF = self.CPF_entry.get()
        cidade = self.Cidade_entry.get()
        UF = self.UF_entry.get()
        telefone = self.Telefone_entry.get()
        Email = self.Email_entry.get()
        usuario = self.Usuario_entry.get()    
        senha = self.Senha_entry.get()  

        if funcionario_id and nome and nascimento and admissao and CPF and cidade and UF and telefone and Email  and usuario and  senha:
            editar_funcionario (nome, nascimento,admissao, CPF, cidade, UF, telefone, Email, usuario, senha, funcionario_id)
            self.nome_entry.delete(0,tk.END)
            self.Data_de_nascimento_entry.delete(0,tk.END)
            self.Data_de_Admissao_entry.delete(0,tk.END)
            self.CPF_entry.delete(0,tk.END)
            self.Cidade_entry.delete(0,tk.END)
            self.UF_entry.delete(0,tk.END)
            self.Telefone_entry.delete(0,tk.END)
            self.Email_entry.delete(0,tk.END)
            self.Senha_entry.delete(0,tk.END)
            self.funcionario_id_entry.delete(0,tk.END)

            messagebox.showinfo("Sucess", "Funcionario atualizado com sucesso")
        else:
            messagebox.showerror("Error", "ID do funcioonario é obrigatorio")
        

    def excluir_funcionario(self):
        funcioanrio_id = self.funcionario_id_entry.get()
        if funcioanrio_id:
            excluir_funcionario(funcioanrio_id)
            self.funcionario_id_entry.delete(0,tk.END)
            messagebox.showinfo ("Sucess", "Funcionario excluido com sucesso!")
        else:
            messagebox.showerror ("Error", "ID do funcioonario é obrigatorio")
    def buscar_funcionario (self):
        self.text_area = tk.Text(self.root, height = 10, width=100,  bg="lightgray")
        self.text_area.place(x= 30, y= 500 )
        id = self.funcionario_id_entry.get()
        funcionario = buscar_funcionario(id)
        self.text_area.delete(1.0, tk.END)   
        self.text_area.insert(tk.END,f"ID:{funcionario [0]}, nome: {funcionario [1]}, Data_de_nascimento: {funcionario[2]},Data_de_admissao:{funcionario[3]}, CPF:{funcionario[4]}, Cidade:{funcionario[5]}, UF:{funcionario[6]}, Telefone:{funcionario[7]}, Email:{funcionario[8]}, Usuario: {funcionario[9]}\n"  ) 

    def limpar_campos(self):
        self.nome_entry.delete(0,tk.END)
        self.Data_de_nascimento_entry.delete(0,tk.END)
        self.Data_de_Admissao_entry.delete(0,tk.END) 
        self.CPF_entry.delete(0,tk.END) 
        self.Cidade_entry.delete(0,tk.END)
        self.UF_entry.delete(0,tk.END) 
        self.Telefone_entry.delete(0,tk.END) 
        self.Email_entry.delete(0,tk.END) 
        self.Usuario_entry.delete(0,tk.END) 
        self.Senha_entry.delete(0,tk.END) 
if __name__ == "__main__":
    root = tk.Tk()
    app = CRUDfuncionario(root)
    root.mainloop()
