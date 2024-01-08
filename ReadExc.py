import pandas as pd


def OpenExc(LumCodigo, caminho_arquivo, nome_aba):

    if (nome_aba in pd.ExcelFile(caminho_arquivo).sheet_names) == False:
        return False, "a aba " + nome_aba + " não encontrada"

    # Use a função `read_excel` do pandas para ler a aba específica
    dados = pd.read_excel(caminho_arquivo, sheet_name=nome_aba,
                          skiprows=1)  # pula a primeira Linha

    # Obtenha a lista de nomes de colunas
    colunas = list(dados.columns)

    # Exiba a lista de nomes de colunas
    # print(colunas)

    # print(dados[:])

    if LumCodigo in colunas:
        LumIndex = colunas.index(LumCodigo)
    else:
        return False, LumCodigo + " não foi encontrado"

    dados_produto = dados[colunas[LumIndex]]

    Exp = {
        'CodZL': "Código ZL",
        'CodSe': "Código Senior",
        'DesSe': "Descrição Senior",
        'SitCa': "Situação Cadastro Caracteristicas Técnicas Senior",
        'Stat': "Status",
        'NoCer': "N° Certificado OCP (RV: xx) [PROCEL]",
        'NumRe': "Número de Registro de Objeto (Etiqueta ENCE)",
        'LED': "LED utilizado",
        'Estru': "Estrutura principal dissipador",
        'Dimen': "Dimensões (aproximadas) (Diâmetro x Comprimento)",
        'Encai': "Encaixe Padrão",
        'Compr': "Comprimento do Produto",
        'Peso': "Peso do produto (aproximado)",
        'Lente': "Lente*",
        'Fonte': "Fonte de luz",
        'Angul': "Ângulo de radiação luminosa",
        'Poten': "Potência nominal",
        'ClEff': "Classe de eficiência energética",
        'Fluxo': "Fluxo luminoso efetivo (lúmens) (±10%)",
        'Efica': "Eficacia luminosa (±10%)",
        'FluLED': "Fluxo luminoso do LED (Tj=25°C) (±10%)",
        'TempC': "Temperatura de cor correlata (TCC)",
        'Tensa': "Tensão de alimentação",
        'Corre': "Corrente de entrada",
        'Corre2': "Corrente e tensão de saída (driver)",
        'Fator': "Fator de potência (FP)",
        'Disto': "Distorção harmônica total de corrente (ATHD)",
        'IRC': "Índice de reprodução de cor (IRC)",
        'GrauP': "Grau de proteção",
        'DispP': "Dispositivo de proteção contra surtos (DPS)",
        'Prote': "Proteção contra sobretensões transitórias",
        'Corre3': "Corrente de fuga NBR IEC 60.598-1",
        'ClIs': "Classe de isolação elétrica",
        'MarMo': "Marca | Modelo | Potência (driver)",
        'TempO': "Temperatura ambiente de operação (Ta)",
        'ProtI': "Proteção contra impacto",
        'VidaL': "Vida útil do LED (reportada TM-21-11)",
        'VidaL2': "Vida útil do LED (projetada TM-21-11)***",
        'Ligaç': "Ligação à rede elétrica (Fase e Neutro)",
        'Garnt': "Garantia (contra defeitos de fabricação)",
        'DatVa': "Data de validade para armazenamento",
        'Revis': "Revisão IES",
        'LenPr': "Length(Prod.)",
        'WidPr': "Width(Prod.)",
        'HeiPr': "Height(Prod.)",
        'LenEm': "Lenght(Emissão)",
        'WidEm': "Width(Emissão)",
        'HeiEm': "Height(Emissão)",
        'NoFon': "N° de Fontes Luminosas"
    }

    assemblyData= {}

    for i,j in zip(dados[colunas[0]],dados[colunas[LumIndex]]):
        assemblyData[str(i)] = j
        
    dados_produto = assemblyData

    ExcDados = {
        'CodZL': LumCodigo,
        'CodSe': dados_produto.get('Zag11', 'N/A'),
        'DesSe': dados_produto.get('Zag1', 'N/A'),
        'Stat': dados_produto.get('Zag2', 'N/A'),
        'Estru': dados_produto.get('112', 'N/A'),
        'Dimen': dados_produto.get('15', 'N/A'),
        'Encai': dados_produto.get('113', 'N/A'),
        'Compr': dados_produto.get('134', 'N/A'),
        'Peso': dados_produto.get('20', 'N/A'),
        'Lente': dados_produto.get('104', 'N/A'),
        'Fonte': dados_produto.get('9', 'N/A'),
        'Angul': dados_produto.get('108', 'N/A'),
        'Poten': ''.join(caracter for caracter in dados_produto.get('5', 'N/A') if caracter.isdigit()),
        'ClEff': dados_produto.get('115', 'N/A'),
        'Fluxo': dados_produto.get('11', 'N/A'),
        'Efica': dados_produto.get('29', 'N/A'),
        'FluLED': dados_produto.get('46', 'N/A'),
        'TempC': dados_produto.get('2', 'N/A'),
        'Tensa': dados_produto.get('1', 'N/A'),
        'Corre': dados_produto.get('22', 'N/A'),
        'Corre2': dados_produto.get('27', 'N/A'),
        'Fator': dados_produto.get('3', 'N/A'),
        'Disto': dados_produto.get('122', 'N/A'),
        'IRC': dados_produto.get('18', 'N/A'),
        'GrauP': dados_produto.get('114', 'N/A'),
        'DispP': dados_produto.get('102', 'N/A'),
        'Prote': dados_produto.get('123', 'N/A'),
        'Corre3': dados_produto.get('158', 'N/A'),
        'ClIs': dados_produto.get('116', 'N/A'),
        'MarMo': dados_produto.get('124', 'N/A'),
        'TempO': dados_produto.get('7', 'N/A'),
        'ProtI': dados_produto.get('117', 'N/A'),
        'VidaL': dados_produto.get('35', 'N/A'),
        'VidaL2': dados_produto.get('118', 'N/A'),
        'Ligaç': dados_produto.get('119', 'N/A'),
        'Garnt': dados_produto.get('120', 'N/A'),
        'DatVa': dados_produto.get('121', 'N/A'),
        'Revis': dados_produto.get('Zag3', 'N/A'),
        'LenPr': dados_produto.get('Zag4', 'N/A')[:-2],
        'WidPr': dados_produto.get('Zag5', 'N/A')[:-2],
        'HeiPr': dados_produto.get('Zag6', 'N/A')[:-2],
        'LenEm': dados_produto.get('Zag7', 'N/A')[:-2],
        'WidEm': dados_produto.get('Zag8', 'N/A')[:-2],
        'HeiEm': dados_produto.get('Zag9', 'N/A')[:-2],
        'NoFon': dados_produto.get('Zag10', 'N/A')
    }

    for key in ExcDados.keys():
        #print(str(ExcDados[key]) + '\t\t # ' + (Exp[key]))
        ExcDados[key] = str(ExcDados[key])

    return ExcDados, Exp

