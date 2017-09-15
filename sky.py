# Abre as iamgens de ciencia e define a região de sky

from astropy.io import fits
import numpy as np
import matplotlib.pyplot as plt
import glob

def abrindo_imagens(icaminho,campo):
    ''' Função responsavel por abrir as imagens de ciencias que serão corrigidas. Tem como parâmetro:

            abrindo_imagens(icaminho,campo)

    Retorna uma lista contendo todas as imagens que estivem no diretório e com o campo indicado
    '''
    #lista onde sera adicionado as imagens
    IMG = []
    HDR = []
    for nome_imagem in glob.glob(icaminho+'%s.*.fits'%campo): 
        #função glob abre imagens fits indentificando todas as imagens que tem um padrão de nomenclatura igual ao indicado
        #como parametro da função. O * implica na abertura de todas as imagens com esse padrão campo.numero.fits
        img, hdr = fits.getdata(nome_imagem, header=True) #salva em img apenas a matriz de dados
        # converte os dados para float64        
        img = np.array(img, dtype='Float64')   
        IMG.append(img) #adiciona os dados atuais na lista geral de dados
        HDR.append(hdr)
    return IMG, HDR
 
def imagem_sky(bcaminho,fcaminho,icaminho,campo,bnumero,fnumero,filtro):
    ''' Essa é a função responsavel por corrigir o background das imagens. Ela ira fornecer uma imagem exemplar das
    imagens a serem corrigidas para que o usuário escolha uma região que não tenha estrelas. Essa região dever ter uma 
    dimenção de 100 x 100 e estar limita entre as dimensões da imagem. Tem como entrada:

            imagem_sky(bcaminho,fcaminho,icaminho,campo,bnumero,fnumero,filtro)

    Tem como saída uma matriz com as dimensões da imagem construida a partir de uma distribuição poissonica com média  
    obitida nos valores da região indica pelo usuário.
    '''
    imagem = abrindo_imagens(icaminho, campo)[0][0] #abre a imagem a ser cálculado o background
    #plota a imagem para o usuário determinar a região
    plt.figure()
    fig, eixos = plt.subplots(nrows=1, ncols=1, figsize=(15,10))
    grafico = plt.imshow(imagem,vmin=np.mean(imagem)-2.5*np.std(imagem),
        vmax=np.mean(imagem)+2.5*np.std(imagem),cmap=plt.cm.gray,origin='lower')
    plt.title("com base na imagem abaixo informe a região (100x100) do céu que nao possue estrelas") 
    #plt.set_title("com base na imagem abaixo informe a região (100x100) do céu que nao possue estrelas")
    plt.show()
    #informa os valores iniciais e finais da região
    xi = int(input("Ponto inicial no eixo x: "))
    xf = int(input("Ponto final no eixo x: "))
    yi = int(input("Ponto inicial no eixo y: "))
    yf = int(input("Ponto final no eixo y: "))
    
    regiao = imagem[xi:xf, yi:yf] #cria a matriz com apenas a parte da imagem que esteja dentro dos limites indicados
    sky_imagem = np.random.poisson(np.mean(regiao), imagem.shape) #produz a matriz aleatório, poissonica com tamho da imagem
    return sky_imagem
