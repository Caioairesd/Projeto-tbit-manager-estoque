import customtkinter as ctk
import tkinter as tk
from tkinter import ttk

# Inicialização
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

app = ctk.CTk()
app.geometry("600x400")

# Frame para a tabela
frame = ctk.CTkFrame(master=app)
frame.pack(pady=20, padx=20, fill="both", expand=True)

# Widget Treeview (tabela)
tree = ttk.Treeview(frame, columns=("Nome", "Idade", "Cidade"), show="headings")
tree.heading("Nome", text="Nome")
tree.heading("Idade", text="Idade")
tree.heading("Cidade", text="Cidade")

# Dados de exemplo
dados = [("Alice", 30, "São Paulo"), ("Bruno", 25, "Rio de Janeiro"), ("Carla", 28, "Belo Horizonte")]
for dado in dados:
    tree.insert("", tk.END, values=dado)

tree.pack(fill="both", expand=True)

app.mainloop()