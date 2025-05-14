import customtkinter as ctk
from tkinter import messagebox
from database_geral import consultar_estoque_db, registrar_reabastecimento_db

class tela_reabastecimento:

    def __init__(self,root):
        self.menu_root = root  
        self.root = ctk.CTkToplevel(root)

        #Define os parâmetros de interface da janela
        self.root.geometry("900x700")

        self.root.title("TBit Manager - Reabastecimento")
        self.root.resizable(width=False,height=False)
        
        self.root.transient(root)  # Faz com que a nova janela fique acima da principal
        self.root.grab_set()  # Bloqueia interações na principal até fechar essa

        self.voltar_menu_button = ctk.CTkButton(self.root, text='Voltar', width=20, command=self.voltar_menu)
        self.voltar_menu_button.place(x=800, y=600)

        # ELEMENTOS NÃO POSICIONADOS, SOMENTE CRIADOS PARA DESENVOLVIMENTO DO BACK
        self.combobox_produtos = ctk.CTkComboBox(self.root, height=30, width=180, values=self.produtos_combobox())
        self.pesquisar_produto_entry = ctk.CTkEntry(self.root, height=30, width=150)
        self.quantidade_entrou_entry = ctk.CTkEntry(self.root, height=30, width=150)
        self.novo_reabastecimento_button = ctk.CTkButton(self.root, text="Novo Reabastecimento", command=self.chamado_reabastecer, height=30, width=120)

        self.combobox_produtos.place(x=150, y=100)
        self.quantidade_entrou_entry.place(x=350, y=100)
        self.novo_reabastecimento_button.place(x=550, y=100)

        # TEXT AREA PARA EXEMPLO
        self.text = ctk.CTkTextbox(self.root, width=300, height=300)
        self.text.place(x=300, y=300)
        
        self.consultar_estoque()

    def produtos_combobox(self):
        estoque = consultar_estoque_db()
        nomes_produtos = [nome[1] for nome in estoque]
        return nomes_produtos

    def get_id_produto(self):
        produto_selecionado = self.combobox_produtos.get()
        busca = consultar_estoque_db()

        for produto in busca:
            if produto_selecionado == produto[1]:
                id_produto = produto[0]
                return id_produto

    def chamado_reabastecer(self):
        quantidade = self.quantidade_entrou_entry.get()
        id_produto = self.get_id_produto()

        if id_produto and quantidade:
            try:
                registrar_reabastecimento_db(id_produto, quantidade)
                messagebox.showinfo("Sucesso", "Chamado cadastrado! Banco de dados atualizando...")

                self.consultar_estoque()
            except:
                messagebox.showerror("Error", "Ocorreu um erro na tentativa de cadastrar novo chamado!")

    def consultar_estoque(self):
        estoque = consultar_estoque_db()
        for produto in estoque:
            self.text.insert(ctk.END, f"Produto: {produto[1]}, ID Produto: {produto[0]}, Qnt: {produto[2]}\n\n")

    def voltar_menu(self):
        
       # from menu_adm import menu_admin
        self.root.destroy()  # Fecha a janela atual
        self.menu_root.deiconify()
    
if __name__ == "__main__":
    root = ctk.CTk()
    app = tela_reabastecimento(root)
    root.mainloop()
