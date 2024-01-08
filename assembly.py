#lucas Ribeiro Nunes#
from ReadIES import *
from ReadExc import *
from MakeIES import *
from MakeLDT import *

import datetime
data_atual = datetime.date.today()

ano = data_atual.year
mes = data_atual.month
dia = data_atual.day

# IES original
Arq = "./teste.IES"

# Especifique o caminho do arquivo XLSX que deseja ler
caminho_arquivo = './Iluminacao_Zagonel_Caracteristicas_Tecnicas.xlsx'

# Especifique o nome da aba que deseja ler ou o índice numérico da aba (começando em 0)
nome_aba = 'ZL28'  # ou índice_aba = 0

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

ies = IES(Arq)

IESimport = {
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
    'Num_Av': ies.Nang(),
    'Num_Ah': ies.Nah(),
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
    'Num_Av': 'Num_Ang_verticais',
    'Num_Ah': 'Num_Ang_Horizontais',
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

LumCodigo = ies.dic['[LUMCAT]'][0].strip()

ExcDados, Exp = OpenExc(LumCodigo, caminho_arquivo, nome_aba)

if(ExcDados == False):
    print(Exp)
else:
    '''
    Comandos extras

    IES pega data do dia 
    DataIES pega data do IES

    '''
    Comandos = {
        'DataAtualIES': str(dia) + " "+meses[mes]+" "+str(ano),
        'DataAtulaLDT':str(dia) + "-"+str(mes)+"-"+str(ano),
        'DataIES': IESimport['Data'],
        'mc': str(int(IESimport['Num_Ah'])-1),
        'dc':str(360/(int(IESimport['Num_Ah'])-1)),
        'ng':IESimport['Num_Av'],
        'dg':str(180/(int(IESimport['Num_Av'])-1)),
        'numLamp':str(ies.Nlamp()),
        'Lm':str(ies.Lm())
    }
## Organização para o IES
    AssIES = {
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
    }

    DadosIES = {
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

    for key in AssIES.keys():
        for com in AssIES[key].split(','):
            if com in ExcDados.keys():
                DadosIES[key] += str(ExcDados[com])
            elif com in IESimport:
                DadosIES[key] += str(IESimport[com])
            elif com in Comandos:
                DadosIES[key] += str(Comandos[com])
            else:
                DadosIES[key] += str(com)

    #print(Dados)
    NewIES(ies, DadosIES, 'Nome')
    ##fim IES

    ##Inicio do LDT
    AssLDT={
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

    DadosLDT={
        'Manufac':'',
        'ltyp':'',
        'lsym':'',
        'mc':'',
        'dc':'',
        'ng':'',
        'dg':'',
        'serNum':'', #editavel
        'lumNam':'',
        'lumNum':'',
        'arquvNam':'',
        'data':'',
        'compr':'',
        'larg':'',
        'altur':'',
        'comprLum':'',
        'lagurLum':'',
        'Cp1':'',
        'Cp2':'',
        'Cp3':'',
        'Cp4':'',
        'DFF':'',
        'LORL':'',
        'mult':'',
        'tilt':'',
        'numLampSTD':'',
        'numLamp':'',
        'typelamp':'',
        'Lm':'',
        'colorapp':'',
        'colorrender':'',
        'potencia':''
    }
    #Fim LDT
    
    for key in AssLDT.keys():
            for com in AssLDT[key].split(','):
                if com in ExcDados.keys():
                    DadosLDT[key] += str(ExcDados[com])
                elif com in IESimport:
                    DadosLDT[key] += str(IESimport[com])
                elif com in Comandos:
                    DadosLDT[key] += str(Comandos[com])
                else:
                    DadosLDT[key] += str(com)
                    
    NewLDT(ies,DadosLDT,'Nome')

