import customtkinter as ctk

class tela_dashboard:

    def __init__(self,root):
        self.menu_root = root  
        self.root = ctk.CTkToplevel(root)

        #Define os parâmetros de interface da janela
        self.root.geometry("900x700")
        self.root.configure(fg_color='#A0A0A0')
        self.root.title("TBit Manager - Dashboard")

        ctk.set_appearance_mode("dark")# Deixar o frame no modo escuro-dark

        largura = self.root.winfo_screenwidth()# Expandir tela largura
        altura = self.root.winfo_screenheight()# Expandir tela altura
        self.root.geometry(f"{largura}x{altura}+0+0")# definir expanção

        


        self.root.grab_set()  # Bloqueia interações na principal até fechar essa
        
        voltar_menu_button = ctk.CTkButton(self.root, text='Voltar',text_color='black', width=90, height= 40,fg_color= '#404040', bg_color= 'gray', command=self.voltar_menu)
        voltar_menu_button.place(x=1700, y=900)

    def voltar_menu(self):
        
       # from menu_adm import menu_admin
        self.root.destroy()  # Fecha a janela atual
        self.menu_root.deiconify()

if __name__ == "__main__":
    root = ctk.CTk()
    app = tela_dashboard(root)
    root.mainloop()
