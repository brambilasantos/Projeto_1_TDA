#remove o bias do flat

from bias import bias_median as bm
from astropy.io import fits
import numpy as np 


def abrindo_flat(caminho, quantidade, filtro):
    flat_img = []
    flat_hdr= []
    for i in range(quantidade):
        a=str(i+1)  #nao existe imagens 0, portanto é necessário incrementar o contador
        # decide a forma que os nomes estão escritos
        if i+1 >= 10:
            flat_path = caminho + 'flat.%s.00%s.fits' %(fitro, str(a))
        else:
            flat_path = caminho + 'flat.%s.000%s.fits' %(filtro, str(a))
        #abre a imagem atual e o hedaer atual
        img, hdr = fits.getdata(flat_path, header=True)
        img = np.array(img, dtype='Float64')   
        flat_img.append(img)
        flat_hdr.append(hdr)
    return flat_img, flat_hdr

def correcao_flat_bias(caminho, quantidade, filtro):
    images_flat = abrindo_flat(caminho, quantidade, filtro)
    bflat = []
    for i in range(len(images_flat[0])):
        correcao = images_flat[0][i] - bm(caminho,quantidade, filtro)
        bflat.append(correcao)
    return bflat

def norm_flat(caminho, quantidade, filtro):
    bflat = correcao_flat_bias(caminho, quantidade, filtro)
    flat_norm = []
    for i in range(len(bflat)):
        flat_norm.append(bflat[i]/np.mean(bflat[i]))
    return flat_norm

def flat_field(caminho, quantidade, filtro):
    median_flat = np.median(norm_flat(caminho, quantidade, filtro, axis=0)
    return median_flat
