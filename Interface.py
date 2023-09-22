import tkinter as tk
from tkinter import ttk
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from ReadIES import *

ies = IES("./teste.IES")

Dados = {
    'Fabricante': ies.dic['[MANUFAC]'],
    'Luminaria_Cod': ies.dic['[TEST]'],
    'Data': ies.dic['[TESTDATE]'],
    'Luminaria': ies.dic['[LUMINAIRE]'],
    'Lampada': ies.dic['[LAMP]'],
    'Lampada_Descr': ies.dic['[LAMPCAT]'],
    'Teste_Lab': ies.dic['[TESTLAB]'],
    'Flash_Area': ies.dic['[FLASHAREA]'],
    'Lampada_Num': ies.Nlamp(),
    'Fluxo_P_Lamp': ies.Lm(),
    'CD_Multiplicador': ies.Fat(),
    'Num_Ang_verticais': ies.Nang(),
    'Num_Ang_Horizontais': ies.Nah(),
    'Ensaio_Tipo': [],
    'Unidade_Medida': [],
    'Largura': [],
    'Comprimento': [],
    'Altura': [],
    'Potencia': [],
    'Angulos_Verticas': ies.AngV(),
    'Angulos_horizontais': ies.AngH(),
    'Candela_Valores': ies.Cd(),
    'Img_ref': []
}

# Função para atualizar o gráfico e a tabela


def update_data():
    # Atualize os dados com base nas entradas do usuário
    Dados['Fabricante'] = fabricante_entry.get()
    Dados['Luminaria_Cod'] = luminaria_cod_entry.get()
    # Atualize outras entradas conforme necessário...

    # Atualize a tabela
    update_table()


# Função para atualizar a tabela


def update_table():
    # Limpe a tabela existente
    for row in table.get_children():
        table.delete(row)

    # Insira os dados na tabela
    for key, value in Dados.items():
        table.insert("", "end", values=(key, value))

# Função para plotar os dados


# Crie a janela principal
root = tk.Tk()
root.title('Interface para Dados, Tabela e Gráfico')

# Crie uma moldura para a tabela
table_frame = ttk.Frame(root)
table_frame.pack(side=tk.TOP, padx=10, pady=10)

# Crie a tabela
table = ttk.Treeview(table_frame, columns=('Campo', 'Valor'), show='headings')
table.heading('Campo', text='Campo')
table.heading('Valor', text='Valor')
table.pack()

# Crie campos de entrada para os dados
fabricante_label = ttk.Label(root, text='Fabricante:')
fabricante_label.pack(anchor=tk.W)
fabricante_entry = ttk.Entry(root)
fabricante_entry.pack(anchor=tk.W)

luminaria_cod_label = ttk.Label(root, text='Luminaria Cod:')
luminaria_cod_label.pack(anchor=tk.W)
luminaria_cod_entry = ttk.Entry(root)
luminaria_cod_entry.pack(anchor=tk.W)

# Crie um botão para atualizar os dados, a tabela e o gráfico
update_button = ttk.Button(root, text='Atualizar', command=update_data)
update_button.pack()

# Crie uma moldura para o gráfico
plot_frame = ttk.Frame(root)
plot_frame.pack(side=tk.TOP, padx=10, pady=10)


# Inicie o loop da interface gráfica
root.mainloop()
