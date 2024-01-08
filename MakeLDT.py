
def NewLDT(IES,Dados, Nome):
    arquivo = open('./LDTs/'+Nome+".LDT", 'w', encoding='utf-8')
    for key in Dados.keys():
        arquivo.write(Dados[key]+"\n")
    for i in range (10): arquivo.write('1\n')

    Nahnow=0
    DivaH = 360/(float(IES.Nah())-1)
    for i in range(int(360/DivaH)):
        arquivo.write(str(Nahnow)+"\n")
        Nahnow+= DivaH

    for i in range(int(IES.Nang())):
        arquivo.write(f'{float(i):.2f}\n')

    for i in range(len(IES.Cd())-1):
        for j in range(len(IES.Cd()[i])):
            arquivo.write(f'{float(IES.Cd()[i][j]) / IES.Lm() * 1000:.5f}\n')

