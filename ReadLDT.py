import chardet


def abrir(name):
    print(name)

    with open(name, 'rb') as f:
        rawdata = f.read(10240)
        encoding = chardet.detect(rawdata)['encoding']

    print(f"Encoding encontrado: {encoding}")

    with open(name, "r", encoding=encoding) as f:
        reader = f.read()

    x = reader
    x = x.splitlines()

    return x


class LDT(object):

    def __init__(self, arq):

        data = abrir(arq)

        self.info = data

        self.Fabricante = data[0]

        self.tipo = data[1]  # Indicador de tipo Tipo

        self.lsym = data[2]  # Indicador de simetria Isym

        # Número Mc de planos C para 0 ... 360°(usual 24 para luminárias interiores,36 para luminárias de rua)
        self.McC = data[3]

        # Distância Dc entre planos C , (Dc = 0 para não equidistante níveis C existentes)
        self.DcC = data[4]

        # Número de Ng das intensidades luminosas em cada nível C (geralmente 19, 37 ou 73)
        self.Ng = data[5]

        # Distância Dg entre as intensidades luminosas (Dg = 0 para intensidades luminosas não sendo da mesma distância nos níveis C
        self.Dg = data[6]

        self.NCert = data[7]  # Número do certificado de teste

        self.Nome = data[8]  # Nome da luminária

        self.Numero = data[9]  # Número da luminária

        self.NomeArq = data[10]  # Nome do arquivo

        self.Data = data[11]  # Data/pessoa responsável

        self.length = data[12]  # Comprimento/diâmetro da luminária

        # Largura b da luminária (b – 0 para luminárias circulares)
        self.width = data[13]

        self.height = data[14]  # Altura da luminária

        # Dimenções da area luminosa

        self.Llength = data[15]  # Comprimento/diâmetro da área luminosa

        self.Lwidth = data[16]  # Largura b1 da área luminosa

        self.LheightC0 = data[17]  # Altura da área luminosa C0

        self.LheightC90 = data[18]  # Altura da área luminosa C90

        self.LheightC180 = data[19]  # Altura da área luminosa C180

        self.LheightC270 = data[20]  # Altura da área luminosa C270

        self.Rzphi = data[21]  # Razão do fluxo descendente phi

        self.REtB = data[22]  # Razão de saída de luz da luminária EtaLB

        self.FatC = data[23]  # Fator de conversação para intensidade luminosa

        # Inclinação da luminária durante a medição (importante para luminárias de rua)
        self.FatI = data[24]

        self.Nequip = data[25]  # Número de equipamentos (opcional)

        self.Nlamp = data[26]  # Número de lâmpadas

        self.LampTip = data[27]  # Número de lâmpadas

        self.Fluxo = data[28]  # Fluxo luminoso total das lâmpadas

        self.TempColor = data[29]  # Temperatura de cor da lâmpada

        self.InColor = data[30]  # Índice de renderização de cores

        self.Potencia = data[31]  # potencia total do sistema

        self.RazFlux = data[32]  # Razão fluxo luminoso total

        # não pertinentes adicionar posteriormente

    def Tipo(self):

        if(self.tipo == "1"):
            return "simetricamente rotativa"
        if(self.tipo == "2"):
            return "linear"
        if(self.tipo == "3"):
            return "simétrica de rotação não pontual"

    def Lsym(self):
        if(self.lsym == "0"):
            return "sem simetria"

        if(self.lsym == "1"):
            return "simetria"

        if(self.lsym == "2"):
            return "plano de simetria C0-C180"

        if(self.lsym == "3"):
            return "plano de simetria C90-C270"

        if(self.lsym == "4"):
            return "plano de simetria C0-C180 e plano C90-C270"
