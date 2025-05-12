#import tkinter as tk
import customtkinter as ctk
from tkinter import messagebox
from database_geral import register_funcionario_db, delete_funcionario_db, update_funcionario_db, pesquisar_funcionario_db, listar_funcionarios_db

#from tkinter import *


class tela_funcionario_adm:
    def __init__(self, root):
        self.menu_root = root  
        self.root = ctk.CTkToplevel(root) 
        self.root.title("TBit Manager - Menu de funcionário")
        self.root.geometry("900x700")
        self.root.resizable(width=False, height=False)

        self.root.transient(root)  # Mantém a janela no topo
        self.root.grab_set()  # Bloqueia interações na principal até fechar essa

        #self.root.config(bg="#003366")
        self.create_widgets()

        self.listar_funcionarios()

    def create_widgets(self):
        # Labels com o texto e sem fundo
        ctk.CTkLabel(self.root, text="Nome:",fg_color="#00284d", text_color='white').place(x=30, y=20)
        ctk.CTkLabel(self.root, text="Data de Nascimento:",fg_color="#00284d", text_color='white').place(x=30, y=60)
        ctk.CTkLabel(self.root, text="Data de Admissão:",fg_color="#00284d", text_color='white').place(x=30, y=100)
        ctk.CTkLabel(self.root, text="CPF:",fg_color="#00284d", text_color='white').place(x=30, y=140)
        ctk.CTkLabel(self.root, text="Cidade:",fg_color="#00284d", text_color='white').place(x=30, y=180)
        ctk.CTkLabel(self.root, text="Estado:",fg_color="#00284d", text_color='white').place(x=30, y=220)
        ctk.CTkLabel(self.root, text="Telefone:",fg_color="#00284d", text_color='white').place(x=30, y=260)
        ctk.CTkLabel(self.root, text="Email:",fg_color="#00284d", text_color='white').place(x=30, y=300)
        ctk.CTkLabel(self.root, text="Usuario:",fg_color="#00284d", text_color='white').place(x=30, y=340)
        ctk.CTkLabel(self.root, text="Senha:",fg_color="#00284d", text_color='white').place(x=30, y=380)
        ctk.CTkLabel(self.root, text="Perfil:",fg_color="#00284d", text_color='white').place(x=30, y=420)

        # Caixas cinza escuro
        self.nome_funcionario_entry  = ctk.CTkEntry(self.root, fg_color="darkgray", width=100,height=25)
        self.data_nascimento_funcionario_entry = ctk.CTkEntry(self.root, fg_color="darkgray", width=100,height=25)
        self.data_admissao_funcionario_entry = ctk.CTkEntry(self.root, fg_color="darkgray", width=100,height=25)
        self.cpf_funcionario_entry = ctk.CTkEntry(self.root, fg_color="darkgray", width=100,height=25)
        self.cidade_funcionario_entry = ctk.CTkEntry(self.root, fg_color="darkgray", width=100,height=25)
        self.uf_funcionario_entry = ctk.CTkEntry(self.root, fg_color="darkgray", width=100,height=25)
        self.telefone_funcionario_entry = ctk.CTkEntry(self.root, fg_color="darkgray", width=100,height=25)
        self.email_funcionario_entry = ctk.CTkEntry(self.root, fg_color="darkgray", width=100,height=25)
        self.usuario_funcionario_entry = ctk.CTkEntry(self.root, fg_color="darkgray")
        self.senha_funcionario_entry = ctk.CTkEntry(self.root, fg_color="darkgray", show="*", width=100,height=25)
        
        self.perfil_funcionario_entry = ctk.CTkComboBox(self.root, fg_color="darkgray", values=["Usuario simples", "Administrador"], width=130, height=25)
        
        self.buscar_funcionario_entry = ctk.CTkEntry(self.root, fg_color="darkgray", width=25,height=100)
        self.exibir_id_entry = ctk.CTkEntry(self.root, fg_color="darkgray", width=70,height=100)

        # Caixas de texto
        self.nome_funcionario_entry.place(x=180, y=20)
        self.data_nascimento_funcionario_entry.place(x=180, y=60)
        self.data_admissao_funcionario_entry.place(x=180, y=100)
        self.cpf_funcionario_entry.place(x=180, y=140)
        self.cidade_funcionario_entry.place(x=180, y=180)
        self.uf_funcionario_entry.place(x=180, y=220)
        self.telefone_funcionario_entry.place(x=180, y=260)
        self.email_funcionario_entry.place(x=180, y=300)
        self.usuario_funcionario_entry.place(x=180, y=340)
        self.senha_funcionario_entry.place(x=180, y=380)
        self.perfil_funcionario_entry.place(x=180, y=420)
        self.buscar_funcionario_entry.place(x=660, y=453)
        

        ctk.CTkLabel(self.root, text="Busca por ID:", fg_color="lightgray").place(x=565, y=450)
        self.id_funcionario_entry = ctk.CTkEntry(self.root, fg_color="darkgray")

        # Botões de funções
        ctk.CTkButton(self.root, text="CANCELAR", command=self.cancelar).place(x=800, y=500)
        ctk.CTkButton(self.root, text="REGISTRAR", command=self.registrar_funcionario).place(x=30, y=450)
        ctk.CTkButton(self.root, text="EXCLUIR", command=self.delete_funcionario).place(x=120, y=450)
        ctk.CTkButton(self.root, text="ALTERAR", command=self.update_funcionario).place(x=195, y=450)
        ctk.CTkButton(self.root, text="BUSCAR", command=self.pesquisar_funcionario).place(x=740, y=500)
        ctk.CTkButton(self.root, text='Voltar', width=20, command=self.voltar_menu).place(x=800, y=600)
       
        #Text Area não funciona verificar
        self.text_area = ctk.CTkTextbox(self.root, height=200, width=550, fg_color="lightgray")
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
        perfil = self.perfil_funcionario_entry.get()
        
        data_nascimento_funcionario = self.inverter_data(data_nascimento_funcionario_invertida)
        data_admissao_funcionario = self.inverter_data(data_admissao_funcionario_invertida)

        if nome_funcionario and data_nascimento_funcionario and data_admissao_funcionario and CPF and Cidade and UF and Telefone and Email and Usuario and Senha:
            register_funcionario_db(nome_funcionario, data_nascimento_funcionario, data_admissao_funcionario, CPF, Cidade, UF, Telefone, Email, Usuario, Senha, perfil)
            self.limpar_campos()
            messagebox.showinfo("Success", "Funcionario criado com Sucesso")
        else:
            messagebox.showerror("Error", "Todos os campos são obrigatórios")

    def listar_funcionarios(self):
        funcionarios = listar_funcionarios_db()
        self.text_area.delete(1.0, ctk.END)
        for funcionario in funcionarios:
            self.text_area.insert(ctk.END, f"ID:{funcionario[0]}, Nome: {funcionario[1]}, Data de Nascimento: {funcionario[2]}, Data de Admissão: {funcionario[3]}, CPF: {funcionario[4]}, Cidade: {funcionario[5]}, UF: {funcionario[6]}, Telefone: {funcionario[7]}, Email: {funcionario[8]}, Usuario: {funcionario[9]}, Senha: {funcionario[11]}, Perfil: {funcionario[10]}\n\n")

    def pesquisar_funcionario(self):
        busca = self.buscar_funcionario_entry.get()
        self.buscar_funcionario_entry.delete(0, ctk.END)

        if busca:
            id_solicitado = pesquisar_funcionario_db(busca)

            if id_solicitado:
                messagebox.showinfo("Sucesso", f"Funcionário {id_solicitado[1]} encontrado com sucesso!")
                self.limpar_campos() # Limpa todos os campos antes de inserir novos dados
                self.text_area.delete(1.0, ctk.END)  # Limpa a área de texto antes de exibir os dados

                # Exibe as informações do funcionário na caixa de texto
                self.text_area.insert(ctk.END, f"ID:{id_solicitado[0]}, Nome: {id_solicitado[1]}, Data de Nascimento: {id_solicitado[2]}, Data de Admissão: {id_solicitado[3]}, CPF: {id_solicitado[4]}, Cidade: {id_solicitado[5]}, UF: {id_solicitado[6]}, Telefone: {id_solicitado[7]}, Email: {id_solicitado[8]}, Usuario: {id_solicitado[9]}, Senha: {id_solicitado[11]}, Perfil: {id_solicitado[10]}\n")

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
                self.perfil_funcionario_entry.set(id_solicitado[11])
     
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
        perfil = self.perfil_funcionario_entry.get()

        if id_funcionario and nome_funcionario and data_nascimento_funcionario and data_admissao_funcionario and CPF and Cidade and UF and Telefone and Email and Usuario and Senha:
            update_funcionario_db(nome_funcionario, data_nascimento_funcionario, data_admissao_funcionario, CPF, Cidade, UF, Telefone, Email, Usuario, Senha, perfil, id_funcionario)
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
                self.id_funcionario_entry.delete(0, ctk.END)
                self.listar_funcionarios()
                messagebox.showinfo("Sucesso", "Funcionário deletado com sucesso!")
            else:
                messagebox.showerror("Erro", "ID do funcionário é obrigatório!")

    def limpar_campos(self):
        self.nome_funcionario_entry.delete(0, ctk.END)
        self.data_nascimento_funcionario_entry.delete(0, ctk.END)
        self.data_admissao_funcionario_entry.delete(0, ctk.END)
        self.cpf_funcionario_entry.delete(0, ctk.END)
        self.cidade_funcionario_entry.delete(0, ctk.END)
        self.uf_funcionario_entry.delete(0, ctk.END)
        self.telefone_funcionario_entry.delete(0, ctk.END)
        self.email_funcionario_entry.delete(0, ctk.END)
        self.usuario_funcionario_entry.delete(0, ctk.END)
        self.senha_funcionario_entry.delete(0, ctk.END)
        self.exibir_id_entry.delete(0, ctk.END)
        self.id_funcionario_entry.delete(0, ctk.END)
        self.text_area.delete(1.0, ctk.END)

    def cancelar(self):
        self.menu_root = root  
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
    
    def voltar_menu(self):
        
       # from menu_adm import menu_admin
        self.root.destroy()  # Fecha a janela atual
        self.menu_root.deiconify()

if __name__ == "__main__":
    root = ctk.CTk()
    app = tela_funcionario_adm(root)
    root.mainloop()


