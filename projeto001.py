#projeto001 Tratamento de Dados


def bias():  
    '''
    O primeiro passo de um processo de tratamento de dados padrão IRAF é fazer a correção 
    do bias, para tanto é necessário tirar a mediana dos bias para poder remove-los das demais 
    imagens

    A mediana deve ser feita elemento por elemento da matriz de dados das imagens bias, para tanto
    é necessário que o usuario forneça o caminho do diretório que contem as imagens bias, e a
    quantidade de imagens bais que possui. Exemplo:
        bias('/home/brambila/UFRJ/TDA/projeto_1_tda/xo2b/', 3)
        #/home/brambila/UFRJ/TDA/projeto_1_tda/xo2b/ -> caminho do diretório
        #3 -> quantidade de imagens bias

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

    #%matplotlib inline 
    #pacote para visualização gráfica
    import matplotlib.pyplot as plt 
    #pacote para trabalhar com matrizes
    import numpy as np 
    #pacote para importar e exportar dados e trabalhar comd dataframes
    import pandas as pd
    from astropy.io import fits

#criando listas vazias onde serão adicionado os dados e os headers de cada imagens bias no diretŕoio
    bias_images = []    
    bias_header = []

    for i in range (numbers):
        a=str(i+1)
        if i+1 == 10:
            bias_path = path + 'bias.B.00%s.fits' %str(a)
        else:
            bias_path = path + 'bias.B.000%s.fits' %str(a)
        img, hdr = fits.getdata(bias_path, header=True)
        img = np.array(img, dtype='Float64')   
        bias_images.append(img)
        bias_header.append(hdr)
bias_median = np.median(bias_images, axis=0)
return bias_median
