#Executa todas as correcoes

from astropy.io import fits
import numpy as np 
import bias
import flat
import sky

def bimagens(bcaminho, icaminho, campo, bnumero, filtro):
    '''Função que corrige o bias das imagens de ciencia. Tem como entrada:
        
            bimagens(bcaminho, icaminho, campo, bnumero, filtro)
        
    Retorna uma lista de imagens corrigidas para o bias.    
    '''
    bciencia = [] #lista onde se add as imagens corrigidas
    imagen_ciencia = sky.abrindo_imagens(icaminho,campo)[0] # fornece os daddos das imagens de ciencia
    header_ciencia = sky.abrindo_imagens(icaminho,campo)[1] # abre o header
    imagen_bias = bias.bias_median(bcaminho,bnumero, filtro) #chama a matriz mediana das imagens bias
    #realiza a correção e a adição das imagens na lista
    for i in range(len(imagen_ciencia)):
        img = imagen_ciencia[i] - imagen_bias
        header_ciencia[i]['Bias'] = 'feito' #add no header da imagem que a correção para bias foi feita
        bciencia.append(img)

    return bciencia
 
def fbimagens(bcaminho, fcaminho, icaminho, campo, bnumero, fnumero, filtro):
    '''Função que corrige as imagens para o flat. Usa as imagens já corrigidas para o bias. Tem como entrada:

            fbimagens(bcaminho, fcaminho, icaminho, campo, bnumero, fnumero, filtro)

    Tem como saída, uma lista de imagens corrigidas tanto para bias quanto para flat field
    '''
    fbciencia = [] #lista onde se add as imagens corrigidas
    #chama a função que fornece as imagens corrigidas para bias
    bciencia = bimagens(bcaminho, icaminho, campo, bnumero, filtro) 
    #chama a função que fornece a matriz mediana e normalizada das imagens flat
    header_ciencia = sky.abrindo_imagens(icaminho,campo)[1]
    imagem_flat = flat.flat_field(bcaminho, fcaminho, bnumero, fnumero, filtro)
    #realiza a correção e adição das imagens na lista
    for i in range(len(bciencia)):
        img = bciencia[i]/imagem_flat
        header_ciencia[i]['Flat'] = 'feito'
        fbciencia.append(img)
    return fbciencia

def sfbimagens(bcaminho, fcaminho, icaminho, campo, bnumero, fnumero, filtro):
    '''Função que corrige as imagens para o sky. Usa as imagens já corrigidas para bias e flat. Tem como entrada:
            
            sfbimagens(bcaminho, fcaminho, icaminho, campo, bnumero, fnumero, filtro)

    Tem como saída, uma lista de imagem com todas as correções realizadas
    '''
    sfbciencia = [] #lista onde se add as imagens corrigidas
    #chama a função que fornece a lista de imagens corrigidas para bias e flat
    fbciencia = fbimagens(bcaminho, fcaminho, icaminho, campo, bnumero, fnumero, filtro)
    #chama a função que deternima a região de céu e fornece a matriz aleatória poissonica do sky
    imagem_sky = sky.imagem_sky(bcaminho,fcaminho,icaminho,campo,bnumero,fnumero,filtro)
    header_ciencia = sky.abrindo_imagens(icaminho,campo)[1]
    #realiza a correção e adição das imagens na lista
    for i in range(len(fbciencia)):
        img = fbciencia[i] - imagem_sky
        header_ciencia[i]['Sky'] = 'feito'
        sfbciencia.append(img)
    return sfbciencia

