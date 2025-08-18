import unittest
import tkinter as tk
from customtkinter import CTkButton, CTk

class App(CTk):
    def __init__(self):
        super().__init__()
        self.clicked = False
        self.button = CTkButton(self, text="Clique", command=self.on_click)
        self.button.pack()

    def on_click(self):
        self.clicked = True

class TestApp(unittest.TestCase):
    def test_button_click(self):
        app = App()
        
        # Simula o clique chamando invoke() que dispara o command do botão
        app.button.invoke()
        
        self.assertTrue(app.clicked)
        
        app.destroy()  # Fecha a janela após o teste

if __name__ == '__main__':
    unittest.main()