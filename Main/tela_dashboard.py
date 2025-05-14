import customtkinter as ctk
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from database_dashboard import produtos_vendidos, clientes_mais_compras,Vendas_marca,total_vendas

plt.rcParams["axes.prop_cycle"] = plt.cycler(
color = ["#4C2A88","#BE96FF","#957DAD","#5E366E","#A98CCC"])

class tela_dashboard:

    def __init__(self,root):
        self.menu_root = root  
        self.root = ctk.CTkToplevel(root)

        largura = self.root.winfo_screenwidth()
        altura = self.root.winfo_screenheight()
        self.root.geometry(f"{largura}x{altura}+0+0")

        #Define os parâmetros de interface da janela
        #self.root.geometry("900x700")
        self.root.configure(fg_color="#FFFFFF")
        self.root.title("TBit Manager - Dashboard")
        self.root.resizable(width=False,height=False)
        

        self.root.transient(root)  # Faz com que a nova janela fique acima da principal
        self.root.grab_set()  # Bloqueia interações na principal até fechar essa
        

        self.gerar_graficos()# Chama a função que gera os gráficos
        self.criar_widgets()# Chama a função que cria os widgets

    def criar_widgets(self):

        voltar_menu_button = ctk.CTkButton(self.root, text='Voltar', width=20, command=self.voltar_menu)
        voltar_menu_button.place(x=1350, y=1000)

    def gerar_graficos(self):

        fig1, ax1 = plt.subplots()
        ax1.bar(produtos_vendidos.keys(),produtos_vendidos.values())
        ax1.set_title("Produtos vendidos")
        ax1.set_xlabel("Produtos")
        ax1.set_ylabel("Vendas")

        fig2, ax2 = plt.subplots()
        ax2.barh(Vendas_marca.keys(),Vendas_marca.values())
        ax2.set_title("Vendas por marca")
        ax2.set_xlabel("Marca")
        ax2.set_ylabel("Vendas")


        fig3, ax3 = plt.subplots()
        ax3.pie(clientes_mais_compras.values(),labels = clientes_mais_compras.keys(),autopct='%1.1f%%')
        ax3.set_title("Clientes compras")
        
        fig4, ax4 = plt.subplots(figsize=(5,2))
        ax4.text(0.5, 0.5, f"R$ {total_vendas:,.2f}", fontsize=30, ha='center', va='center', color="#4C2A85")
        ax4.set_title("Total de Vendas", fontsize=16)
        ax4.axis("off")

        self.exibir_grafico(fig1,1250,100)
        self.exibir_grafico(fig2,550,100)
        self.exibir_grafico(fig3,10,500)
        self.exibir_grafico(fig4, x=600, y=10)

    def exibir_grafico(self, fig, x, y):
        canvas = FigureCanvasTkAgg(fig, master=self.root)
        canvas.get_tk_widget().place(x=x, y=y)
        canvas.draw()




    def voltar_menu(self):
        
        # from menu_adm import menu_admin
        self.root.destroy()  # Fecha a janela atual
        self.menu_root.deiconify()

if __name__ == "__main__":
    root = ctk.CTk()
    app = tela_dashboard(root)
    root.mainloop()
