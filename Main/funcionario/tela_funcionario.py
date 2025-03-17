import tkinter as tk
from tkinter import messagebox
from database_geral import register_funcionario_db, delete_funcionario_db, update_funcionario_db, pesquisar_funcionario_db, listar_funcionarios_db
from tkinter import *


class tela_funcionario_admin:
    def __init__(self, root):
        
        self.root = tk.Toplevel(root) 
        self.root.title("CRUD FUNCIONARIO TerraBytes")
        self.root.geometry("900x700")
        self.root.resizable(width=False, height=False)

        self.root.transient(root)  # Mantém a janela no topo
        self.root.grab_set()  # Bloqueia interações na principal até fechar essa

        self.root.config(bg="lightgray")
        self.create_widgets()

        self.listar_funcionarios()

    def create_widgets(self):
        # Labels com o texto e sem fundo
        tk.Label(self.root, text="Nome:", bg="lightgray").place(x=30, y=20)
        tk.Label(self.root, text="Data de Nascimento:", bg="lightgray").place(x=30, y=60)
        tk.Label(self.root, text="Data de Admissão:",  bg="lightgray").place(x=30, y=100)
        tk.Label(self.root, text="CPF:", bg="lightgray").place(x=30, y=140)
        tk.Label(self.root, text="Cidade:", bg="lightgray").place(x=30, y=180)
        tk.Label(self.root, text="Estado:", bg="lightgray").place(x=30, y=220)
        tk.Label(self.root, text="Telefone:", bg="lightgray").place(x=30, y=260)
        tk.Label(self.root, text="Email:", bg="lightgray").place(x=30, y=300)
        tk.Label(self.root, text="Usuario:", bg="lightgray").place(x=30, y=340)
        tk.Label(self.root, text="Senha:", bg="lightgray").place(x=30, y=380)
        

        # Caixas cinza escuro
        self.nome_funcionario_entry  = tk.Entry(self.root, bg="darkgray")
        self.data_nascimento_funcionario_entry = tk.Entry(self.root, bg="darkgray")
        self.data_admissao_funcionario_entry = tk.Entry(self.root, bg="darkgray")
        self.cpf_funcionario_entry = tk.Entry(self.root, bg="darkgray")
        self.cidade_funcionario_entry = tk.Entry(self.root, bg="darkgray")
        self.uf_funcionario_entry = tk.Entry(self.root, bg="darkgray")
        self.telefone_funcionario_entry = tk.Entry(self.root, bg="darkgray")
        self.email_funcionario_entry = tk.Entry(self.root, bg="darkgray")
        self.usuario_funcionario_entry = tk.Entry(self.root, bg="darkgray")
        self.senha_funcionario_entry = tk.Entry(self.root, bg="darkgray", show="*")
        self.buscar_funcionario_entry = tk.Entry(self.root, bg="darkgray")
        self.exibir_id_entry = tk.Entry(self.root, bg="darkgray")

        # Caixas de texto
        self.nome_funcionario_entry.place(x=180, y=20, width=250)
        self.data_nascimento_funcionario_entry.place(x=180, y=60, width=250)
        self.data_admissao_funcionario_entry.place(x=180, y=100, width=250)
        self.cpf_funcionario_entry.place(x=180, y=140, width=250)
        self.cidade_funcionario_entry.place(x=180, y=180, width=250)
        self.uf_funcionario_entry.place(x=180, y=220, width=250)
        self.telefone_funcionario_entry.place(x=180, y=260, width=250)
        self.email_funcionario_entry.place(x=180, y=300, width=250)
        self.usuario_funcionario_entry.place(x=180, y=340, width=250)
        self.senha_funcionario_entry.place(x=180, y=380, width=250)
        self.buscar_funcionario_entry.place(x=660, y=453, width=70)
        

        tk.Label(self.root, text="Busca por ID:", bg="lightgray").place(x=565, y=450)
        self.id_funcionario_entry = tk.Entry(self.root, bg="darkgray")

        # Botões de funções
        tk.Button(self.root, text="CANCELAR", command=self.cancelar).place(x=800, y=450)
        tk.Button(self.root, text="REGISTRAR", command=self.registrar_funcionario).place(x=30, y=420)
        tk.Button(self.root, text="EXCLUIR", command=self.delete_funcionario).place(x=120, y=420)
        tk.Button(self.root, text="EDITAR", command=self.update_funcionario).place(x=195, y=420)
        tk.Button(self.root, text="BUSCAR", command=self.pesquisar_funcionario).place(x=740, y=450)

        self.text_area = tk.Text(self.root, height=12, width=105, bg="lightgray")
        self.text_area.place(x=30, y=480)

    def registrar_funcionario(self):
        nome_funcionario = self.nome_funcionario_entry.get()
        data_nascimento_funcionario_invertida = self.data_nascimento_funcionario_entry.get()
        data_admissao_funcionario_invertida = self.data_admissao_funcionario_entry.get()
        CPF = self.cpf_funcionario_entry.get()
        Cidade = self.cidade_funcionario_entry.get()
        UF = self.uf_funcionario_entry.get()
        Telefone = self.telefone_funcionario_entry.get()
        Email = self.email_funcionario_entry.get()
        Usuario = self.usuario_funcionario_entry.get()
        Senha = self.senha_funcionario_entry.get()
        
        data_nascimento_funcionario = self.inverter_data(data_nascimento_funcionario_invertida)
        data_admissao_funcionario = self.inverter_data(data_admissao_funcionario_invertida)

        if nome_funcionario and data_nascimento_funcionario and data_admissao_funcionario and CPF and Cidade and UF and Telefone and Email and Usuario and Senha:
            register_funcionario_db(nome_funcionario, data_nascimento_funcionario, data_admissao_funcionario, CPF, Cidade, UF, Telefone, Email, Usuario, Senha)
            self.limpar_campos()
            messagebox.showinfo("Success", "Funcionario criado com Sucesso")
        else:
            messagebox.showerror("Error", "Todos os campos são obrigatórios")

    def listar_funcionarios(self):
        funcionarios = listar_funcionarios_db()
        self.text_area.delete(1.0, tk.END)
        for funcionario in funcionarios:
            self.text_area.insert(tk.END, f"id:{funcionario[0]}, Nome: {funcionario[1]}, Data de Nascimento: {funcionario[2]}, Data de Admissão: {funcionario[3]}, CPF: {funcionario[4]}, Cidade: {funcionario[5]}, UF: {funcionario[6]}, Telefone: {funcionario[7]}, Email: {funcionario[8]}, Usuario: {funcionario[9]}, Senha: {funcionario[10]}\n\n")

    def pesquisar_funcionario(self):
        busca = self.buscar_funcionario_entry.get()
        self.buscar_funcionario_entry.delete(0, tk.END)

        if busca:
            id_solicitado = pesquisar_funcionario_db(busca)

            if id_solicitado:
                messagebox.showinfo("Sucesso", f"Funcionário {id_solicitado[1]} encontrado com sucesso!")
                self.limpar_campos() # Limpa todos os campos antes de inserir novos dados
                self.text_area.delete(1.0, tk.END)  # Limpa a área de texto antes de exibir os dados

                # Exibe as informações do funcionário na caixa de texto
                self.text_area.insert(tk.END, f"ID:{id_solicitado[0]}, Nome: {id_solicitado[1]}, Data de Nascimento: {id_solicitado[2]}, Data de Admissão: {id_solicitado[3]}, CPF: {id_solicitado[4]}, Cidade: {id_solicitado[5]}, UF: {id_solicitado[6]}, Telefone: {id_solicitado[7]}, Email: {id_solicitado[8]}, Usuario: {id_solicitado[9]}, Senha: {id_solicitado[10]}\n")

                # Preenche os campos de entrada com os dados encontrados
                self.id_funcionario_entry.insert(0, id_solicitado[0])
                self.nome_funcionario_entry.insert(0, id_solicitado[1])
                self.data_nascimento_funcionario_entry.insert(0, id_solicitado[2])
                self.data_admissao_funcionario_entry.insert(0, id_solicitado[3])
                self.cpf_funcionario_entry.insert(0, id_solicitado[4])
                self.cidade_funcionario_entry.insert(0, id_solicitado[5])
                self.uf_funcionario_entry.insert(0, id_solicitado[6])
                self.telefone_funcionario_entry.insert(0, id_solicitado[7])
                self.email_funcionario_entry.insert(0, id_solicitado[8])
                self.usuario_funcionario_entry.insert(0, id_solicitado[9])
                self.senha_funcionario_entry.insert(0, id_solicitado[10])
     
            else:
                messagebox.showerror("Erro", "Funcionário não encontrado")
        else:
            messagebox.showerror("Erro", "Campo de busca vazio")

    def update_funcionario(self):
        id_funcionario = self.id_funcionario_entry.get()
        nome_funcionario = self.nome_funcionario_entry.get()
        data_nascimento_funcionario = self.data_nascimento_funcionario_entry.get()
        data_admissao_funcionario = self.data_admissao_funcionario_entry.get()
        CPF = self.cpf_funcionario_entry.get()
        Cidade = self.cidade_funcionario_entry.get()
        UF = self.uf_funcionario_entry.get()
        Telefone = self.telefone_funcionario_entry.get()
        Email = self.email_funcionario_entry.get()
        Usuario = self.usuario_funcionario_entry.get()
        Senha = self.senha_funcionario_entry.get()

        if id_funcionario and nome_funcionario and data_nascimento_funcionario and data_admissao_funcionario and CPF and Cidade and UF and Telefone and Email and Usuario and Senha:
            update_funcionario_db(nome_funcionario, data_nascimento_funcionario, data_admissao_funcionario, CPF, Cidade, UF, Telefone, Email, Usuario, Senha, id_funcionario)
            messagebox.showinfo("Sucesso", "Funcionário atualizado com sucesso")
            self.limpar_campos()
            self.listar_funcionarios()
        else:
            messagebox.showerror("Erro", "Todos os campos são obrigatórios")

    def delete_funcionario(self):
        id_funcionario = self.id_funcionario_entry.get()
        confirmacao = messagebox.askyesno("Confirmação", "Você realmente deseja deletar esse funcionário?")
        if confirmacao:
            if id_funcionario:
                delete_funcionario_db(id_funcionario)
                self.id_funcionario_entry.delete(0, tk.END)
                self.listar_funcionarios()
                messagebox.showinfo("Sucesso", "Funcionário deletado com sucesso!")
            else:
                messagebox.showerror("Erro", "ID do funcionário é obrigatório!")

    def limpar_campos(self):
        self.nome_funcionario_entry.delete(0, tk.END)
        self.data_nascimento_funcionario_entry.delete(0, tk.END)
        self.data_admissao_funcionario_entry.delete(0, tk.END)
        self.cpf_funcionario_entry.delete(0, tk.END)
        self.cidade_funcionario_entry.delete(0, tk.END)
        self.uf_funcionario_entry.delete(0, tk.END)
        self.telefone_funcionario_entry.delete(0, tk.END)
        self.email_funcionario_entry.delete(0, tk.END)
        self.usuario_funcionario_entry.delete(0, tk.END)
        self.senha_funcionario_entry.delete(0, tk.END)
        self.exibir_id_entry.delete(0, tk.END)
        self.id_funcionario_entry.delete(0, tk.END)
        self.text_area.delete(1.0, tk.END)

    def cancelar(self):
        confirmacao = messagebox.askyesno("Confirmação", "Você deseja mesmo cancelar a operação?")
        if confirmacao == True:
            messagebox.showinfo("Cancelar", "Ação cancelada")
            self.limpar_campos()
            self.listar_funcionarios()

    def inverter_data(self, data_digitada):
        data = data_digitada.split("/")
        data_banco = data[2]+"/"+data[1]+"/"+data[0]

        print(data_banco)

        return data_banco

if __name__ == "__main__":
    root = tk.Tk()
    app = tela_funcionario_admin(root)
    root.mainloop()


