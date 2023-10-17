
def NewLDT(IES,Dados, Nome):
    arquivo = open('./LDTs/'+Nome+".LDT", 'w', encoding='utf-8')

    arquivo.write(Dados['Fabri']+"\n")  # 1

    arquivo.write(Dados['Tipo']+"\n")  # 2

    arquivo. write(Dados['Simetria']+"\n")  # 3

    arquivo.write(Dados['Mc']+"\n")  # 4

    arquivo.write(Dados['Dc']+"\n")  # 5

    arquivo.write(Dados['Ng'] + "\n")  # 6

    arquivo.write(Dados['Dg'] + "\n")  # 7

    arquivo.write(Dados['NumeroRelatorio'] + "\n")  # 8

    arquivo.write(Dados['NomeLuminaria'] + "\n")  # 9

    arquivo.write(Dados['NumeroLuminaria'] + "\n")  # 10

    arquivo.write(Dados['NomeArquivo'] + "\n")  # 11

    arquivo.write(Dados['DataUsuario'] + "\n")  # 12

    arquivo.write(Dados['ComprimentoDiametro'] + "\n")  # 13

    arquivo.write(Dados['LarguraLuminaria'] + "\n")  # 14

    arquivo.write(Dados['AlturaLuminaria'] + "\n")  # 15

    arquivo.write(Dados['ComprimentoDiametroArea'] + "\n")  # 16

    arquivo.write(Dados['LarguraArea'] + "\n")  # 17

    arquivo.write(Dados['AlturaAreaC0'] + "\n")  # 18

    arquivo.write(Dados['AlturaAreaC90'] + "\n")  # 19

    arquivo.write(Dados['AlturaAreaC180'] + "\n")  # 20

    arquivo.write(Dados['AlturaAreaC270'] + "\n")  # 21

    arquivo.write(Dados['DFF'] + "\n")  # 22

    arquivo.write(Dados['LORL'] + "\n")  # 23

    arquivo.write(Dados['FatorConversao'] + "\n")  # 24

    arquivo.write(Dados['InclinacaoLuminaria'] + "\n")  # 25

    arquivo.write(Dados['NumeroConjuntosLampadas'] + "\n")  # 26
