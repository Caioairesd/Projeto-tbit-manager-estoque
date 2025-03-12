import tkinter as tk
from tkinter import *
from database import tbit_db

class main_menu:
    def __init__(self,root):
        self.root = root
        self.root.title("TBit Manager by TerraBytes") 
        self.create_widgets()
        self.root.geometry("900x700")
        self.root.resizable( width = False, height = False)
        self.root.geometry("900x700")
        pass

    def create_widgets(self):
        LeftFrame = Frame(root, width=200, height=300, bg="MIDNIGHTBLUE", relief="raise") # Cria um frame à esquerda
        LeftFrame.pack(side=LEFT) # Posiciona o frame à esquerda

        RightFrame = Frame(root, width=395, height=300, bg="MIDNIGHTBLUE", relief="raise") # Cria um frame à esquerda
        RightFrame.pack(side=RIGHT) # Posiciona o frame à esquerda

        # ADICIONAR LOGO
        LogoLabel = Label(LeftFrame, bg="MIDNIGHTBLUE") # Cria uma label que carrega a logo
        LogoLabel.place(x=50, y=100) # Posiciona o label no frame esquerdo

        UsuarioLabel = Label(RightFrame, text="Usuario:", font=("Century Gothic", 20), bg="MIDNIGHTBLUE", fg="White") # Cria um label para o usuario
        UsuarioLabel.place(x=5, y=100) # Posiciona o label o frame direito

        UsuarioEntry = tk.Entry(RightFrame, width=30) # Cria um campo de entrada para o usuario
        UsuarioEntry.place(x=120, y=115) # Posiciona o campo de entrada

        SenhaLabel = Label(RightFrame, text="Senha:", font=("Century Gothic", 20), bg="MIDNIGHTBLUE", fg="White") # Cria um label para a senha
        SenhaLabel.place(x=5, y=150) # Posiciona o label no frame direito

        SenhaEntry = tk.Entry(RightFrame, width=30, show="*") # Cria um campo de entrada para a senha
        SenhaEntry.place(x=120, y=165)        



    
if __name__ == '__main__':
    root = tk.Tk()
    app = main_menu(root)
    root.mainloop()