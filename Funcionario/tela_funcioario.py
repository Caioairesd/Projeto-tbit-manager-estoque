import tkinter as tk
from tkinter import messagebox
from crud_funcionario import login_funcionario, excluir_funcionario, editar_funcionario, buscar_funcionario, listar_funcionarios_crud
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
        # Labels com o texto e sem fundo
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
        self.buscar_entry = tk.Entry(self.root, bg="darkgray")
        self.exibir_id_entry = tk.Entry(self.root, bg="darkgray")

        # Caixas de texto
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
        self.buscar_entry.place(x=310, y=423, width=70)
        

        tk.Label(self.root, text="id:", bg="lightgray").place(x=290, y=420)
        self.funcionario_id_entry = tk.Entry(self.root, bg="darkgray")

        # Botões de funções
        tk.Button(self.root, text="CANCELAR", command=self.cancelar).place(x=450, y=420)
        tk.Button(self.root, text="CRIAR", command=self.login_funcionario).place(x=30, y=420)
        tk.Button(self.root, text="EXCLUIR", command=self.excluir_funcionario).place(x=90, y=420)
        tk.Button(self.root, text="EDITAR", command=self.editar_funcionario).place(x=160, y=420)
        tk.Button(self.root, text="BUSCAR", command=self.buscar_funcionario).place(x=225, y=420)

        self.text_area = tk.Text(self.root, height=3, width=105, bg="lightgray")
        self.text_area.place(x=30, y=480)

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
        

        if nome and Data_de_nascimento and Data_de_admissao and CPF and Cidade and UF and Telefone and Email and Usuario and Senha:
            login_funcionario(nome, Data_de_nascimento, Data_de_admissao, CPF, Cidade, UF, Telefone, Email, Usuario, Senha)
            self.limpar_campos()
            messagebox.showinfo("Success", "Funcionario criado com Sucesso")
        else:
            messagebox.showerror("Error", "Todos os campos são obrigatórios")

    def listar_funcionarios(self):
        funcionarios = listar_funcionarios_crud()
        self.text_area.delete(1.0, tk.END)
        for funcionario in funcionarios:
            self.text_area.insert(tk.END, f"id:{funcionario[0]}, Nome: {funcionario[1]}, Data de Nascimento: {funcionario[2]}, Data de Admissão: {funcionario[3]}, CPF: {funcionario[4]}, Cidade: {funcionario[5]}, UF: {funcionario[6]}, Telefone: {funcionario[7]}, Email: {funcionario[8]}, Usuario: {funcionario[9]}, Senha: {funcionario[10]}\n")

    def buscar_funcionario(self):
        busca = self.buscar_entry.get()
        self.buscar_entry.delete(0, tk.END)

        if busca:
            id_solicitado = buscar_funcionario(busca)

            if id_solicitado:
                messagebox.showinfo("Sucesso", f"Funcionário {id_solicitado[1]} encontrado com sucesso!")
                self.text_area.delete(1.0, tk.END)  # Limpa a área de texto antes de exibir os dados

                # Exibe as informações do funcionário na caixa de texto
                self.text_area.insert(tk.END, f"ID:{id_solicitado[0]}, Nome: {id_solicitado[1]}, Data de Nascimento: {id_solicitado[2]}, Data de Admissão: {id_solicitado[3]}, CPF: {id_solicitado[4]}, Cidade: {id_solicitado[5]}, UF: {id_solicitado[6]}, Telefone: {id_solicitado[7]}, Email: {id_solicitado[8]}, Usuario: {id_solicitado[9]}, Senha: {id_solicitado[10]}\n")

                # Preenche os campos de entrada com os dados encontrados
                self.funcionario_id_entry.insert(0, id_solicitado[0])
                self.nome_entry.insert(0, id_solicitado[1])
                self.Data_de_nascimento_entry.insert(0, id_solicitado[2])
                self.Data_de_Admissao_entry.insert(0, id_solicitado[3])
                self.CPF_entry.insert(0, id_solicitado[4])
                self.Cidade_entry.insert(0, id_solicitado[5])
                self.UF_entry.insert(0, id_solicitado[6])
                self.Telefone_entry.insert(0, id_solicitado[7])
                self.Email_entry.insert(0, id_solicitado[8])
                self.Usuario_entry.insert(0, id_solicitado[9])
                self.Senha_entry.insert(0, id_solicitado[10])
                self.funcionario_id_entry.insert(0, id_solicitado[11])
     
            else:
                messagebox.showerror("Erro", "Funcionário não encontrado")
        else:
            messagebox.showerror("Erro", "Campo de busca vazio")

    def editar_funcionario(self):
        funcionario_id = self.funcionario_id_entry.get()
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

        if funcionario_id and nome and Data_de_nascimento and Data_de_admissao and CPF and Cidade and UF and Telefone and Email and Usuario and Senha:
            editar_funcionario(nome, Data_de_nascimento, Data_de_admissao, CPF, Cidade, UF, Telefone, Email, Usuario, Senha, funcionario_id)
            messagebox.showinfo("Sucesso", "Funcionário atualizado com sucesso")
            self.limpar_campos()
            self.listar_funcionarios()
        else:
            messagebox.showerror("Erro", "Todos os campos são obrigatórios")

    def excluir_funcionario(self):
        funcionario_id = self.funcionario_id_entry.get()
        confirmacao = messagebox.askyesno("Confirmação", "Você realmente deseja deletar esse funcionário?")
        if confirmacao:
            if funcionario_id:
                excluir_funcionario(funcionario_id)
                self.funcionario_id_entry.delete(0, tk.END)
                self.listar_funcionarios()
                messagebox.showinfo("Sucesso", "Funcionário deletado com sucesso!")
            else:
                messagebox.showerror("Erro", "ID do funcionário é obrigatório!")

    def limpar_campos(self):
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
        self.exibir_id_entry.delete(0, tk.END)
        self.funcionario_id_entry.delete(0, tk.END)
        self.text_area.delete(1.0, tk.END)

    def cancelar(self):
        self.limpar_campos()

if __name__ == "__main__":
    root = tk.Tk()
    app = CRUDfuncionario(root)
    root.mainloop()