Arq = "./teste.IES"

# Especifique o caminho do arquivo XLSX que deseja ler
caminho_arquivo = './Iluminacao_Zagonel_Caracteristicas_Tecnicas.xlsx'

# Especifique o nome da aba que deseja ler ou o índice numérico da aba (começando em 0)
nome_aba = 'ZL28'  # ou índice_aba = 0

LumCodigo='ZL 2805'
ExcDados, Exp = OpenExc(LumCodigo, caminho_arquivo, nome_aba)

ExcDados
'''import pandas as pd


def OpenExc(LumCodigo, caminho_arquivo, nome_aba):

    if (nome_aba in pd.ExcelFile(caminho_arquivo).sheet_names) == False:
        return False, "a aba " + nome_aba + " não encontrada"

    # Use a função `read_excel` do pandas para ler a aba específica
    dados = pd.read_excel(caminho_arquivo, sheet_name=nome_aba,
                          skiprows=1)  # pula a primeira Linha

    # Obtenha a lista de nomes de colunas
    colunas = list(dados.columns)

    # Exiba a lista de nomes de colunas
    # print(colunas)

    # print(dados[:])

    if LumCodigo in colunas:
        LumIndex = colunas.index(LumCodigo)
    else:
        return False, LumCodigo + " não foi encontrado"

    dados_produto = dados[colunas[LumIndex]]

    Exp = {
        'CodZL': "Código ZL",
        'CodSe': "Código Senior",
        'DesSe': "Descrição Senior",
        'SitCa': "Situação Cadastro Caracteristicas Técnicas Senior",
        'Stat': "Status",
        'NoCer': "N° Certificado OCP (RV: xx) [PROCEL]",
        'NumRe': "Número de Registro de Objeto (Etiqueta ENCE)",
        'LED': "LED utilizado",
        'Estru': "Estrutura principal dissipador",
        'Dimen': "Dimensões (aproximadas) (Diâmetro x Comprimento)",
        'Encai': "Encaixe Padrão",
        'Compr': "Comprimento do Produto",
        'Peso': "Peso do produto (aproximado)",
        'Lente': "Lente*",
        'Fonte': "Fonte de luz",
        'Angul': "Ângulo de radiação luminosa",
        'Poten': "Potência nominal",
        'ClEff': "Classe de eficiência energética",
        'Fluxo': "Fluxo luminoso efetivo (lúmens) (±10%)",
        'Efica': "Eficacia luminosa (±10%)",
        'FluLED': "Fluxo luminoso do LED (Tj=25°C) (±10%)",
        'TempC': "Temperatura de cor correlata (TCC)",
        'Tensa': "Tensão de alimentação",
        'Corre': "Corrente de entrada",
        'Corre2': "Corrente e tensão de saída (driver)",
        'Fator': "Fator de potência (FP)",
        'Disto': "Distorção harmônica total de corrente (ATHD)",
        'IRC': "Índice de reprodução de cor (IRC)",
        'GrauP': "Grau de proteção",
        'DispP': "Dispositivo de proteção contra surtos (DPS)",
        'Prote': "Proteção contra sobretensões transitórias",
        'Corre3': "Corrente de fuga NBR IEC 60.598-1",
        'ClIs': "Classe de isolação elétrica",
        'MarMo': "Marca | Modelo | Potência (driver)",
        'TempO': "Temperatura ambiente de operação (Ta)",
        'ProtI': "Proteção contra impacto",
        'VidaL': "Vida útil do LED (reportada TM-21-11)",
        'VidaL2': "Vida útil do LED (projetada TM-21-11)***",
        'Ligaç': "Ligação à rede elétrica (Fase e Neutro)",
        'Garnt': "Garantia (contra defeitos de fabricação)",
        'DatVa': "Data de validade para armazenamento",
        'Revis': "Revisão IES",
        'LenPr': "Length(Prod.)",
        'WidPr': "Width(Prod.)",
        'HeiPr': "Height(Prod.)",
        'LenEm': "Lenght(Emissão)",
        'WidEm': "Width(Emissão)",
        'HeiEm': "Height(Emissão)",
        'NoFon': "N° de Fontes Luminosas"
    }
    ExcDados = {
        'CodZL': LumCodigo,             # Codigo ZL
        'CodSe': dados_produto[0],      # Código Senior
        'DesSe': dados_produto[1],      # Descrição Senior
        # Situação Cadastro Caracteristicas Técnicas Senior
        'SitCa': dados_produto[2],
        'Stat': dados_produto[3],       # Status
        'NoCer': dados_produto[4],      # N° Certificado OCP (RV: xx) [PROCEL]
        # Número de Registro de Objeto (Etiqueta ENCE)
        'NumRe': dados_produto[5],
        'LED': dados_produto[6],        # LED utilizado
        'Estru': dados_produto[7],      # Estrutura principal dissipador
        # Dimensões (aproximadas) (Diâmetro x Comprimento)
        'Dimen': dados_produto[8],
        'Encai': dados_produto[9],      # Encaixe Padrão
        'Compr': dados_produto[10],     # Comprimento do Produto
        'Peso': dados_produto[11],      # Peso do produto (aproximado)
        'Lente': dados_produto[12],     # Lente*
        'Fonte': dados_produto[13],     # Fonte de luz
        'Angul': dados_produto[14],     # Ângulo de radiação luminosa
        'Poten':''.join(caracter for caracter in dados_produto[15] if caracter.isdigit()),     # Potência nominal
        'ClEff': dados_produto[16],     # Classe de eficiência energética
        # Fluxo luminoso efetivo (lúmens) (±10%)
        'Fluxo': dados_produto[17],
        'Efica': dados_produto[18],     # Eficacia luminosa (±10%)
        # Fluxo luminoso do LED (Tj=25°C) (±10%)
        'FluLED': dados_produto[19],
        'TempC': dados_produto[20],     # Temperatura de cor correlata (TCC)
        'Tensa': dados_produto[21],     # Tensão de alimentação
        'Corre': dados_produto[22],     # Corrente de entrada
        'Corre2': dados_produto[23],    # Corrente e tensão de saída (driver)
        'Fator': dados_produto[24],     # Fator de potência (FP)
        # Distorção harmônica total de corrente (ATHD)
        'Disto': dados_produto[25],
        'IRC': dados_produto[26],       # Índice de reprodução de cor (IRC)
        'GrauP': dados_produto[27],     # Grau de proteção
        # Dispositivo de proteção contra surtos (DPS)
        'DispP': dados_produto[28],
        # Proteção contra sobretensões transitórias
        'Prote': dados_produto[29],
        'Corre3': dados_produto[30],    # Corrente de fuga NBR IEC 60.598-1
        'ClIs': dados_produto[31],      # Classe de isolação elétrica
        'MarMo': dados_produto[32],     # Marca | Modelo | Potência (driver)
        'TempO': dados_produto[33],     # Temperatura ambiente de operação (Ta)
        'ProtI': dados_produto[34],     # Proteção contra impacto
        'VidaL': dados_produto[35],     # Vida útil do LED (reportada TM-21-11)
        # Vida útil do LED (projetada TM-21-11)***
        'VidaL2': dados_produto[36],
        # Ligação à rede elétrica (Fase e Neutro)
        'Ligaç': dados_produto[37],
        # Garantia (contra defeitos de fabricação)
        'Garnt': dados_produto[38],
        'DatVa': dados_produto[39],     # Data de validade para armazenamento
        'Revis': dados_produto[40],     # Revisão IES
        'LenPr': dados_produto[41][:-2],     # Lenght(Prod.)
        'WidPr': dados_produto[42][:-2],     # Width(Prod.)
        'HeiPr': dados_produto[43][:-2],     # Height(Prod.)
        'LenEm': dados_produto[44][:-2],     # Lenght(Emissão)
        'WidEm': dados_produto[45][:-2],     # Width(Emissão)
        'HeiEm': dados_produto[46][:-2],     # Height(Emissão)
        'NoFon': dados_produto[47]      # N° de Fontes Luminosas
    }

    for key in ExcDados.keys():
        #print(str(ExcDados[key]) + '\t\t # ' + (Exp[key]))
        ExcDados[key] = str(ExcDados[key])

    return ExcDados, Exp
'''