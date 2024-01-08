import tkinter as tk
from tkinter import ttk, filedialog
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from VisualIES import *
from PIL import Image, ImageTk

class DictEditorInterface:
    def __init__(self, master, dicts):
        self.master = master
        self.notebook = ttk.Notebook(master)
        self.dicts = dicts
        self.ies_file_path = None
        self.figures_tab = None
        self.existing_figures = []

        self.create_widgets()

    def create_widgets(self):
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

        save_button = tk.Button(self.master, text="Salvar Alterações", command=self.save_changes)
        save_button.pack(pady=10)

    def create_dict_widgets(self, frame, dict_name, dict_values, screen_width):
        for row, (key, value) in enumerate(dict_values.items()):
            label_key = tk.Label(frame, text=key)
            label_key.grid(row=row, column=0, padx=5, pady=5, sticky='e', columnspan=2)

            entry = tk.Entry(frame, width=screen_width // 8)
            entry.insert(0, str(value))
            entry.grid(row=row, column=2, padx=5, pady=5, sticky='w', columnspan=2)

            entry.bind("<KeyRelease>", lambda event, key=key, entry=entry, dict_name=dict_name: self.update_dict_final(dict_name, key, entry.get()))

            entry.bind("<MouseWheel>", self.on_mousewheel)

            frame.grid_columnconfigure(0, weight=1)
            frame.grid_columnconfigure(1, weight=1)
            frame.grid_columnconfigure(2, weight=1)
            frame.grid_columnconfigure(3, weight=1)

    def update_dict_final(self, dict_name, key, value):
        self.dicts[dict_name][key] = value

    def save_changes(self):
        for dict_name, dict_values in self.dicts.items():
            print(f"{dict_name}:", dict_values)

    def on_inner_frame_configure(self, canvas):
        canvas.configure(scrollregion=canvas.bbox("all"))

    def on_mousewheel(self, event):
        self.master.event_generate("<MouseWheel>", delta=event.delta, state=event.state)

    def select_folder(self):
        folder_path = filedialog.askdirectory()
        print("Pasta selecionada:", folder_path)

    def select_excel_file(self):
        excel_file_path = filedialog.askopenfilename(filetypes=[("Arquivos Excel", "*.xlsx;*.xls")])
        print("Arquivo Excel selecionado:", excel_file_path)

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
        "IES": {
        '[TEST]': 'CodZL',
        '[ISSUEDATE]': 'IES, ,DataIES, lucas rev 22',
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
        "AssLDT": {
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

    root = tk.Tk()
    root.state('zoomed')  # Maximiza a janela
    app = DictEditorInterface(root, dicts)
    root.mainloop()