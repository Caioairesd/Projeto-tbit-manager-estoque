import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.title("Treeview com Estilo")
root.geometry("400x250")

# Criando o estilo
style = ttk.Style(root)

# Escolher tema base (opcional: 'default', 'clam', 'alt', etc.)
style.theme_use("clam")

# Estilo geral do Treeview
style.configure("Treeview",
    background="white",
    foreground="black",
    rowheight=30,
    fieldbackground="white",
    font=('Arial', 12)
)

# Estilo da linha selecionada
style.map("Treeview",
    background=[("selected", "lightblue")],
    foreground=[("selected", "black")]
)

# Criando Treeview
tree = ttk.Treeview(root, columns=("Nome", "Idade"), show="headings")
tree.heading("Nome", text="Nome")
tree.heading("Idade", text="Idade")

tree.insert("", "end", values=("Ana", 25))
tree.insert("", "end", values=("João", 30))
tree.insert("", "end", values=("Maria", 22))

tree.pack(expand=True, fill="both", padx=10, pady=10)

root.mainloop()