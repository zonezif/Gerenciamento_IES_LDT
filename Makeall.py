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
'''
# IES original
Arq = "./teste.IES"

# Especifique o caminho do arquivo XLSX que deseja ler
caminho_arquivo_ex = './Iluminacao_Zagonel_Caracteristicas_Tecnicas.xlsx'

# Especifique o nome da aba que deseja ler ou o índice numérico da aba (começando em 0)
nome_aba_ex = 'ZL28'  # ou índice_aba = 0

'''

def MakeAll(Arq_IES,caminho_arquivo_ex,nome_aba_ex,nome,AssIES,AssLDT):

    ies = IES(Arq_IES)

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
  
    LumCodigo = ies.dic['[LUMCAT]'][0].strip()

    ExcDados, Exp = OpenExc(LumCodigo, caminho_arquivo_ex, nome_aba_ex)

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
        DadosIES = {}

        for key in AssIES.keys():
            for com in AssIES[key].split(','):
                if not(key in DadosIES):
                    DadosIES[key] =''
                if com in ExcDados.keys():
                    DadosIES[key] += str(ExcDados[com])
                elif com in IESimport:
                    DadosIES[key] += str(IESimport[com])
                elif com in Comandos:
                    DadosIES[key] += str(Comandos[com])
                else:
                    DadosIES[key] += str(com)
        ##fim IES

        ##Inicio do LDT
        
        DadosLDT={}
    
        
        for key in AssLDT.keys():
                for com in AssLDT[key].split(','):
                    if not(key in DadosLDT):
                        DadosLDT[key] =''
                    if com in ExcDados.keys():
                        DadosLDT[key] += str(ExcDados[com])
                    elif com in IESimport:
                        DadosLDT[key] += str(IESimport[com])
                    elif com in Comandos:
                        DadosLDT[key] += str(Comandos[com])
                    else:
                        DadosLDT[key] += str(com)
    #Fim LDT 
    ArqName = ''
    
    for com in nome.split(','):
                    if com in ExcDados.keys():
                        ArqName += str(ExcDados[com])
                    elif com in IESimport:
                        ArqName += str(IESimport[com])
                    elif com in Comandos:
                        ArqName += str(Comandos[com])
                    else:
                        ArqName += str(com)

    NewLDT(ies,DadosLDT,ArqName)
    NewIES(ies, DadosIES, ArqName)