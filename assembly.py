#lucas Ribeiro Nunes#
from ReadIES import *
from ReadExc import *
from MakeIES import *

import datetime
data_atual = datetime.date.today()

ano = data_atual.year
mes = data_atual.month
dia = data_atual.day

meses = {
    1: 'Jan',
    2: 'Feb',
    3: 'Mar',
    4: 'Apr',
    5: 'May',
    6: 'Jun',
    7: 'Jul',
    8: 'Aug',
    9: 'Sep',
    10: 'Oct',
    11: 'Nov',
    12: 'Dec'
}

ies = IES("./teste.IES")

DadosIES = {
    'Fabri': ies.dic['[MANUFAC]'][0].strip(),
    'Lumin': ies.dic['[TEST]'][0].strip(),
    'Data': ies.dic['[TESTDATE]'][0].strip(),
    'Lumin': ies.dic['[LUMINAIRE]'][0].strip(),
    'Lampa': ies.dic['[LAMP]'][0].strip(),
    'Lampada': ies.dic['[LAMPCAT]'][0].strip(),
    'Teste': ies.dic['[TESTLAB]'][0].strip(),
    'Flash': ies.dic['[FLASHAREA]'][0].strip(),
    'Lampa': ies.Nlamp(),
    'Fluxo': ies.Lm(),
    'CD_Mu': ies.Fat(),
    'Num_A': ies.Nang(),
    'Num_A': ies.Nah(),
    'Ensaio': [],
    'Unida': [],
    'Largu': [],
    'Compr': [],
    'Altur': [],
    'Poten': [],
    'Angul': ies.AngV(),
    'Angul': ies.AngH(),
    'Cande': ies.Cd(),
    'Img_r': []
}
ExpIES = {
    'Fabri': 'Fabricante',
    'Lumin': 'Luminaria_Cod',
    'Data': 'Data',
    'Lumin': 'Luminaria',
    'Lampa': 'Lampada',
    'Lampada': 'Lampada_Descr',
    'Teste': 'Teste_Lab',
    'Flash': 'Flash_Area',
    'Lampa': 'Lampada_Num',
    'Fluxo': 'Fluxo_P_Lamp',
    'CD_Mu': 'CD_Multiplicador',
    'Num_A': 'Num_Ang_verticais',
    'Num_A': 'Num_Ang_Horizontais',
    'Ensaio': 'Ensaio_Tipo',
    'Unida': 'Unidade_Medida',
    'Largu': 'Largura',
    'Compr': 'Comprimento',
    'Altur': 'Altura',
    'Poten': 'Potencia',
    'Angul': 'Angulos_Verticas',
    'Angul': 'Angulos_horizontais',
    'Cande': 'Candela_Valores',
    'Img_r': 'Img_ref'
}


LumCodigo = 'ZL 2805'

# Especifique o caminho do arquivo XLSX que deseja ler
caminho_arquivo = './Iluminacao_Zagonel_Caracteristicas_Tecnicas.xlsx'

# Especifique o nome da aba que deseja ler ou o índice numérico da aba (começando em 0)

nome_aba = 'ZL28'  # ou índice_aba = 0

ExcDados, Exp = OpenExc(LumCodigo, caminho_arquivo, nome_aba)

if(ExcDados == False):
    print(Exp)
else:
    '''
    Comandos extras

    DataAtual pega data do dia 
    DataIES pega data do IES

    '''
    Comandos = {
        'DataAtual': str(dia) + " "+meses[mes]+" "+str(ano),
        'DataIES': DadosIES['Data']
    }

    Ass = {
        '[TEST]': 'CodZL',
        '[ISSUEDATE]': 'DataAtual, ,DataIES, lucas rev 22',
        '[MANUFAC]': 'Zagonel',
        '[LUMCAT]': 'CodZL',
        '[LUMINAIRE]': 'DesSe',
        '[LAMPCAT]': '',
        '[LAMP]': 'LED',
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
        '[FLASHAREA]': ''
    }

    Dados = {
        '[TEST]': '',
        '[ISSUEDATE]': '',
        '[MANUFAC]': '',
        '[LUMCAT]': '',
        '[LUMINAIRE]': '',
        '[LAMPCAT]': '',
        '[LAMP]': '',
        '[_VOLTAGE]': '',
        '[_CURRENT]': '',
        '[_POWERFACTOR]': '',
        '[TESTLAB]': '',
        '[_TESTINST]': '',
        '[_TESTDIST]': '',
        '[_TESTTEMPERATURE]': '',
        '[_TESTHUMIDITY]': '',
        '[_TESTOPERATOR]': '',
        '[BALLAST]': '',
        '[BALLASTCAT]': '',
        '[TESTDATE]': '',
        '[FLASHAREA]': ''
    }

    for key in Ass.keys():
        for com in Ass[key].split(','):
            if com in ExcDados.keys():
                Dados[key] += str(ExcDados[com])
            elif com in Comandos:
                Dados[key] += str(Comandos[com])
            else:
                Dados[key] += str(com)

print(Dados)

NewIES(ies, Dados, 'Nome')
