import tkinter as tk
from tkinter import *
class menu_admin:
    def __init__(self,root):
        self.root = root
        self.root.title("TBit Manager by TerraBytes - Menu Principal - Administrador") 
#        self.create_widget()
        self.root.geometry("900x700")
        self.root.resizable( width = False, height = False)

        tk.Button(text="Teste").place(x=100,y=34)
        pass

if __name__ == '__main__':
    root = tk.Tk()
    app = menu_admin(root)
    root.mainloop()