import numpy as np
import chardet
encodingIES = 'utf-8'


def Decode(name):
    with open(name, 'rb') as f:
        rawdata = f.read(10240)
        encodingIES = chardet.detect(rawdata)['encoding']
    return encodingIES


def abrir(name, nick):

    Decode(name)

    with open(name, "r", encoding=Decode(name)) as f:
        reader = f.read()

    x = reader
    x = x.splitlines()

    data = ""
    cabeçalho = []

    for i in range(len(x)):
        if (x[i] == 'TILT=NONE'):
            for j in x[i+1:]:
                data += j
                cabeçalho = x[:i+3]
            break
    dic = {}

    for i in cabeçalho:
        if (len(i.split()) > 1):
            dic[i.split()[0]] = i.split(']')[1:]

    if (nick == 0):
        data = data[:]
        return data

    if (nick == 1):
        data = data[4:len(data)-1]
        return data

    if (nick == 2):
        return (dic)

    if (nick == 3):
        return (cabeçalho)


def coord(data, angle):

    ex = angle
    defase = ex+int(len(data)/2)

    if(defase > len(data)-1):
        defase = defase-len(data)

    if(ex > len(data)-1):
        ex = ex-len(data)

    vet = data[defase]

    vet = vet[0:len(vet)-1]

    vet2 = data[ex]

    vet2 = vet2[0:len(vet2)-1]

    val = []
    l = len(vet2)

    for i in vet:
        val.append(float(i))

    for i in range(len(vet2)):
        val.append(float(vet2[l-1-i]))
    return val


def rad(vet):
    rads = []

    x = range(len(vet))

    for i in x:
        rads.append(float(i)*np.pi/180-np.pi/2)

    return rads


def grad(vet):
    grads = []

    x = range(int(len(vet)/2), 0, -1)
    for i in x:
        grads.append(i)

    x = range(int(len(vet)/2))

    for i in x:
        grads.append(i)

    return grads


def dif(v1, v2, p):
    difer = []
    if(p == 1):
        v2.reverse()
        for i, j in zip(v1, v2):
            difer.append(((np.sqrt((i-j)**2))/max(i, j))*100)
    if(p == 3):
        v2.reverse()
        for i, j in zip(v1, v2):
            difer.append(np.sqrt((i-j)**2))

    if(p == 2):
        return ((np.sqrt(v1-v2)**2))

    if(p == 0):
        return (100*(np.sqrt(v1-v2)**2)/max(v1, v2))

    return difer


class IES(object):

    def __init__(self, arq):
        self.x = abrir(arq, 0).split()
        self.off = 0

        AngV = [0]
        self.off = int(self.Nang())+11

        for i in self.x[12:self.off]:
            AngV.append(float(i))

        self.angv = AngV

        AngH = []
        for i in self.x[self.off:int(self.Nah())+self.off]:
            AngH.append(float(i))
        self.angh = AngH

        Cd = []

        self.off += int(self.Nah())

        for j in range(int(self.Nah())):
            cd = []
            for i in self.x[self.off:int(self.Nang())+self.off]:
                cd.append(float(i))
            self.off += int(self.Nang())
            Cd.append(cd)
        self.Xd = Cd

        self.dic = abrir(arq, 2)

        self.top = abrir(arq, 3)

    def Nlamp(self):
        return float(self.x[0])  # Numero de luminarias

    def Lm(self):
        return float(self.x[1])  # Fluxo

    def Fat(self):
        return float(self.x[2])  # Fator de multiplicação

    def Nang(self):
        return self.x[3]  # Numeros de angulos da teia

    def Nah(self):
        return self.x[4]  # numero de angulos horizontais

    def Unid(self):
        return self.x[6]  # Unidade 1 para pes 2 para metros

    def AngV(self):
        return self.angv

    def AngH(self):
        return self.angh

    def Cd(self):
        return self.Xd

    def Dic(self):
        return self.dic

    def Top(self):
        return self.top
