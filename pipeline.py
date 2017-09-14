#pipeline


from astropy.io import fits
import numpy as np 
import bias
import flat
import sky

def bimagens(bcaminho, icaminho, campo, bnumero, filtro):
    bciencia = []
    imagen_ciencia = sky.abrindo_imagens(icaminho,campo)[0]
    imagen_bias = bias.bias_median(bcaminho,bnumero, filtro)
    for i in range(len(imagen_ciencia)):
        img = imagen_ciencia[i] - imagen_bias
        bciencia.append(img)
    return bciencia
 
def fbimagens(bcaminho, fcaminho, icaminho, campo, bnumero, fnumero, filtro):
    fbciencia = []
    bciencia = bimagens(bcaminho, icaminho, campo, bnumero, filtro)
    imagem_flat = flat.flat_field(fcaminho,fnumero, filtro)
    for i in range(len(bciencia)):
        img = bciencia[i]/imagem_flat
        fbciencia.append(img)
    return fbciencia

def sfbimagens(bcaminho, fcaminho, icaminho, campo, bnumero, fnumero, filtro):
    sfbciencia = []
    fbciencia = fbimagens(bcaminho, fcaminho, icaminho, campo, bnumero, fnumero, filtro)
    imagem_sky = sky.imagem_sky(bcaminho,fcaminho,icaminho,campo,bnumero,fnumero,filtro)
    for i in range(len(fbciencia)):
        img = fbciencia[i] - imagem_sky
        sfbciencia.append(img)
    return sfbciencia

