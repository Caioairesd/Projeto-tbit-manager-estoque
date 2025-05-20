import customtkinter as ctk
from tkinter import messagebox
from database_geral import tbit_db
from menu_adm import menu_admin
from menu_user import menu_usuario

class login_menu:
    def __init__(self,root):
        ctk.set_appearance_mode("dark")  # Deixar o frame no modo escuro-dark
        self.root = root
        self.root.title("TBit Manager by TerraBytes")
        largura = self.root.winfo_screenwidth()  # Expandir tela largura
        altura = self.root.winfo_screenheight()  # Expandir tela altura
        self.root.geometry(f"{largura}x{altura}+0+0")  # definir expanção

        
        self.root.configure(fg_color='#161B22')
        # Fundo geral da janela
        self.root.configure(bg="#0D1117")

        self.create_widget()

    def create_widget(self):

        # Frame principal
        self.right_frame = ctk.CTkFrame(self.root, width=400, height=300, fg_color="#2C3E50")
        self.right_frame.place(relx=0.5, rely=0.5, anchor="center")

        # Título
        self.titulo = ctk.CTkLabel(self.root, text="T B I T  M A N A G E R", font=("Garamond", 60),fg_color="#161B22", text_color="#58A6FF")
        self.titulo.place(relx=0.5, y=60, anchor="center")

        # Label Usuario
        self.usuario_label = ctk.CTkLabel(self.right_frame, text="Usuario:", font=("Times New Roman", 30), fg_color='#2C3E50', text_color="#C9D1D9")
        self.usuario_label.place(x=50, y=90)
        # Label Senha
        self.senha_label = ctk.CTkLabel(self.right_frame, text="Senha:",font=("Times New Roman", 30),fg_color='#2C3E50', text_color="#C9D1D9")
        self.senha_label.place(x=50, y=150)

        # Entry Usuario
        self.usuario_entry = ctk.CTkEntry(self.right_frame, text_color='#FFFFFF', width=160, height=35, fg_color='#1B263B', placeholder_text='Nome usuario...')
        self.usuario_entry.place(x=160, y=95)

        # Entry Senha
        self.senha_entry = ctk.CTkEntry(self.right_frame, text_color='#FFFFFF', width=160, height=35, fg_color='#1B263B', show="*", placeholder_text='Senha usuario...')
        self.senha_entry.place(x=160, y=150)


        # Botão Login
        self.login_button = ctk.CTkButton(self.right_frame, text="LOGIN", text_color='#FFFFFF', width=80, height=30,fg_color='#1B263B', hover_color="#2B3A55", command=self.login_user)
        self.login_button.place(x=160, y=200)

    def login_user(self):

        usuario = self.usuario_entry.get()
        senha = self.senha_entry.get()

        try:
            database = tbit_db()
            cursor = database.cursor
            cursor.execute('SELECT nome_funcionario, usuario_funcionario, senha_funcionario, perfil_funcionario FROM funcionario WHERE usuario_funcionario = %s AND senha_funcionario = %s', (usuario, senha,))

            verify_login = cursor.fetchone()

            if verify_login:
                if (verify_login[3] == "Administrador"):
                    messagebox.showinfo(title="INFO LOGIN", message=f"Acesso ao ADMINISTRADOR concedido. Bem Vindo {verify_login[0]}!")
                    self.root.withdraw()
                    self.abrir_menu_admin()

                elif (verify_login[3] == "Usuario simples"):
                    messagebox.showinfo(title="INFO LOGIN", message=f"Acesso concedido. Bem Vindo {verify_login[0]}!")
                    self.root.withdraw()
                    self.abrir_menu_user()
            else:
                messagebox.showinfo(title="INFO LOGIN", message="Acesso Negado. Verifique se está cadastrado no Sistema!")

        except Exception as e:
            messagebox.showerror(title="Erro", message=f"Ocorreu um erro: {str(e)}")

    def abrir_menu_admin(self):
        from menu_adm import menu_admin
        janela_admin = ctk.CTkToplevel(self.root)  # <- agora é Toplevel
        app = menu_admin(janela_admin)

    def abrir_menu_user(self):
        from menu_user import menu_usuario
        janela_user = ctk.CTkToplevel(self.root)  # <- agora é Toplevel
        app = menu_usuario(janela_user)

if __name__ == '__main__':
    root = ctk.CTk()
    app = login_menu(root)
    root.mainloop()