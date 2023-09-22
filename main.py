import pickle
from ReadIES import *

# Dados de exemplo
dados = IES("./teste.IES")

# Imagem de exemplo (substitua pelo caminho da sua imagem)
caminho_imagem = "./tesst.jpg"

# Função para salvar as informações em um arquivo binário com a image


def Exp_gedr(filename, dados, imagem):
    with open(filename, 'wb') as file:
        dados = {'Revs': {'Rev1': dados, 'Rev2': dados},
                 'Imgs': {'Img1': imagem}}
        pickle.dump(dados, file)


# Função para recuperar informações de um arquivo binário com a imagem
def GEDR(filename):
    with open(filename, 'rb') as file:
        dados = pickle.load(file)
    return dados['Revs'], dados['Imgs']


# Nome do arquivo
nome_arquivo = "TEST.gedr"

# Lendo a imagem em bytes
with open(caminho_imagem, 'rb') as img_file:
    imagem_bytes = img_file.read()

# Salvando as informações (dados e imagem) em formato binário
Exp_gedr(nome_arquivo, dados, imagem_bytes)

# Recuperando as informações (dados e imagem) do arquivo binário
IESs, imagem_recuperada = GEDR(nome_arquivo)

# Salvando a imagem recuperada
with open('imagem_recuperada.jpg', 'wb') as img_file:
    img_file.write(imagem_recuperada['Img1'])

for chave in IESs:
    print(chave)

print("Imagem recuperada com sucesso!")
