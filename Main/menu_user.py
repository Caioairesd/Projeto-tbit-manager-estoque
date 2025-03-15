
import tkinter as tk
from tkinter import *
class menu_usuario:
    def __init__(self,root):
        self.root = root
        self.root.title("TBit Manager by TerraBytes - Menu Principal - Usuario") 
#        self.create_widget()
        self.root.geometry("900x700")
        self.root.resizable( width = False, height = False)
        pass

if __name__ == '__main__':
    root = tk.Tk()
    app = menu_usuario(root)
    root.mainloop()

