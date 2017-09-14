# definir sky
from astropy.io import fits
import numpy as np
import matplotlib.pyplot as plt
import glob

def abrindo_imagens(icaminho,campo):
    
    IMG = []
    HDR= []
    for nome_imagem in glob.glob(icaminho+'%s.*.fits'%campo):
        #descobri essa maravilhosa função só agora :(, ela é capaz de abrir )
        img, hdr = fits.getdata(nome_imagem, header=True)
        img = np.array(img, dtype='Float64')   
        IMG.append(img)
        HDR.append(hdr)
    return IMG, HDR
 
def imagem_sky(bcaminho,fcaminho,icaminho,campo,bnumero,fnumero,filtro):
    imagem = abrindo_imagens(icaminho, campo)[0][0]
    print ("com base na imagem abaixo informe a região (100x100) do céu que nao possue estrelas")
    plt.figure()
    fig, eixos = plt.subplots(nrows=1, ncols=1, figsize=(15,10))
    grafico = plt.imshow(imagem,vmin=np.mean(imagem)-2.5*np.std(imagem),
        vmax=np.mean(imagem)+2.5*np.std(imagem),cmap=plt.cm.gray,origin='lower')
    plt.show()
    xi = int(input("Ponto inicial no eixo x: "))
    xf = int(input("Ponto final no eixo x: "))
    yi = int(input("Ponto inicial no eixo y: "))
    yf = int(input("Ponto final no eixo y: "))
    
    regiao = imagem[xi:xf, yi:yf]
    sky_imagem = np.random.poisson(np.mean(regiao), imagem.shape)
    return sky_imagem