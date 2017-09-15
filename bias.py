#calcula a mediana do bias

import numpy as np #pacote para trabalhar com matrizes
from astropy.io import fits #pacote para trabalhar com imagens em formato fits

def bias_median(path, numbers, filtro):
    '''
    O primeiro passo de um processo de tratamento de dados padrão IRAF é fazer a correção 
    do bias, para tanto é necessário tirar a mediana dos bias para poder remove-los das demais 
    imagens
    A mediana deve ser feita elemento por elemento da matriz de dados das imagens bias, para tanto
    é necessário que o usuario forneça o caminho do diretório que contem as imagens bias, e a
    quantidade de imagens bais que possui. Exemplo:
        bias('/home/brambila/UFRJ/TDA/projeto_1_tda/xo2b/', 3, 'B')
        #/home/brambila/UFRJ/TDA/projeto_1_tda/xo2b/ -> caminho do diretório
        #3 -> quantidade de imagens bias
        #B -> filtro da imagem
        array([[ 286.88000488,  285.87915039,  288.06213379, ...,  315.57910156,
            316.58032227,  316.63049316],
        [ 285.38061523,  285.38134766,  286.38110352, ...,  311.60235596,
            314.52593994,  314.47576904],
        [ 285.87982178,  286.05993652,  287.06103516, ...,  316.52642822,
            314.57836914,  314.62750244],
        ..., 
        [ 285.05438232,  287.05535889,  287.05462646, ...,  312.50134277,
            315.63708496,  315.71685791],
        [ 288.60974121,  285.61022949,  288.05279541, ...,  313.49945068,
            314.63500977,  314.71636963],
        [ 284.61010742,  284.05200195,  284.60986328, ...,  313.63592529,
            313.63568115,  313.71594238]])
    '''  
    #criando listas vazias onde serão adicionado os dados e os headers de cada imagens bias no diretŕoio
    bias_images = []    
    bias_header = []
    
    # o loop ira percorrer o diretório abrindo as imagens, salvando seus dados e header nas listas
    # acima
    for i in range (numbers):
        a=str(i+1)  #nao existe imagens 0, portanto é necessário incrementar o contador
        # decide a forma que os nomes estão escritos
        if i+1 >= 10:
            bias_path = path + 'bias.%s.00%s.fits' %(filtro, str(a))
        else:
            bias_path = path + 'bias.%s.000%s.fits' %(filtro, str(a))
        #abre a imagem atual e o hedaer atual
        img, hdr = fits.getdata(bias_path, header=True)
        # converte os dados para float64
        img = np.array(img, dtype='Float64')   
        #adiciona a imagem e o header na suas respectivas listas
        bias_images.append(img)
        bias_header.append(hdr)
    #faz a mediana elemento a elemento (axix=0)
    median = np.median(bias_images, axis=0)
    return median
