import tkinter as tk
from tkinter import messagebox
from crud_funcionario import fazer_login_funcionario


class CRUDfuncioario:
    def __init__(self, root):
        self.root = root 
        self.root.title ("CRUD FUNCIONARIO")
        
        

        self.criar_funcionario()
    def criar_funcionario(self):
        tk.Label(self.root,text= "Nome: ").grid(row= 0, column= 1)
        tk.Label(self.root,text= "Data de Nascimaento: ").grid(row= 1, column= 1)
        tk.Label(self.root,text= "data de admisão: ").grid(row= 2, column= 1)
        tk.Label(self.root,text= "CPF: ").grid(row= 3, column= 1)
        tk.Label(self.root,text= "Cidade: ").grid(row= 4, column= 1)
        tk.Label(self.root,text= "UF: ").grid(row= 5, column= 1)
        tk.Label(self.root,text= "telefone: ").grid(row= 5, column= 1)
        tk.Label(self.root,text= "Email: ").grid(row= 6, column= 1)
        tk.Label(self.root,text= "Usuario: ").grid(row= 7, column= 1)
        tk.Label(self.root,text= "Senha: ").grid(row= 8, column= 1)

        self.nome_entry = tk.Entry(self.root)
        self.Data_de_nascimento_entry = tk.Entry(self.root)
        self.Data_de_Admissao_entry = tk.Entry(self.root)
        self.CPF_entry = tk.Entry(self.root)
        self.Cidade_entry = tk.Entry(self.root)
        self.UF_entry = tk.Entry(self.root)
        self.Estado_entry = tk.Entry(self.root)
        self.Telefone_entry = tk.Entry(self.root)
        self.Email_entry = tk.Entry(self.root)
        self.Usuario_entry = tk.Entry(self.root)
        self.Senha_entry = tk.Entry(self.root)

        tk.Button(self.root, text= "Funcionario Login", command = self.fazer_login_funcionario).grid(row= 6, column= 0, columnspan= 1)
     
    def fazer_login_funcionario (self):
        nome = self.nome_entry.get()
        DataDeNascimento= self.Data_de_nascimento_entry.get()
        DataDeAdmissao = self.Data_de_Admissao_entry.get()
        CPF = self.CPF_entry.get()
        Cidade = self.Cidade_entry.get()
        UF = self.Estado_entry.get()
        Telefone= self.Telefone_entry.get()
        Email= self.Email_entry.get()
        Usuario = self.Usuario_entry.get()
        Senha = self.Senha_entry.get()

        #fazendo a mensagem de criado ou não criado o funcionario
        if nome and DataDeNascimento and DataDeAdmissao and Cidade and CPF and UF and Telefone and Email and Usuario and Senha :
            fazer_login_funcionario(nome, DataDeNascimento, DataDeAdmissao, Cidade, CPF, UF, Telefone, Email, Usuario, Senha)
            self.nome_entry.delete(0,tk.END)
            self.Data_de_nascimento_entry.delete(0,tk.END)
            self.Data_de_Admissao_entry.delete(0,tk.END)
            self.CPF_entry.delete(0,tk.END)
            self.Cidade_entry.delete(0,tk.END)
            self.UF_entry.delete(0,tk.END)
            self.Estado_entry.delete(0,tk.END)
            self.Telefone_entry.delete(0,tk.END)
            self.Email_entry.delete(0,tk.END)
            self.Usuario_entry.delete(0,tk.END)
            self.Senha_entry.delete(0,tk.END)
            messagebox.showinfo("Success", "Funcionario criado com Sucesso")
        else:
            messagebox.showerror("Error", "Todos os campos são obrigatorios")


if __name__ == "__main__":
    root = tk.Tk()
    app = CRUDfuncioario(root)
    root.mainloop()


