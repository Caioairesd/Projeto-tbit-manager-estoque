import customtkinter as ctk
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk
from database_geral import montante_pedidos, total_vendas, clientes_mais_pedidos, Categorias_mais_vendidas, total_clientes, total_produtos, vendas_por_mes
plt.rcParams["axes.prop_cycle"] = plt.cycler(
    color=["#0073E6", "#1E90FF", "#6495ED", "#4169E1", "#4682B4"]
)

class tela_dashboard:

    def __init__(self, root):
        ctk.set_appearance_mode("dark")
        self.menu_root = root
        self.root = ctk.CTkToplevel(root)

        largura = self.root.winfo_screenwidth()
        altura = self.root.winfo_screenheight()
        self.root.geometry(f"{largura}x{altura}+0+0")

        self.root.configure(fg_color="#1F2937")
        self.root.title("TBit Manager - Dashboard")
        self.root.resizable(width=False, height=False)
        self.root.transient(root)
        self.root.grab_set()

        self.gerar_graficos()
        self.criar_widgets()

    def criar_widgets(self):
        # Botão responsável por voltar ao menu 0073E6
        voltar_menu_button = ctk.CTkButton(self.root, text='VOLTAR', width=90, height=40,fg_color='#0073E6', command=self.voltar_menu)
        voltar_menu_button.place(x=1770, y=1000)
        
        ''' # Botão responsável por atualizar o dashboard
        update_button = ctk.CTkButton(self.root, text='ATUALIZAR ', width=90, height=40,fg_color='#0073E6', command=self.voltar_menu)
        update_button.place(x=1600, y=1000)
        '''
    def gerar_graficos(self):
        dados_Vendas_clientes = clientes_mais_pedidos()
        nomes_clientes = [item["nome_cliente"] for item in dados_Vendas_clientes]
        quantidades_pedidos = [item["total_vendas"] for item in dados_Vendas_clientes]

        fig2, ax2 = plt.subplots(figsize=(7, 4))
        fig2.patch.set_facecolor("#2C3E50")
        ax2.barh(nomes_clientes, quantidades_pedidos, color="#0073E6")
        ax2.set_title("Destaques em Pedidos",fontsize=15,ha='center', va='center', color="#FFFFFF")
        ax2.set_xlabel("Pedidos", color="#FFFFFF",fontsize=15)
        ax2.set_ylabel("Clientes", color="#FFFFFF",fontsize=15)
        ax2.tick_params(colors="#FFFFFF")
        ax2.grid(axis='x', linestyle='--', alpha=0.5)
        fig2.tight_layout(pad=0)

        dados_categorias_pedidos = Categorias_mais_vendidas()
        nome_categoria = [item["categoria_produto"] for item in dados_categorias_pedidos]
        pedidos_categoria = [item["pedidos_categoria"] for item in dados_categorias_pedidos]
        cores_adicionais = ["#001F3F", "#003366", "#004080", "#0059B3", "#0073E6", "#1E90FF", "#3399FF", "#66B2FF", "#99CCFF", "#CCE5FF"]




        fig3, ax3 = plt.subplots(figsize=(10.5, 7))
        fig3.patch.set_facecolor("#2C3E50")
        ax3.pie(pedidos_categoria, labels=nome_categoria, colors=cores_adicionais,
                autopct='%1.1f%%', textprops=dict(color="white"))
        ax3.set_title("Categorias Mais Vendidas",fontsize=25, color="#FFFFFF")

        fig4, ax4 = plt.subplots(figsize=(3, 1.5))
        fig4.patch.set_facecolor("#2C3E50")
        ax4.text(0.5, 0.5, f"R$ {montante_pedidos():.2f}", fontsize=30, ha='center', va='center', color="#FFFFFF")
        ax4.set_title("Receita\nTotal", fontsize=16, color="#FFFFFF")
        ax4.axis("off")
        fig4.tight_layout(pad=0)

        fig5, ax5 = plt.subplots(figsize=(2, 1.5))
        fig5.patch.set_facecolor("#2C3E50")
        ax5.text(0.5, 0.5, f"{total_vendas()}", fontsize=30, ha='center', va='center', color="#FFFFFF")
        ax5.set_title("Total de\nPedidos", fontsize=16, color="#FFFFFF")
        ax5.axis("off")
        fig5.tight_layout(pad=0)

        fig6, ax6 = plt.subplots(figsize=(2, 1.5))
        fig6.patch.set_facecolor("#2C3E50")
        ax6.text(0.5, 0.5, f"{total_clientes()}", fontsize=30, ha='center', va='center', color="#FFFFFF")
        ax6.set_title("Total de\nClientes", fontsize=16, color="#FFFFFF")
        ax6.axis("off")
        fig6.tight_layout(pad=0)

        fig7, ax7 = plt.subplots(figsize=(2, 1.5))
        fig7.patch.set_facecolor("#2C3E50")
        ax7.text(0.5, 0.5, f"{total_produtos()}", fontsize=30, ha='center', va='center', color="#FFFFFF")
        ax7.set_title("Total de\nProdutos", fontsize=16, color="#FFFFFF")
        ax7.axis("off")
        fig7.tight_layout(pad=0)

        dados_pedidos = vendas_por_mes()
        meses = [item["mes"] for item in dados_pedidos]
        vendas = [item["pedidos"] for item in dados_pedidos]

        fig8, ax8 = plt.subplots(figsize=(7, 4))
        fig8.patch.set_facecolor("#2C3E50")
        ax8.plot(meses, vendas, marker='o', color="#0073E6", linewidth=2)
        ax8.set_title("Evolução das Vendas", color="#FFFFFF",fontsize=15)
        ax8.set_xlabel("Meses", color="#FFFFFF",fontsize=15)
        ax8.set_ylabel("Quantidade de Vendas", color="#FFFFFF",fontsize=15)
        ax8.tick_params(axis='x', rotation=45, colors="#FFFFFF")
        ax8.tick_params(axis='y', colors="#FFFFFF")
        ax8.grid(True, linestyle='--', alpha=0.5)
        fig8.tight_layout(pad=0)

        # Mostra os gráficos com frames arredondados
        self.exibir_grafico(fig2, 1150, 20, exibir_toolbar=True)
        self.exibir_grafico(fig3, 50, 250, exibir_toolbar=False)
        self.exibir_grafico(fig4, 800, 20, exibir_toolbar=False)
        self.exibir_grafico(fig5, 50, 20, exibir_toolbar=False)
        self.exibir_grafico(fig6, 300, 20, exibir_toolbar=False)
        self.exibir_grafico(fig7, 550, 20, exibir_toolbar=False)
        self.exibir_grafico(fig8, 1150, 515, exibir_toolbar=True)

    def exibir_grafico(self, fig, x, y, exibir_toolbar):
        width = fig.get_size_inches()[0] * 100
        height = fig.get_size_inches()[1] * 100
        frame_height = height + 60 if exibir_toolbar else height + 20

        # Definimos o tamanho no construtor
        frame = ctk.CTkFrame(
            master=self.root,
            fg_color="#2C3E50",
            corner_radius=20,
            width=width + 20,
            height=frame_height
        )
        frame.place(x=x - 10, y=y - 10)  # Aqui só posição

        canvas = FigureCanvasTkAgg(fig, master=frame)
        canvas.get_tk_widget().place(x=10, y=10)
        canvas.draw()

        if exibir_toolbar:
            toolbar = NavigationToolbar2Tk(canvas, frame, pack_toolbar=False)
            toolbar.place(x=10, y=height + 15)
            toolbar.update()

    def voltar_menu(self):
        self.root.destroy()
        self.menu_root.deiconify()

if __name__ == "__main__":
    root = ctk.CTk()
    app = tela_dashboard(root)
    root.mainloop()