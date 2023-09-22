from ReadLDT import *
import os

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
def convert(arq):
    
    new = LDT(arq)

    arquivo = open('./IESs/'+arq.split(".")[0]+".IES", 'w', encoding='utf-8')

    arquivo.write('IESNA:LM-63-2002\n')

    arquivo.write("[TEST] " + new.Numero+"\n")

    arquivo.write("[TESTLAB] " + new.Fabricante +"\n")

    arquivo.write("[TESTDATE] "+str(dia) +" "+meses[mes]+" "+str(ano)+"\n")

    arquivo.write("[ISSUEDATE] "+str(dia) +" "+meses[mes]+" "+str(ano)+"\n")

    arquivo.write("[MANUFAC] "+ new.Fabricante+"\n")

    arquivo.write("[LUMCAT] "+ new.Numero+"\n") 

    arquivo.write("[LUMINAIRE] "+new.Nome+"\n")

    arquivo.write("[LAMPCAT] "+new.LampTip+"\n")

    arquivo.write("[LAMP] "+new.LampTip+"\n")

    arquivo.write("TILT=NONE\n")

    arquivo.write(new.Nlamp+" "+str(float(new.Fluxo)/float(new.Nlamp))+" "+new.FatC+" "+new.Ng+" "+str(int(new.McC)+1))

    arquivo.write(" 1")  #5.9 <photometric type> 1 tipo C

    arquivo.write(" 2 ")  #<units type> 2 metros

    arquivo.write(str(float(new.Llength)*10**(-3))+" "+str(float(new.Lwidth)*10**(-3))+" "+str(float(new.LheightC0)*10**(-3))+"\n")

    arquivo.write("1.00 1.00 "+new.Potencia+"\n")

    NNg = new.info[42+int(new.McC):42+int(new.McC) +int(new.Ng)]

    for i, j in zip(NNg, range(len(NNg))):
            arquivo.write(str(i)+' ')
            arquivo.write((" "*(8-len(str(i)))))
            if ((j+1) % 10 == 0):
                arquivo.write('\n')
                
    arquivo.write("\n")

    NMc = new.info[42:42+int(new.McC)]
    NMc.append("360.0")

    for i, j in zip(NMc, range(len(NMc))):
            arquivo.write(str(i)+' ')
            arquivo.write((" "*(8-len(str(i)))))
            if ((j+1) % 10 == 0):
                arquivo.write('\n')
                
    dd1 = new.info[42+int(new.McC) +int(new.Ng):]
            
    arquivo.write('\n')
    n=0
    for l in range(int(new.McC)):
        
        for i, j in zip(dd1[l*len(NNg):(1+l)*len(NNg)], range(l*len(NNg),(1+l)*len(NNg))):
            temp = str((round(float(i)*(float(new.Fluxo)/1000), 2)))
            arquivo.write(temp+' ')
            arquivo.write((" "*(8-len(temp))))
            
            if ((j+1-n) % 10 == 0):
                arquivo.write('\n')
                
        arquivo.write('\n')
        n+=1
        
    for i, j in zip(dd1[:len(NNg)], range(len(NNg))):
            temp = str((round(float(i)*(float(new.Fluxo)/1000), 2)))
            arquivo.write(temp+' ')
            arquivo.write((" "*(8-len(temp))))
            
            if ((j+1-n) % 10 == 0):
                arquivo.write('\n')
    arquivo.write('\n') 
       
    arquivo.close()
    print(arq +">>>"+ arq.split(".")[0]+".IES")

key = "s"

while key == "s":
    dire = input("\nArraste a pasta aqui!!").replace('"', "")
    os.system("cls")
    dire = dire.replace("'", "")
    dire = dire.replace("&", "")
    if dire[0] == " ":
        dire = dire[1:]
    print(dire)
    os.chdir(dire)

    page = os.getcwd()
    lista = os.listdir(page)
    LDTs = []
    cwd = page

    for i in lista:
        arq = i.split(".")
        if len(arq) > 1:
            if arq[1] == "LDT":
                LDTs.append(i)
            if arq[1] == "ldt":
                LDTs.append(i)

    if os.path.exists("IESs") != 1:
        os.makedirs(page + "//IESs")
        page += page + "//IESs"
  
    for i in LDTs:
        convert(i)


