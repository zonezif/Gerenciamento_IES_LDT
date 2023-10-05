
def NewIES(ies, Dados, Nome):

    dd1 = ies.Cd()
    av = ies.AngV()
    top = ies.Top()
    ah = ies.AngH()
    arquivo = open('./IESs/'+Nome+".IES", 'w', encoding='utf-8')

    arquivo.write('IESNA:LM-63-2002\n')

    for key in Dados.keys():
        arquivo.write(key+' '+Dados[key]+"\n")

    for i in top[top.index('TILT=NONE'):]:
        arquivo.write(i+'\n')

    for i, j in zip(av, range(len(av))):
        arquivo.write(str(i)+' ')
        arquivo.write((" "*(8-len(str(i)))))
        if ((j+1) % 10 == 0):
            arquivo.write('\n')

    arquivo.write('\n')

    for i, j in zip(ah, range(len(ah))):
        arquivo.write(str(i)+' ')
        arquivo.write((" "*(8-len(str(i)))))
        if ((j+1) % 10 == 0):
            arquivo.write('\n')

    arquivo.write('\n')

    for l in range(len(dd1)):

        for i, j in zip(dd1[l], range(int(ies.Nang()))):
            arquivo.write(str(i)+' ')
            arquivo.write((" "*(8-len(str(i)))))
            if ((j+1) % 10 == 0):
                arquivo.write('\n')

        arquivo.write('\n')
    arquivo.close()


'''
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
'''
