import customtkinter as ctk
from database_geral import registrar_cliente_db, update_cliente_db, delete_cliente_db, get_clientes_db, pesquisar_cliente_db
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

        self.deletar_button = ctk.CTkButton(self.root, text="Deletar cliente", width=150, height=30, command=self.deletar_cliente)
        self.deletar_button.place(x=400, y=200)

        self.pesquisar_button = ctk.CTkButton(self.root, text="Pesquisar cliente", width=150, height=30, command=self.pesquisar_cliente)
        self.pesquisar_button.place(x=400, y=250)

        self.listar_button = ctk.CTkButton(self.root, text="Listar clientes", width=150, height=30, command=self.listar_clientes)
        self.listar_button.place(x=400, y=300)

    def registrar_cliente(self):
        nome_cliente = self.nome_cliente_entry.get()
        descricao_cliente = self.descricao_cliente_entry.get()
        cnpj_cliente = self.cnpj_cliente_entry.get()
        
        if nome_cliente and descricao_cliente and cnpj_cliente:
            try:
                registrar_cliente_db(nome_cliente, descricao_cliente, cnpj_cliente)
                messagebox.showinfo("Sucesso", "Cadastro do cliente foi efetuado com sucesso!")
                self.limpar_campos()
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
                self.limpar_campos()
            except:
                messagebox.showerror("Error", "Erro na tentativa de alterar informações!")
        else:
            messagebox.showerror("Erro", "Preencha todos os campos!")
    
    def deletar_cliente(self):
        id_cliente = self.id_cliente_entry.get()
        if id_cliente:
            confirmacao = messagebox.askyesno("","Você realmente deseja deletar esse formecedor?")
            if confirmacao  == True:
                delete_cliente_db(id_cliente)
                self.id_cliente_entry.delete(0,ctk.END)
                messagebox.showinfo("Sucesso","Fornecedor deletado com sucesso!")
        else:
            messagebox.showerror("Erro","ID do fornecedor é obrigatório!")

    def pesquisar_cliente(self):
        id_cliente = self.id_cliente_entry.get()
        if id_cliente:
            busca = pesquisar_cliente_db(id_cliente)

            if busca:
                messagebox.showinfo("Sucesso", f"Cliente '{busca[1]} encontrado!'")
                return f"ID: {busca[0]}, Nome: {busca[1]}, Descrição: {busca[2]}, CNPJ: {busca[3]}"

    def listar_clientes(self):
        clientes = get_clientes_db()

        for cliente in clientes:
            return f"ID: {cliente[0]}, Nome: {cliente[1]}, Descrição: {cliente[2]}, CNPJ: {cliente[3]}"

    def limpar_campos(self):
        self.id_cliente_entry.delete(0, ctk.END)
        self.nome_cliente_entry.delete(0, ctk.END)
        self.cnpj_cliente_entry.delete(0, ctk.END)
        self.descricao_cliente_entry.delete(0, ctk.END)

    def voltar_menu(self):
       # from menu_adm import menu_admin
        self.root.destroy()  # Fecha a janela atual
        self.menu_root.deiconify()
    
if __name__ == "__main__":
    root = ctk.CTk()
    app = tela_cliente(root)
    root.mainloop()
