from ReadIES import IES, coord, rad, grad, dif
from ReadIES import *
import numpy as np
import matplotlib.pyplot as plt
import statistics as st
import os


def Visual(arq, sub, ang):

    print('Abrindo...> ' + arq + ' >>>'+'IES_' + arq)

    ies1 = IES(arq)

    number = (len(ies1.AngH())-1)/2-ang*(len(ies1.AngH())-1)/4
    angulo = int(number)

    if (os.path.exists('./out/'+arq[:int(len(arq)-4)]) != 1):
        os.makedirs('./out/' + arq[:int(len(arq)-4)])

    Valplt = coord(ies1.Cd(), angulo)  # valor em Cd para cada angulo

    maxmd = [0, 0]
    maxme = [0, 0]

    for i, j in zip(Valplt, range(len(Valplt))):
        if (i > maxmd[0] and j < int(len(Valplt)/2)):
            maxmd[0] = i
            maxmd[1] = float(j)

        if (i > maxme[0] and j > int(len(Valplt)/2)):
            maxme[0] = i
            maxme[1] = float(j)
    print(i, j)

    meio = ((maxme[1]-maxmd[1])/2)+maxmd[1]+180

    plt.figure(figsize=(10, 10))

    plt.axes(projection='polar')

    x1 = list(range(90, 180, 10))
    x2 = sorted(x1, key=int, reverse=True)
    x3 = list(range(10, 90, 10))
    x4 = sorted(x3, key=int, reverse=True)
    x = x1+[180]+x2+x4+[0]+x3

    plt.thetagrids(range(0, 360, 10), x)
    plt.title("Distribuição de intensidade luminosa na Curva\n" +
              sub, fontsize=16)
    plt.quiver(0, 0, maxmd[1]*np.pi/180-np.pi/2, maxmd[0], color='red',
               angles="xy", scale_units='xy', scale=1.)
    plt.fill(rad(Valplt), Valplt, '.r', alpha=0.2)
    plt.quiver(0, 0, maxme[1]*np.pi/180-np.pi/2, maxme[0], color='blue',
               angles="xy", scale_units='xy', scale=1.)

    plt.quiver(0, 0, meio*np.pi/180-np.pi/2, (maxme[0]+maxme[0])/2, color='g',
               angles="xy", scale_units='xy', scale=1.)

    plt.text((meio+15)*np.pi/180-np.pi/2, (maxme[0]+maxme[0])/4, 'Diferença em graus = ' +
             str(360-meio)[:5]+" °")

    plt.savefig('./Distribuição_'+sub+'.png')
    #plt.show()

    plt.figure(figsize=(10, 10))
    plt.subplot(2, 1, 1)
    plt.title('Simetria da distribuição luminosa\n'+sub)
    plt.plot(grad(Valplt)[:180], Valplt[180:], color='blue')

    plt.plot(grad(Valplt)[180:], Valplt[0:180], color='red')

    plt.axhline(y=max(Valplt[0:180]), color='r', linestyle='-.', alpha=0.5)

    plt.axhline(y=max(Valplt[180:]), color='b', linestyle='-.', alpha=0.5)

    plt.axvline(x=maxmd[1], color='r', linestyle=':', alpha=0.5)

    plt.axvline(x=360-maxme[1], color='b', linestyle=':', alpha=0.5)

    plt.text(8, dif(max(Valplt[0:180]), max(Valplt[180:]), 2), 'Média da diferença = '+str(
        dif(max(Valplt[0:180]), max(Valplt[180:]), 0))[:5]+"%"+"\nDiferença absoluta = "+str(dif(max(Valplt[0:180]), max(Valplt[180:]), 2)).split(".")[0]+"Cd", style='italic')

    plt.subplot(2, 1, 2)
    plt.fill(grad(Valplt)[:180], dif(Valplt[180:],
                                     Valplt[0:180], 3), color='r', alpha=0.2)

    print(dif(max(Valplt[0:180]), max(Valplt[180:]), 0))

    plt.text(8, max(dif(Valplt[180:], Valplt[0:180], 3)), 'Máxima da diferença = '+str(max(dif(Valplt[180:],
                                                                                               Valplt[0:180], 3)))[:5], style='italic')
    plt.text(8, st.mean(dif(Valplt[180:], Valplt[0:180], 3)), 'Média da diferença = '+str(st.mean(dif(Valplt[180:],
                                                                                                      Valplt[0:180], 3)))[:5], style='italic')
    '''plt.scatter(grad(Valplt)[:180], dif(Valplt[180:],
                                        Valplt[0:180]), c=dif(Valplt[180:], Valplt[0:180]))'''
    plt.axhline(y=st.mean(dif(Valplt[180:],
                              Valplt[0:180], 3)), color='r', linestyle='-', alpha=0.6)

    plt.savefig('./Simetria_'+sub+'.png')

    #plt.show()