import customtkinter as ctk
from database_geral import registrar_cliente_db, update_cliente_db, delete_cliente_db, pesquisar_cliente_db
from tkinter import messagebox

class tela_cliente:

    
    def __init__(self,root):
        self.menu_root = root  
        self.root = ctk.CTkToplevel(root)

        #Define os parâmetros de interface da janela
        self.root.geometry("900x700")

        self.root.title("TBit Manager - Menu de cliente")
        self.root.resizable(width=False,height=False)

        self.root.transient(root)  # Faz com que a nova janela fique acima da principal
        self.root.grab_set()  # Bloqueia interações na principal até fechar essa

        self.create_widget()

    def create_widget(self):

        self.voltar_menu_button = ctk.CTkButton(self.root, text='Voltar', width=20, command=self.voltar_menu)
        self.voltar_menu_button.place(x=800, y=600)

        self.id_cliente_entry = ctk.CTkEntry(self.root, placeholder_text="Digite o ID para pesquisa...", width=250, height=30)
        self.id_cliente_entry.place(x=100, y=100)

        self.nome_cliente_entry = ctk.CTkEntry(self.root, placeholder_text="Nome para registro do cliente...", width=250, height=30)
        self.nome_cliente_entry.place(x=100, y=150)

        self.descricao_cliente_entry = ctk.CTkEntry(self.root, placeholder_text="Descrição para registro do cliente...", width=250, height=30)
        self.descricao_cliente_entry.place(x=100, y=200)

        self.cnpj_cliente_entry = ctk.CTkEntry(self.root, placeholder_text="00.000.000/0000-00", width=250, height=30)
        self.cnpj_cliente_entry.place(x=100, y=250)

        self.registrar_button = ctk.CTkButton(self.root, text="Registrar cliente", width=150, height=30, command=self.registrar_cliente)
        self.registrar_button.place(x=400, y=100)

        self.alterar_button = ctk.CTkButton(self.root, text="Alterar cliente", width=150, height=30, command=self.alterar_cliente)
        self.alterar_button.place(x=400, y=150)

        self.pesquisar_button = ctk.CTkButton(self.root, text="Pesquisar cliente", width=150, height=30)
        self.pesquisar_button.place(x=400, y=200)

    def registrar_cliente(self):
        nome_cliente = self.nome_cliente_entry.get()
        descricao_cliente = self.descricao_cliente_entry.get()
        cnpj_cliente = self.cnpj_cliente_entry.get()
        
        if nome_cliente and descricao_cliente and cnpj_cliente:
            try:
                registrar_cliente_db(nome_cliente, descricao_cliente, cnpj_cliente)
                messagebox.showinfo("Sucesso", "Cadastro do cliente foi efetuado com sucesso!")
            except:
                messagebox.showerror("Error", "Erro na tentativa de cadastrar um novo cliente!")
        else:
            messagebox.showinfo("Error", "Preencha todos os campos!")

    def alterar_cliente(self):
        id_cliente = self.id_cliente_entry.get()
        nome_cliente = self.nome_cliente_entry.get()
        descricao_cliente = self.descricao_cliente_entry.get()
        cnpj_cliente = self.cnpj_cliente_entry.get()

        if nome_cliente and descricao_cliente and cnpj_cliente:
            try:
                update_cliente_db(nome_cliente, descricao_cliente, cnpj_cliente, id_cliente)
                messagebox.showinfo("Sucesso", "Informações alteradas com sucesso!")
            except:
                messagebox.showerror("Error", "Erro na tentativa de alterar informações!")
        else:
            messagebox.showerror("Erro", "Preencha todos os campos!")

    def voltar_menu(self):
       # from menu_adm import menu_admin
        self.root.destroy()  # Fecha a janela atual
        self.menu_root.deiconify()
    
if __name__ == "__main__":
    root = ctk.CTk()
    app = tela_cliente(root)
    root.mainloop()
