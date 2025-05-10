import customtkinter as ctk
from tkinter import messagebox, LEFT, RIGHT
from database_geral import tbit_db
from menu_adm import menu_admin
from menu_user import menu_usuario
from database_geral import __init__

class login_menu:
    def __init__(self,root):
        tbit_db.__init__(self)
        
        self.root = root
        self.root.title("TBit Manager by TerraBytes") 
        self.create_widget()
        self.root.geometry("600x300")
        self.root.resizable( width = False, height = False)
        pass

    def create_widget(self):
        self.left_frame = ctk.CTkFrame(self.root, width=200, height=300, fg_color="Black") # Cria um frame à esquerda
        self.left_frame.pack(side=LEFT) # Posiciona o frame à esquerda

        self.right_frame = ctk.CTkFrame(self.root, width=400, height=300, fg_color="Black") # Cria um frame à esquerda
        self.right_frame.pack(side=RIGHT) # Posiciona o frame à esquerda


        self.usuario_label = ctk.CTkLabel(self.right_frame, text="Usuario:", font=("Times New Roman", 20), fg_color="Black", text_color='white') # Cria um label para o usuario
        self.usuario_label.place(x=10, y=105) # Posiciona o label o frame direito

        self.usuario_entry = ctk.CTkEntry(self.right_frame, width=140,height=30) # Cria um campo de entrada para o usuario
        self.usuario_entry.place(x=100, y=100) # Posiciona o campo de entrada

        self.senha_label = ctk.CTkLabel(self.right_frame, text="Senha:", font=("", 20), fg_color="Black", text_color="White") # Cria um label para a senha
        self.senha_label.place(x=10, y=160) # Posiciona o label no frame direito

        self.senha_entry = ctk.CTkEntry(self.right_frame, width=140,height=30, show="*") # Cria um campo de entrada para a senha
        self.senha_entry.place(x=100, y=160)       
        
        self.login_button = ctk.CTkButton(self.right_frame, text="LOGIN", width=15, command=self.login_user) # Cria um botao de login
        self.login_button.place(x=80, y=225)

    def login_user(self):
        

        usuario = self.usuario_entry.get()
        senha = self.senha_entry.get()

        
        try:
            database = tbit_db()
            cursor = database.cursor
            cursor.execute('SELECT nome_funcionario, usuario_funcionario, senha_funcionario, perfil_funcionario FROM funcionario WHERE usuario_funcionario = %s AND senha_funcionario = %s' ,(usuario, senha,))
        
            verify_login = cursor.fetchone()

            if verify_login:
                
                if (verify_login[3] == "Administrador"):
                    messagebox.showinfo(title="INFO LOGIN", message="Acesso ao ADM concedido. Bem Vindo!")

                    self.root.withdraw()
                    self.abrir_menu_admin()

                elif (verify_login[3] == "Usuario simples"):
                    messagebox.showinfo(title="INFO LOGIN", message="Acesso concedido. Bem Vindo!")

                    self.root.withdraw()
                    self.abrir_menu_user()
            else:
                messagebox.showinfo(title="INFO LOGIN", message="Acesso Negado. Verifique se está cadastrado no Sistema!")
                
        except Exception as e:
            messagebox.showerror(title="Erro", message=f"Ocorreu um erro: {str(e)}")
    
    def abrir_menu_admin(self):
        janela_admin = ctk.CTk()  
        app = menu_admin(janela_admin) 
        janela_admin.mainloop()

    def abrir_menu_user(self):
        janela_user = ctk.CTk()
        app = menu_usuario(janela_user)
        janela_user.mainloop()
        
    
if __name__ == '__main__':
    root = ctk.CTk()
    app = login_menu(root)
    root.mainloop()