import customtkinter as ctk

class tela_pedido:

    def __init__(self,root):
        self.root = ctk.CTkToplevel(root)

        #Define os parâmetros de interface da janela
        self.root.geometry("900x700")

        self.root.title("TBit Manager - Menu Fornecedor")
        self.root.resizable(width=False,height=False)
        

        self.root.transient(root)  # Faz com que a nova janela fique acima da principal
        self.root.grab_set()  # Bloqueia interações na principal até fechar essa

if __name__ == "__main__":
    root = ctk.CTk()
    app = tela_pedido(root)
    root.mainloop()
