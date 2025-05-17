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
        self.root.configure(fg_color="#A0A0A0")

        #ctk.set_appearance_mode('dark')

        largura = self.root.winfo_screenwidth()# Expandir tela largura
        altura = self.root.winfo_screenheight()# Expandir tela altura
        self.root.geometry(f"{largura}x{altura}+0+0")# definir expanção

        #self.root.config(bg="#003366")
        self.create_widgets()
        

        self.listar_funcionarios()

    def create_widgets(self):
        #adciona um titulo 
        self.titulo = ctk.CTkLabel(self.root, text='F U N C I O N A R I O - A D M I N I S T R A D O R',font=("Garamond", 60), fg_color="#A0A0A0", text_color='black') # Cria um label para o usuario
        self.titulo.place(x=280, y=60) # Posiciona o label do titulo

        #cria o frame como fundo para deixar um fundo para as labls e caixas de textos
        self.right_frame = ctk.CTkFrame(self.root, width=800, height=800, fg_color="gray")# definir o tamanho e cor do fundo da frame
        self.right_frame.place(x=100, y=160)# definir a expanção da frame



        # Labels com o texto e sem fundo
        ctk.CTkLabel(self.right_frame, text="Nome :",font=("Times New Roman", 23),fg_color="gray", text_color='black').place(x=90, y=40)
        ctk.CTkLabel(self.right_frame, text="Data de Nascimento :",font=("Times New Roman", 23),fg_color="#808080", text_color='black',).place(x=90, y=90)
        ctk.CTkLabel(self.right_frame, text="Data de Admissão :",font=("Times New Roman", 23),fg_color="#808080", text_color='black').place(x=90, y=140)
        ctk.CTkLabel(self.right_frame, text="CPF :",font=("Times New Roman", 23),fg_color="#808080", text_color='black').place(x=90, y=190)
        ctk.CTkLabel(self.right_frame, text="Cidade :",font=("Times New Roman", 23),fg_color="#808080", text_color='black').place(x=90, y=240)
        ctk.CTkLabel(self.right_frame, text="Estado :",font=("Times New Roman", 23),fg_color="#808080", text_color='black').place(x=90, y=290)
        ctk.CTkLabel(self.right_frame, text="Telefone :",font=("Times New Roman", 23),fg_color="#808080", text_color='black').place(x=90, y=340)
        ctk.CTkLabel(self.right_frame, text="Email :",font=("Times New Roman", 23),fg_color="#808080", text_color='black').place(x=90, y=390)
        ctk.CTkLabel(self.right_frame, text="Usuario :",font=("Times New Roman", 23),fg_color="#808080", text_color='black').place(x=90, y=440)
        ctk.CTkLabel(self.right_frame, text="Senha :",font=("Times New Roman", 23),fg_color="#808080", text_color='black').place(x=90, y=490)
        

        # Caixas de textos
        self.nome_funcionario_entry  = ctk.CTkEntry(self.right_frame, text_color='black',fg_color="lightgray", border_color= 'gray',width=300,height=30)
        self.data_nascimento_funcionario_entry = ctk.CTkEntry(self.right_frame, text_color='black',fg_color="lightgray",border_color='gray', width=100,height=30)
        self.data_admissao_funcionario_entry = ctk.CTkEntry(self.right_frame, text_color='black',fg_color="lightgray",border_color='gray', width=100,height=30)
        self.cpf_funcionario_entry = ctk.CTkEntry(self.right_frame, text_color='black',fg_color="lightgray",border_color='gray', width=150,height=30)
        self.cidade_funcionario_entry = ctk.CTkEntry(self.right_frame, text_color='black',fg_color="lightgray",border_color='gray', width=150,height=30)
        self.uf_funcionario_entry = ctk.CTkEntry(self.right_frame, text_color='black',fg_color="lightgray",border_color='gray', width=150,height=30)
        self.telefone_funcionario_entry = ctk.CTkEntry(self.right_frame, text_color='black',fg_color="lightgray",border_color='gray', width=150,height=30)
        self.email_funcionario_entry = ctk.CTkEntry(self.right_frame, text_color='black',fg_color="lightgray",border_color='gray', width=280,height=30)
        self.usuario_funcionario_entry = ctk.CTkEntry(self.right_frame, text_color='black',fg_color="lightgray",border_color='gray',  width=120, height=30)
        self.senha_funcionario_entry = ctk.CTkEntry(self.right_frame, text_color='black',fg_color="lightgray",border_color='gray', show="*", width=120,height=30)

        self.buscar_funcionario_entry = ctk.CTkEntry(self.right_frame, text_color='black',fg_color="lightgray",border_color='gray', width=90,height=30)
       


        #Posicionamento das caixas de textos especialmente para nao dar conflito com o GET = PEGAR
        self.nome_funcionario_entry.place(x=170, y=40)#
        self.data_nascimento_funcionario_entry.place(x=300, y=90)#
        self.data_admissao_funcionario_entry.place(x=280, y=140)#
        self.cpf_funcionario_entry.place(x=190, y=190)#
        self.cidade_funcionario_entry.place(x=190, y=240)#
        self.uf_funcionario_entry.place(x=190, y=290)#
        self.telefone_funcionario_entry.place(x=190, y=340)#
        self.email_funcionario_entry.place(x=190, y=390)#
        self.usuario_funcionario_entry.place(x=190, y=440)#
        self.senha_funcionario_entry.place(x=190, y=490)#
        #Posicionamento das caixas de textos especialmente para nao dar conflito com o GET = PEGAR
        self.buscar_funcionario_entry.place(x=190, y=640)
        
        #Posicionamento das caixas de textos especialmente para nao dar conflito com o GET = PEGAR
        ctk.CTkLabel(self.right_frame, text="Busca por :\n(id)   ",text_color='black',font=('Times New Roman', 20), fg_color="gray").place(x=90, y=640)
        self.id_funcionario_entry = ctk.CTkEntry(self.right_frame, fg_color="white")


        # Botões de funções
        ctk.CTkButton(self.right_frame, text="CANCELAR",text_color='black' ,fg_color= '#404040', bg_color= '#808080', width=90, height= 40,command=self.cancelar).place(x=420, y=560)
        ctk.CTkButton(self.right_frame, text="REGISTRAR",text_color='black', fg_color= '#404040', bg_color= '#808080', width=90, height= 40,command=self.registrar_funcionario).place(x=90, y=560)
        ctk.CTkButton(self.right_frame, text="EXCLUIR",text_color='black', fg_color= '#404040', bg_color= '#808080', width=90, height= 40,command=self.delete_funcionario).place(x=200, y=560)
        ctk.CTkButton(self.right_frame, text="EDITAR",text_color='black', fg_color= '#404040', bg_color= '#808080', width=90, height= 40,command=self.update_funcionario).place(x=310, y=560)
        ctk.CTkButton(self.right_frame, text="BUSCAR",text_color='black', fg_color= '#404040', bg_color= '#808080', width=50, height= 30,command=self.pesquisar_funcionario).place(x=300, y=640)
        ctk.CTkButton(self.root, text='Voltar',text_color='black',fg_color= '#404040', bg_color= '#A0A0A0', width=90, height= 40, command=self.voltar_menu).place(x=1810, y=920)
       
        #Text Area para exibir a tabela em tempo real do Banco de Dados
        self.text_area = ctk.CTkTextbox(self.root,text_color='black', width=800,height=800, fg_color="gray")
        self.text_area.place(x=1000, y=160)



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
        self.text_area.delete(1.0, ctk.END)
        for funcionario in funcionarios:
            self.text_area.insert(ctk.END,f"id:{funcionario[0]}, Nome: {funcionario[1]}, Data de Nascimento: {funcionario[2]}, Data de Admissão: {funcionario[3]}, CPF: {funcionario[4]}, Cidade: {funcionario[5]}, UF: {funcionario[6]}, Telefone: {funcionario[7]}, Email: {funcionario[8]}, Usuario: {funcionario[9]}, Senha: {funcionario[10]}\n\n")
            self.text_area.place(x=1000, y=160)
            
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
                self.text_area.insert(ctk.END, f"ID:{id_solicitado[0]}, Nome: {id_solicitado[1]}, Data de Nascimento: {id_solicitado[2]}, Data de Admissão: {id_solicitado[3]}, CPF: {id_solicitado[4]}, Cidade: {id_solicitado[5]}, UF: {id_solicitado[6]}, Telefone: {id_solicitado[7]}, Email: {id_solicitado[8]}, Usuario: {id_solicitado[9]}, Senha: {id_solicitado[10]}\n")

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


