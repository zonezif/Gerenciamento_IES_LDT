from ReadIES import *

ies = IES("./teste.IES")

Dados = {
    'Fabricante': ies.dic['[MANUFAC]'][0].strip(),
    'Luminaria_Cod': ies.dic['[TEST]'][0].strip(),
    'Data': ies.dic['[TESTDATE]'][0].strip(),
    'Luminaria': ies.dic['[LUMINAIRE]'][0].strip(),
    'Lampada': ies.dic['[LAMP]'][0].strip(),
    'Lampada_Descr': ies.dic['[LAMPCAT]'][0].strip(),
    'Teste_Lab': ies.dic['[TESTLAB]'][0].strip(),
    'Flash_Area': ies.dic['[FLASHAREA]'][0].strip(),
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


def NewIES(Dados, Nome):

    arquivo = open('./IESs/'+Nome+".IES", 'w', encoding=encodingIES)

    arquivo.write('IESNA:LM-63-2002\n')
    arquivo.write('[TEST] '+Dados['Luminaria_Cod'].strip() + "\n")
    arquivo.write('[TESTLAB] '+Dados['Teste_Lab'] + "\n")
    arquivo.write('[TESTDATE] '+Dados['Data'] + "\n")
    arquivo.write('[ISSUEDATE] '+Dados['Data'] + "\n")
    arquivo.write('[MANUFAC] '+Dados['Teste_Lab'] + "\n")
    arquivo.write('[LUMCAT] '+Dados['Luminaria_Cod'].strip() + "\n")
    arquivo.write('[LUMINAIRE] '+Dados['Luminaria'] + "\n")
    arquivo.write('[LAMPCAT] '+Dados['Lampada_Descr'] + "\n")
    arquivo.write('[LAMP] '+Dados['Lampada'] + "\n")
    arquivo.write('[FLASHAREA] '+Dados['Flash_Area'] + "\n")
    arquivo.write(str(Dados['Lampada_Num']) + "\n")
    arquivo.write(str(Dados['Fluxo_P_Lamp']) + "\n")
    arquivo.write(str(Dados['CD_Multiplicador']) + "\n")
    arquivo.write(str(Dados['Num_Ang_verticais']) + "\n")
    arquivo.write(str(Dados['Num_Ang_Horizontais']) + "\n")


NewIES(Dados, "teste2")
