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
        'Potên': "Potência nominal",
        'ClEff': "Classe de eficiência energética",
        'Fluxo': "Fluxo luminoso efetivo (lúmens) (±10%)",
        'Eficá': "Eficácia luminosa (±10%)",
        'FluLED': "Fluxo luminoso do LED (Tj=25°C) (±10%)",
        'TempC': "Temperatura de cor correlata (TCC)",
        'Tensã': "Tensão de alimentação",
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
        'Potên': dados_produto[15],     # Potência nominal
        'ClEff': dados_produto[16],     # Classe de eficiência energética
        # Fluxo luminoso efetivo (lúmens) (±10%)
        'Fluxo': dados_produto[17],
        'Eficá': dados_produto[18],     # Eficácia luminosa (±10%)
        # Fluxo luminoso do LED (Tj=25°C) (±10%)
        'FluLED': dados_produto[19],
        'TempC': dados_produto[20],     # Temperatura de cor correlata (TCC)
        'Tensã': dados_produto[21],     # Tensão de alimentação
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
        'LenPr': dados_produto[41],     # Lenght(Prod.)
        'WidPr': dados_produto[42],     # Width(Prod.)
        'HeiPr': dados_produto[43],     # Height(Prod.)
        'LenEm': dados_produto[44],     # Lenght(Emissão)
        'WidEm': dados_produto[45],     # Width(Emissão)
        'HeiEm': dados_produto[46],     # Height(Emissão)
        'NoFon': dados_produto[47]      # N° de Fontes Luminosas
    }

    for key in ExcDados.keys():
        print(str(ExcDados[key]) + '\t\t # ' + (Exp[key]))
        ExcDados[key] = str(ExcDados[key])

    return ExcDados, Exp
