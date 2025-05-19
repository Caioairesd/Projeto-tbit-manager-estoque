import customtkinter as ctk
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk
from database_geral import montante_pedidos, total_vendas, produtos_mais_vendidos, clientes_mais_pedidos, Categorias_mais_vendidas, total_clientes, total_produtos, vendas_por_mes

# Define a paleta principal dos gráficos (destaques em azul)
plt.rcParams["axes.prop_cycle"] = plt.cycler(
    color=["#00BFFF", "#1E90FF", "#6495ED", "#4169E1", "#4682B4"]
)

class tela_dashboard:

    def __init__(self, root):
        ctk.set_appearance_mode("dark")  # Interface escura
        self.menu_root = root
        self.root = ctk.CTkToplevel(root)

        largura = self.root.winfo_screenwidth()
        altura = self.root.winfo_screenheight()
        self.root.geometry(f"{largura}x{altura}+0+0")

        # Configuração da janela principal
        self.root.configure(fg_color="#37363B")  # Fundo da janela (cinza escuro)
        self.root.title("TBit Manager - Dashboard")
        self.root.resizable(width=False, height=False)
        self.root.transient(root)
        self.root.grab_set()

        # Geração dos gráficos e botões
        self.gerar_graficos()
        self.criar_widgets()

    def criar_widgets(self):
        # Botão de voltar
        voltar_menu_button = ctk.CTkButton(self.root, text='Voltar', width=20, command=self.voltar_menu)
        voltar_menu_button.place(x=1800, y=1000)

    def gerar_graficos(self):
        # Gráfico 1 - Clientes com mais pedidos (barras horizontais)
        dados_Vendas_clientes = clientes_mais_pedidos()
        nomes_clientes = [item["nome_cliente"] for item in dados_Vendas_clientes]
        quantidades_pedidos = [item["total_vendas"] for item in dados_Vendas_clientes]

        fig2, ax2 = plt.subplots(figsize=(6, 4))
        fig2.patch.set_facecolor("#5E5D66")  # Fundo do gráfico
        ax2.barh(nomes_clientes, quantidades_pedidos, color="#00BFFF")  # Barras em azul
        ax2.set_title("Clientes com \nmais pedidos", color="#FFFFFF")
        ax2.set_xlabel("Vendas", color="#FFFFFF")
        ax2.set_ylabel("Clientes", color="#FFFFFF")
        ax2.tick_params(colors="#FFFFFF")
        ax2.grid(axis='x', linestyle='--', alpha=0.5)
        fig2.tight_layout(pad=0)

        # Gráfico 2 - Categorias mais vendidas (pizza)
        dados_categorias_pedidos = Categorias_mais_vendidas()
        nome_categoria = [item["categoria_produto"] for item in dados_categorias_pedidos]
        pedidos_categoria = [item["pedidos_categoria"] for item in dados_categorias_pedidos]
        cores_personalizadas = ["#00BFFF", "#1E90FF", "#6495ED", "#4169E1", "#4682B4", "#87CEFA", "#B0C4DE"]

        fig3, ax3 = plt.subplots(figsize=(8, 7))
        fig3.patch.set_facecolor("#5E5D66")
        ax3.pie(pedidos_categoria, labels=nome_categoria, colors=cores_personalizadas,
                autopct='%1.1f%%', textprops=dict(color="white"))
        ax3.set_title("Top 10\nCategorias", color="#FFFFFF")

        # Gráfico 3 - Receita total
        valor = montante_pedidos()
        fig4, ax4 = plt.subplots(figsize=(3, 1.5))
        fig4.patch.set_facecolor("#5E5D66")
        ax4.text(0.5, 0.5, f"R$ {valor:.2f}", fontsize=30, ha='center', va='center', color="#00BFFF")
        ax4.set_title("Receita\ntotal", fontsize=16, color="#FFFFFF")
        ax4.axis("off")
        fig4.tight_layout(pad=0)

        # Gráfico 4 - Total de vendas
        fig5, ax5 = plt.subplots(figsize=(2, 1.5))
        fig5.patch.set_facecolor("#5E5D66")
        ax5.text(0.5, 0.5, f"{total_vendas()}", fontsize=30, ha='center', va='center', color="#00BFFF")
        ax5.set_title("total de\nVendas", fontsize=16, color="#FFFFFF")
        ax5.axis("off")
        fig5.tight_layout(pad=0)

        # Gráfico 5 - Total de clientes
        fig6, ax6 = plt.subplots(figsize=(2, 1.5))
        fig6.patch.set_facecolor("#5E5D66")
        ax6.text(0.5, 0.5, f"{total_clientes()}", fontsize=30, ha='center', va='center', color="#00BFFF")
        ax6.set_title("total de\nclientes", fontsize=16, color="#FFFFFF")
        ax6.axis("off")
        fig6.tight_layout(pad=0)

        # Gráfico 6 - Total de produtos
        fig7, ax7 = plt.subplots(figsize=(2, 1.5))
        fig7.patch.set_facecolor("#5E5D66")
        ax7.text(0.5, 0.5, f"{total_produtos()}", fontsize=30, ha='center', va='center', color="#00BFFF")
        ax7.set_title("total de\nprodutos", fontsize=16, color="#FFFFFF")
        ax7.axis("off")
        fig7.tight_layout(pad=0)

        # Gráfico 7 - Evolução das vendas (linha)
        dados_pedidos = vendas_por_mes()
        meses = [item["mes"] for item in dados_pedidos]
        vendas = [item["pedidos"] for item in dados_pedidos]

        fig8, ax8 = plt.subplots(figsize=(6, 4))
        fig8.patch.set_facecolor("#5E5D66")
        ax8.plot(meses, vendas, marker='o', color="#00BFFF", linewidth=2)
        ax8.set_title("Evolução das Vendas", color="#FFFFFF")
        ax8.set_xlabel("Mês", color="#FFFFFF")
        ax8.set_ylabel("Quantidade de Vendas", color="#FFFFFF")
        ax8.tick_params(axis='x', rotation=45, colors="#FFFFFF")
        ax8.tick_params(axis='y', colors="#FFFFFF")
        ax8.grid(True, linestyle='--', alpha=0.5)
        fig8.tight_layout(pad=0)

        # Exibir os gráficos
        self.exibir_grafico(fig2, 1150, 20, exibir_toolbar=True)
        self.exibir_grafico(fig3, 50, 200, exibir_toolbar=False)
        self.exibir_grafico(fig4, 550, 20, exibir_toolbar=False)
        self.exibir_grafico(fig5, 50, 20, exibir_toolbar=False)
        self.exibir_grafico(fig6, 200, 20, exibir_toolbar=False)
        self.exibir_grafico(fig7, 350, 20, exibir_toolbar=False)
        self.exibir_grafico(fig8, 1150, 500, exibir_toolbar=True)

    def exibir_grafico(self, fig, x, y, exibir_toolbar):
        # Embute o gráfico na interface Tkinter
        canvas = FigureCanvasTkAgg(fig, master=self.root)
        canvas.get_tk_widget().place(x=x, y=y)
        canvas.draw()

        if exibir_toolbar:
            toolbar = NavigationToolbar2Tk(canvas, self.root, pack_toolbar=False)
            toolbar.place(x=x, y=y + fig.get_size_inches()[1] * 100)
            toolbar.update()

    def voltar_menu(self):
        self.root.destroy()
        self.menu_root.deiconify()

if __name__ == "__main__":
    root = ctk.CTk()
    app = tela_dashboard(root)
    root.mainloop()
