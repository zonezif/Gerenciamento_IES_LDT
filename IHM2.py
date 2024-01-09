import tkinter as tk
from tkinter import ttk, filedialog
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from VisualIES import *
from PIL import Image, ImageTk
from Makeall import*
import json

class DictEditorInterface:
    def __init__(self, master, dicts):
        self.master = master
        self.notebook = ttk.Notebook(master)
        self.dicts = dicts
        self.ies_file_path = None
        self.figures_tab = None
        self.excel_file_path = None
        self.existing_figures = []
        self.excel_sheet_name_var = tk.StringVar()
        self.file_name_var = tk.StringVar()
        self.entry_widgets = {}  # Dicionário para mapear os widgets Entry
        self.create_widgets()
        self.inicial()

    def create_widgets(self):
 # Frame para o campo "Nome da Aba do Excel"
        excel_frame = ttk.Frame(self.master)
        excel_frame.pack(pady=10, padx=10, fill=tk.X)

        excel_sheet_label = tk.Label(excel_frame, text="Nome da Aba do Excel:", width=20, anchor=tk.W)
        excel_sheet_label.grid(row=0, column=0, padx=(0, 10))

        # Variável para armazenar a opção selecionada
        self.excel_sheet_name_var = tk.StringVar(self.master)
        self.excel_sheet_name_var.set('Selecione uma opção')  # Valor padrão

        # Opções iniciais para a lista suspensa
        self.options = ['Abra um arquivo execel']  # Você pode adicionar mais opções conforme necessário

        # Criar a lista suspensa
        self.excel_sheet_dropdown = ttk.OptionMenu(excel_frame, self.excel_sheet_name_var, *self.options)
        self.excel_sheet_dropdown.grid(row=0, column=1)
        self.excel_sheet_dropdown.config(width=30)  # Defina a largura conforme necessário



        # Campo para "Nome do Arquivo"
        file_name_label = tk.Label(excel_frame, text="Nome do Arquivo:", width=20, anchor=tk.W)
        file_name_label.grid(row=1, column=0, padx=(0, 10))

       
        file_name_entry = tk.Entry(excel_frame, textvariable=self.file_name_var)
        file_name_entry.grid(row=1, column=1)

        # Adicione o evento de bind para atualizar o dicionário original quando o nome do arquivo for modificado
        file_name_entry.bind("<KeyRelease>", self.update_file_name_in_dict)

        screen_width = self.master.winfo_screenwidth()
        for i, (dict_name, dict_values) in enumerate(self.dicts.items()):
            frame = ttk.Frame(self.notebook)
            self.notebook.add(frame, text=dict_name)

            canvas = tk.Canvas(frame, borderwidth=0, highlightthickness=0)
            scrollbar = ttk.Scrollbar(frame, orient="vertical", command=canvas.yview)
            inner_frame = ttk.Frame(canvas)

            canvas.create_window((0, 0), window=inner_frame, anchor="nw", tags="inner_frame")
            canvas.configure(yscrollcommand=scrollbar.set)

            self.create_dict_widgets(inner_frame, dict_name, dict_values, screen_width)

            canvas.grid(row=0, column=0, sticky="nsew")
            scrollbar.grid(row=0, column=1, sticky="ns")
            frame.columnconfigure(0, weight=1)
            frame.rowconfigure(0, weight=1)

            inner_frame.bind("<Configure>", lambda event, canvas=canvas: self.on_inner_frame_configure(canvas))

        self.notebook.pack(expand=True, fill='both')

        select_folder_button = tk.Button(self.master, text="Selecionar Pasta", command=self.select_folder)
        select_folder_button.pack(side=tk.LEFT, padx=10)

        select_excel_button = tk.Button(self.master, text="Selecionar Arquivo Excel", command=self.select_excel_file)
        select_excel_button.pack(side=tk.LEFT, padx=10)

        select_ies_button = tk.Button(self.master, text="Selecionar Arquivo IES", command=self.select_ies_file)
        select_ies_button.pack(side=tk.LEFT, padx=10)

        visualize_button = tk.Button(self.master, text="Visualizar Figuras", command=self.visualize_figures)
        visualize_button.pack(side=tk.LEFT, padx=10)

      
        save_button = tk.Button(self.master, text="Salvar", command=self.save)
        save_button.pack(pady=10)

        carregar = tk.Button(self.master, text="carregar", command=self.load)
        carregar.pack(pady=10)

        save_change = tk.Button(self.master, text="Salvar Alterações", command=self.save_ch)
        save_change.pack(pady=10)

 
    def update_file_name_in_dict(self, event):

        new_file_name = self.file_name_var.get()
        logs['NomeArq'] = new_file_name

    def create_dict_widgets(self, frame, dict_name, dict_values, screen_width):
        for row, (key, value) in enumerate(dict_values.items()):
            label_key = tk.Label(frame, text=key)
            label_key.grid(row=row, column=0, padx=5, pady=5, sticky='e', columnspan=2)

            entry = tk.Entry(frame, width=screen_width // 8)
            entry.insert(0, str(value))
            entry.grid(row=row, column=2, padx=5, pady=5, sticky='w', columnspan=2)

            # Adicionar a entrada ao dicionário entry_widgets
            self.entry_widgets[(dict_name, key)] = entry

            # Campo para "Nome do Arquivo"

            entry.bind("<KeyRelease>", lambda event, key=key, entry=entry, dict_name=dict_name: self.update_dict_final(dict_name, key, entry.get()))

            entry.bind("<MouseWheel>", self.on_mousewheel)

            frame.grid_columnconfigure(0, weight=1)
            frame.grid_columnconfigure(1, weight=1)
            frame.grid_columnconfigure(2, weight=1)
            frame.grid_columnconfigure(3, weight=1)

    def update_dict_final(self, dict_name, key, value):
        self.dicts[dict_name][key] = value

    def save_ch(self):
        file_path = filedialog.asksaveasfilename(defaultextension=".json", filetypes=[("Arquivos JSON", "*.json"), ("Todos os arquivos", "*.*")])
        with open(file_path, 'w') as file:
            json.dump({'dicts': self.dicts, 'logs': logs}, file)  # Alterado dicts para self.dicts

    def save(self):
        MakeAll(self.ies_file_path, self.excel_file_path, self.excel_sheet_name_var.get(), self.file_name_var.get(), self.dicts['AssIES'], self.dicts['AssLDT'])  # Alterado dicts para self.dicts

    def load(self):
        file_path = filedialog.askopenfile(defaultextension=".json", filetypes=[("Arquivos JSON", "*.json"), ("Todos os arquivos", "*.*")])
        if file_path:
            with open(file_path.name, 'r') as file:
                data = json.load(file)

            # Atualizar dicionários e logs
            self.dicts = data['dicts']
            self.logs = data['logs']
            self.file_name_var.set(self.logs['NomeArq'])
            # Atualizar a interface com os novos valores do dicionário
            self.update_interface_from_dicts()
            new_file_name = self.file_name_var.get()
            logs['NomeArq'] = new_file_name

    def update_interface_from_dicts(self):
        """Atualiza os campos da interface com os valores do dicionário."""
        for (dict_name, dict_values), frame in zip(self.dicts.items(), self.notebook.tabs()):
            for key, value in dict_values.items():
                entry = self.entry_widgets[(dict_name, key)]
                entry.delete(0, tk.END)  # Limpa o valor atual
                entry.insert(0, str(value))  # Insere o novo valor

    def inicial(self):
        file_path = './padrão.json'
        if file_path:
            with open(file_path, 'r') as file:
                data = json.load(file)

            # Atualizar dicionários e logs
            self.dicts = data['dicts']
            self.logs = data['logs']
            self.file_name_var.set(self.logs['NomeArq'])
            # Atualizar a interface com os novos valores do dicionário
            self.update_interface_from_dicts()
            new_file_name = self.file_name_var.get()
            logs['NomeArq'] = new_file_name

    def on_inner_frame_configure(self, canvas):
        canvas.configure(scrollregion=canvas.bbox("all"))

    def on_mousewheel(self, event):
        self.master.event_generate("<MouseWheel>", delta=event.delta, state=event.state)

    def select_folder(self):
        folder_path = filedialog.askdirectory()
        print("Pasta selecionada:", folder_path)

    def select_excel_file(self):
        self.excel_file_path = filedialog.askopenfilename(filetypes=[("Arquivos Excel", "*.xlsx;*.xls")])
        print("Arquivo Excel selecionado:", self.excel_file_path)
        # Aqui, atualizamos as opções da lista suspensa
        nova_lista = OpenExcinc(self.excel_file_path)
        self.excel_sheet_name_var.set('Selecione uma opção')  # Limpa a seleção atual, se houver.
        
        # Remove o dropdown atual
        self.excel_sheet_dropdown['menu'].delete(0, 'end')
        # Adiciona as novas opções ao dropdown
        for opcao in nova_lista:
            self.excel_sheet_dropdown['menu'].add_command(label=opcao, command=tk._setit(self.excel_sheet_name_var, opcao))
        
        # Atualiza a variável de opções com as novas opções
        self.options = nova_lista

    def select_ies_file(self):
        self.ies_file_path = filedialog.askopenfilename(filetypes=[("Arquivos IES", "*.ies")])
        print("Arquivo IES selecionado:", self.ies_file_path)

    def visualize_figures(self):
        if self.ies_file_path:
            if not self.existing_figures:
                Visual(self.ies_file_path, '90_270', 0)
                Visual(self.ies_file_path, '180_0', 1)

            self.show_figures()
    def show_figures(self):
        if self.figures_tab is None:
            self.figures_tab = ttk.Frame(self.notebook)
            self.notebook.add(self.figures_tab, text="Figuras")

        for widget in self.figures_tab.winfo_children():
            widget.destroy()

        example_files = ['./Distribuição_90_270.png', './Simetria_90_270.png', './Distribuição_180_0.png', './Simetria_180_0.png']

        for file_name in example_files:
            file_path = os.path.join(os.path.dirname(__file__), file_name)
            fig = self.load_image_as_figure(file_path)
            canvas = FigureCanvasTkAgg(fig, master=self.figures_tab)
            canvas.get_tk_widget().pack(side=tk.LEFT, fill=tk.BOTH)

    def load_image_as_figure(self, file_path):
        img = Image.open(file_path)
        img = img.resize((400, 400))
        img = img.convert("RGB")
        img_array = np.asarray(img)

        fig = Figure(figsize=(4, 4))
        ax = fig.add_subplot(111)

        # Remover borda do gráfico
        ax.axis('off')

        # Adicionar imagem sem interpolação
        ax.imshow(img_array, interpolation='none')

        return fig

if __name__ == "__main__":
    # Suas dicts originais
    dicts = {
        'AssIES' :{
            '[TEST]': 'CodZL',
            '[ISSUEDATE]': 'IES, ,DataIES, testedia 08',
            '[MANUFAC]': 'Zagonel',
            '[LUMCAT]': 'CodZL',
            '[LUMINAIRE]': 'DesSe',
            '[LAMPCAT]': 'Leds SMD - ,TempC, - IRC ,IRC',
            '[LAMP]': 'Leds SMD - ,TempC, - IRC ,IRC',
            '[_VOLTAGE]': '',
            '[_CURRENT]': '',
            '[_POWERFACTOR]': '',
            '[TESTLAB]': 'Zagonel',
            '[_TESTINST]': '',
            '[_TESTDIST]': '',
            '[_TESTTEMPERATURE]': '',
            '[_TESTHUMIDITY]': '',
            '[_TESTOPERATOR]': '',
            '[BALLAST]': '',
            '[BALLASTCAT]': '',
            '[TESTDATE]': 'DataIES',
            '[FLASHAREA]': 'Flash'
        },
        'AssLDT':{
            'Manufac':'Zagonel',
            'ltyp':'2',
            'lsym':'0',
            'mc': 'mc',
            'dc':'dc',
            'ng':'ng',
            'dg':'dg',
            'serNum':'CodZL', #editavel
            'lumNam':'DesSe',
            'lumNum':'CodZL',
            'arquvNam':'Nome do arquivo',
            'data':'DataAtulaLDT',
            'compr':'LenPr',
            'larg':'WidPr',
            'altur':'HeiPr',
            'comprLum':'LenEm',
            'lagurLum':'WidEm',
            'Cp1':'1',
            'Cp2':'1',
            'Cp3':'1',
            'Cp4':'1',
            'DFF':'100',
            'LORL':'100',
            'mult':'1',
            'tilt':'0',
            'numLampSTD':'1',
            'numLamp':'numLamp',
            'typelamp':'Leds SMD - ,TempC, - IRC ,IRC',
            'Lm':'Lm',
            'colorapp':'0',
            'colorrender':'',
            'potencia':'Poten'
        }
    }
    logs = {
        "execelaba":'',
        "execelArq":'',
        'NomeArq':'',
        'IesArq':''
    }

    root = tk.Tk()
    root.state('zoomed')  # Maximiza a janela
    app = DictEditorInterface(root, dicts)
    root.mainloop()