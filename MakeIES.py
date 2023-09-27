
def NewIES(Dados, Nome):

    arquivo = open('./IESs/'+Nome+".IES", 'w', encoding='utf-8')

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
