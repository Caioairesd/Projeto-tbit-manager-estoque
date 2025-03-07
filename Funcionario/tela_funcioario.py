import tkinter as tk
from tkinter import messagebox
from crud_funcionario import fazer_login_funcionario
from tkinter import*



class CRUDfuncioario:
    def __init__(self, root):
        self.root = root 
        self.root.title ("CRUD FUNCIONARIO")
        self.root.geometry ("900x700")
        #self.root['bg'] = "MIDNIGHTBLUE"
       

        
        

        self.criar_funcionario()
    def criar_funcionario(self):
        tk.Label(self.root,text= "Nome: ").place(x= 0, y= 0)
        tk.Label(self.root,text= "Data de Nascimento: ").place(x= 0, y= 20)
        tk.Label(self.root,text= "Data de admissão: ").place(x= 0, y= 40)
        tk.Label(self.root,text= "CPF: ").place(x= 0, y= 60)
        tk.Label(self.root,text= "Cidade: ").place(x= 0, y= 80)
        tk.Label(self.root,text= "Estado: ").place(x= 0, y= 100)
        tk.Label(self.root,text= "Telefone: ").place(x= 0, y= 120)
        tk.Label(self.root,text= "Email: ").place(x= 0, y= 140)
        tk.Label(self.root,text= "Usuario: ").place(x= 0, y= 160)
        tk.Label(self.root,text= "Senha: ").place(x= 0, y= 180)

      

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

        self.nome_entry.place(x= 50, y= 0)
        self.Data_de_nascimento_entry.place(x= 50, y= 20)
        self.Data_de_Admissao_entry.grid(row= 2, column= 10)
        self.CPF_entry.grid(row= 3, column= 10)
        self.Cidade_entry.grid(row= 4, column= 10)
        self.UF_entry.grid(row= 5, column= 10)
        self.Estado_entry.grid(row= 6, column= 10)
        self.Telefone_entry.grid(row= 7, column= 10)
        self.Email_entry.grid(row= 8, column= 10)
        self.Usuario_entry.place(x= 100, y= 180)

        tk.Button(self.root, text= "Funcionario Login", command = self.fazer_login_funcionario)
        tk.Button.place(x= 200, y=290)
     
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


