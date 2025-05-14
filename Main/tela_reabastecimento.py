import customtkinter as ctk

class tela_reabastecimento:

    def __init__(self,root):
        self.menu_root = root  
        self.root = ctk.CTkToplevel(root)
        self.root.configure(fg_color="#A0A0A0")
        #Define os parâmetros de interface da janela
        self.root.geometry("900x700")

        self.root.title("TBit Manager - Reabastecimento")
        self.root.resizable(width=False,height=False)
        

        self.root.transient(root)  # Faz com que a nova janela fique acima da principal
        self.root.grab_set()  # Bloqueia interações na principal até fechar essa


        voltar_menu_button = ctk.CTkButton(self.root, text='Voltar', text_color='black',fg_color='#404040',width=80,height= 30, command=self.voltar_menu)
        voltar_menu_button.place(x=790, y=640)

    def voltar_menu(self):
        
       # from menu_adm import menu_admin
        self.root.destroy()  # Fecha a janela atual
        self.menu_root.deiconify()
    
if __name__ == "__main__":
    root = ctk.CTk()
    app = tela_reabastecimento(root)
    root.mainloop()
