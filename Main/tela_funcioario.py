import tkinter as tk
from tkinter import messagebox
from database_geral import registrar_funcionario
from tkinter import*



class tela_funcionario:
    def __init__(self, root):
        
        self.root = tk.Toplevel(root) 
        self.root.title ("CRUD FUNCIONARIO                                                                                                                                                                       TerraBytes")
        self.root.geometry ("900x700")
        self.root.resizable(width= False, height=False)
        #self.root['bg'] = "gray"


        self.root.transient(root)  # Faz com que a nova janela fique acima da principal
        self.root.grab_set()  # Bloqueia interações na principal até fechar essa


       
        self.criar_funcionario()
    def criar_funcionario(self):
        tk.Label(self.root,text= "Nome: ").place(x= 0, y= 0)
        tk.Label(self.root,text= "Data de Nascimento: ").place(x= 0, y= 30)
        tk.Label(self.root,text= "Data de admissão: ").place(x= 0, y= 60)
        tk.Label(self.root,text= "CPF: ").place(x= 0, y= 90)
        tk.Label(self.root,text= "Cidade: ").place(x= 0, y= 120)
        tk.Label(self.root,text= "Estado: ").place(x= 0, y= 150)
        tk.Label(self.root,text= "Telefone: ").place(x= 0, y= 180)
        tk.Label(self.root,text= "Email: ").place(x= 0, y= 210)
        tk.Label(self.root,text= "Usuario: ").place(x= 0, y= 240)
        tk.Label(self.root,text= "Senha: ").place(x= 0, y= 270)

      

        self.nome_entry = tk.Entry(self.root)
        self.Data_de_nascimento_entry = tk.Entry(self.root)
        self.Data_de_Admissao_entry = tk.Entry(self.root)
        self.CPF_entry = tk.Entry(self.root)
        self.Cidade_entry = tk.Entry(self.root)
        self.UF_entry = tk.Entry(self.root)

        self.Telefone_entry = tk.Entry(self.root)
        self.Email_entry = tk.Entry(self.root)
        self.Usuario_entry = tk.Entry(self.root)
        self.Senha_entry = tk.Entry(self.root)

        self.nome_entry.place(x= 50, y= 0, width= "150")
        self.Data_de_nascimento_entry.place(x= 120, y= 30, width= "100")
        self.Data_de_Admissao_entry.place(x= 110, y= 60, width= "110")
        self.CPF_entry.place(x= 50, y= 90, width= "100")
        self.Cidade_entry.place(x= 50, y= 120,width= "100")
        self.UF_entry.place(x= 50, y= 150, width= "100")
        self.Telefone_entry.place(x= 55, y= 180, width= "95")
        self.Email_entry.place(x= 50, y= 210, width= "100")
        self.Usuario_entry.place(x= 50, y= 240, width= "100")
        self.Senha_entry.place(x= 50, y= 270, width= "100")

        tk.Button(self.root, text= "FAZER LOGIN", command = self.registrar_funcionario).place(x= 0, y= 300)
      
    def registrar_funcionario (self):
        nome = self.nome_entry.get()
        DataDeNascimento= self.Data_de_nascimento_entry.get()
        DataDeAdmissao = self.Data_de_Admissao_entry.get()
        CPF = self.CPF_entry.get()
        Cidade = self.Cidade_entry.get()
        UF = self.UF_entry.get()
        Telefone= self.Telefone_entry.get()
        Email= self.Email_entry.get()
        Usuario = self.Usuario_entry.get()
        Senha = self.Senha_entry.get()

        #fazendo a mensagem de criado ou não criado o funcionario
        if nome and DataDeNascimento and DataDeAdmissao and CPF and Cidade and UF and Telefone and Email and Usuario and Senha:
            registrar_funcionario(nome, DataDeNascimento, DataDeAdmissao,  CPF, Cidade, UF , Telefone, Email, Usuario, Senha)
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
            messagebox.showinfo("Success", "Funcionario criado com Sucesso")
        else:
            messagebox.showerror("Error", "Todos os campos são obrigatorios")




if __name__ == "__main__":
    root = tk.Tk()
    app = tela_funcionario(root)
    root.mainloop()