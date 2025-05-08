import customtkinter as ctk

class tela_cliente:

    
    def __init__(self,root):
        self.root = ctk.CTkToplevel(root)

        #Define os parâmetros de interface da janela
        self.root.geometry("900x700")

        self.root.title("TBit Manager - Cadastro de cliente")
        self.root.resizable(width=False,height=False)
        


        self.root.transient(root)  # Faz com que a nova janela fique acima da principal
        self.root.grab_set()  # Bloqueia interações na principal até fechar essa

        self.create_widget()

    def create_widget(self):

        voltar_menu_button = ctk.CTkButton(self.root, text='Voltar', width=20, command=self)
        voltar_menu_button.place(x=275, y=40)

    '''def voltar_menu(self):

        

        from menu_adm import menu_admin
        janela_admin = ctk.CTk()  
        app = menu_admin(janela_admin) 
        janela_admin.mainloop()

        self.root.destroy(tela_cliente)'''

       
        
        

if __name__ == "__main__":
    root = ctk.CTk()
    app = tela_cliente(root)
    root.mainloop()
