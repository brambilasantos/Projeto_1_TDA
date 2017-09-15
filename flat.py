#Remove o bias do flat, normaliza e faz a mediana

from bias import bias_median
from astropy.io import fits
import numpy as np 


def abrindo_flat(fcaminho, fnumero, filtro):
    '''Função responsavel por abrir as imagens de flat. Recebe como parametro o caminho das imagens, a quantidade de 
    imagens flat e o filtro em que elas foram feitas:
        abrindo_flat(fcaminho, fnumero, filtro)

    Retorna uma lista de dois elementos:
        abrindo_flat(fcaminho, fnumero, filtro)[0] -> lista de imagens flat
        abrindo_flat(fcaminho, fnumero, filtro)[1] -> lista dos headers flat
    '''
    #definindo duas listas vazias que serão preenchidas com as imagens e com os headers
    flat_img = []
    flat_hdr= []
    for i in range(fnumero):
        a=str(i+1)  #nao existe imagens 0, portanto é necessário incrementar o contador
        # decide a forma que os nomes estão escritos
        if i+1 >= 10:
            flat_path = fcaminho + 'flat.%s.00%s.fits' %(filtro, str(a))
        else:
            flat_path = fcaminho + 'flat.%s.000%s.fits' %(filtro, str(a))
        #abre a imagem atual e o hedaer atual
        img, hdr = fits.getdata(flat_path, header=True)
        # converte os dados para float64
        img = np.array(img, dtype='Float64')   
        #adiciona a imagem e o header em suas respectivas listas
        flat_img.append(img)
        flat_hdr.append(hdr)
    return flat_img, flat_hdr

def correcao_flat_bias(bcaminho, fcaminho, bnumero, fnumero, filtro):
    ''' Antes de obter o flat field é necessario que as imagens flat sejam corrigidas para bias. Recebe de entrada:
        
            correcao_flat_bias(baminho, fcaminho, bnumero, fnumero, filtro)
        
    Tem como retorno as imagens de flat corrigidas por bias.
    '''
    #abre as imagens de flat
    images_flat = abrindo_flat(fcaminho, fnumero, filtro) 
    #Lista vazia que sera preenchida com as imagens corrigidas
    bflat = []
    for i in range(len(images_flat[0])):
        correcao = images_flat[0][i] - bias_median(bcaminho, bnumero, filtro) #correção bias
        bflat.append(correcao) #add na lista
    return bflat

def norm_flat(bcaminho, fcaminho, bnumero, fnumero, filtro):
    ''' Antes de se fazer a mediana elemento a elemento das imagens flat é necessário que todas as imagens estejam 
    normalizadas. Essa normalização é feita dividindo todos os elementos da matriz pelo valor médio da todos os elementos
    da matriz. Recebe como parâmetros de entrada:
        
        norm_flat(bcaminho, fcaminho, bnumero, fnumero, filtro)

    Tem como retorno as imagens normalizadas e prontas para retirar a mediana dos elementos.
    '''
    #Abre as imagens a serem normalizadas
    bflat = correcao_flat_bias(bcaminho, fcaminho, bnumero, fnumero, filtro)
    #lista onde será guardado os resultados
    flat_norm = []
    for i in range(len(bflat)):
        flat_norm.append(bflat[i]/np.mean(bflat[i])) #normaliza as matrizes
    return flat_norm

def flat_field(bcaminho, fcaminho, bnumero, fnumero, filtro):
    '''Função que retorna a mediana elemento a elemento. Tem como entrada:

        flat_field(bcaminho, fcaminho, bnumero, fnumero, filtro)

    Tem como sainda, uma única matriz em que o elemento a11 será o valor mediano de todos os a11 de todas as matrizes 
    normalizadas e corrigidas para bias. 

    '''
    #faz a mediana elemento a elemento (axis=0)
    median_flat = np.median(norm_flat(bcaminho, fcaminho, bnumero, fnumero, filtro), axis=0) 
    return median_flat
