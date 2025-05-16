import customtkinter as ctk
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.backends.backend_tkagg import NavigationToolbar2Tk
from database_geral import montante_pedidos, total_vendas, produtos_mais_vendidos,clientes_mais_pedidos, Categorias_mais_vendidas


plt.rcParams["axes.prop_cycle"] = plt.cycler(
color = ["#4C2A88","#BE96FF","#957DAD","#5E366E","#A98CCC"])

class tela_dashboard:

    def __init__(self,root):
        ctk.set_appearance_mode("dark")
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
        voltar_menu_button.place(x=1800, y=1000)

    def gerar_graficos(self):
       

        dados_vendas = produtos_mais_vendidos()  # Chama a função corretamente

        # Separando os dados para o gráfico
        nomes_produtos = [item["nome"] for item in dados_vendas]
        quantidades_vendas = [item["total_vendas"] for item in dados_vendas]

        # Criando o gráfico
        fig1, ax1 = plt.subplots()
        ax1.bar(nomes_produtos, quantidades_vendas)

        ax1.set_title("Produtos Vendidos")
        ax1.set_xlabel("Produtos")
        ax1.set_ylabel("Vendas")
        ax1.tick_params(axis='x', rotation=45)  # Melhorando a visualização dos rótulos no eixo X


        dados_Vendas_clientes = clientes_mais_pedidos()
        nomes_clientes = [item["nome_cliente"] for item in dados_Vendas_clientes]
        quantidades_pedidos = [item["total_vendas"] for item in dados_Vendas_clientes]

        fig2, ax2 = plt.subplots()
        ax2.barh(nomes_clientes,quantidades_pedidos)
        ax2.set_title("Vendas por marca")
        ax2.set_xlabel("Marca")
        ax2.set_ylabel("Vendas")

        dados_categorias_pedidos = Categorias_mais_vendidas()
        nome_categoria = [item["categoria_produto"] for item in dados_categorias_pedidos]
        pedidos_categoria = [item["pedidos_categoria"] for item in dados_categorias_pedidos]

        fig3, ax3 = plt.subplots(figsize=(10,10))
        ax3.pie(pedidos_categoria,labels = nome_categoria,autopct='%1.1f%%')
        ax3.set_title("Clientes compras")
        
        valor = montante_pedidos()

        fig4, ax4 = plt.subplots(figsize=(5,2))
        ax4.text(0.5, 0.5, f"R$ {valor}", fontsize=30, ha='center', va='center', color="#4C2A85")
        ax4.set_title("Valor total", fontsize=16)
        ax4.axis("off")

        fig5, ax5 = plt.subplots(figsize=(5,2))
        ax5.text(0.5, 0.5, f"{total_vendas()}", fontsize=30, ha='center', va='center', color="#4C2A85")
        ax5.set_title("Número de Vendas", fontsize=16)
        ax5.axis("off")
        


        self.exibir_grafico(fig1,1250,100)
        self.exibir_grafico(fig2,1250,500)
        self.exibir_grafico(fig3,-40,60)
        self.exibir_grafico(fig4, x=600, y=10)
        self.exibir_grafico(fig5, x=10, y=10)

    def exibir_grafico(self, fig, x, y):
        canvas = FigureCanvasTkAgg(fig, master=self.root)
        canvas.get_tk_widget().place(x=x, y=y)
        canvas.draw()

        # Adicionando a barra de ferramentas para zoom e pan
        toolbar = NavigationToolbar2Tk(canvas, self.root, pack_toolbar=False)
        toolbar.place(x=x, y=y + fig.get_size_inches()[1] * 100)  # Ajusta a posição da toolbar
        toolbar.update()



    def voltar_menu(self):
        
        # from menu_adm import menu_admin
        self.root.destroy()  # Fecha a janela atual
        self.menu_root.deiconify()

if __name__ == "__main__":
    root = ctk.CTk()
    app = tela_dashboard(root)
    root.mainloop()
