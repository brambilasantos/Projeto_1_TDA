import matplotlib.pyplot as plt
from correcoes import *
import bias
import flat
import sky
def iniciando_correcoes():
    ''' Esta é a função a qual inicia a correção das imagens. Ela possui parâmetros livres.
    Esta função sera responsal por defenir todos os parâmetros de entrada das demais funções
    presentes na pipeline, seja em qual estagio de correção for. 
    a regra de nomeação de imagens devem ser respeitadas:
        imagem de ciencia:
            campo.numero.fits -> xo2b.0001.fits, xo2b.0002.fits, ..., xo2b.0099.fits,...,
                                 xo2b.0300.fits, ...
        imagem de bias:
            bias.filtro.numero.fits -> bias.B.0001.fits,..., bias.B.0011.fits
       
        imagem de flat:
            flat.filtro.numero.fits -> flat.B.0001.fits,..., flat.B.0011.fits
        
        

    '''
    #definindo os parâmetros
    icaminho = input('Indique o caminho do diretorio que contem as imagens de ciencia: ')
    campo = input('Indice o nome do campo de observacao: ')
    bcaminho = input('Indique o caminho do diretorio que contem as imagens de bias: ')
    fcaminho = input('Indique o caminho do diretorio que contem as imagens de flat: ')
    bnumero = int(input('Indique a quantidade de imagens bias existentes: '))
    fnumero = int(input('Indique a quantidade de imagens flat existentes: '))
    filtro = input('Indique o filtro usado: ')
    
    print('Realizando o Bias')
    #chama a função do arquivo sky que abre as imagens originais
    imagem_original = sky.abrindo_imagens(icaminho,campo)[0] 
    #chama a função do arquivo correcoes que corrige as imagens originais pro bias
    imagem_pos_bias = bimagens(bcaminho,icaminho,campo,bnumero,filtro)[0]                                                    #
    #plota as imagens antes e depois da correção bias para comparação
    plt.figure() #abre a janela gráfica
    fig, eixos = plt.subplots(nrows=1, ncols=2, figsize=(15,10)) #define gráficos lado a lado
    original = eixos[0].imshow(imagem_original,vmin=np.mean(imagem_original)-2.5*np.std(imagem_original),
        vmax=np.mean(imagem_original)+2.5*np.std(imagem_original),cmap=plt.cm.gray,origin='lower')#plot a primeira imagem
    eixos[0].set_title('Imagem Original') #nomeia o primeiro gráfico
    bias = eixos[1].imshow(imagem_pos_bias,vmin=np.mean(imagem_pos_bias)-2.5*np.std(imagem_pos_bias),
        vmax=np.mean(imagem_pos_bias)+2.5*np.std(imagem_pos_bias),cmap=plt.cm.gray,origin='lower') #plot a segunda imagem
    eixos[1].set_title("Depois do Bias") #nomeia o segundo gráfico
    plt.show()#mostra a imagem
    #
    print ('Realizando o Flat')
    #abre as imanges corrigdas para flat e bias
    imagem_pos_flat = fbimagens(bcaminho,fcaminho,icaminho,campo,bnumero,fnumero,filtro)[0] 
    #plota as imagens pós correção bias (antes de flat) e pós correção bias e flat para comparação    
    plt.figure()
    fig, eixos = plt.subplots(nrows=1, ncols=2, figsize=(15,10))
    bias = eixos[0].imshow(imagem_pos_bias,vmin=np.mean(imagem_pos_bias)-2.5*np.std(imagem_pos_bias),
        vmax=np.mean(imagem_pos_bias)+2.5*np.std(imagem_pos_bias),cmap=plt.cm.gray,origin='lower')  
    eixos[0].set_title('Antes do Flat')
    flat = eixos[1].imshow(imagem_pos_flat,vmin=np.mean(imagem_pos_flat)-2.5*np.std(imagem_pos_flat),
        vmax=np.mean(imagem_pos_flat)+2.5*np.std(imagem_pos_flat),cmap=plt.cm.gray,origin='lower')
    eixos[1].set_title("Depois do Flat")
    plt.show()
    #        
    print ('Realizando o Sky')
    #chama a função do arquivo correcoes que corrige o sky
    imagens_ciencia = sfbimagens(bcaminho,fcaminho,icaminho,campo,bnumero,fnumero,filtro)
    #Plota uma imgem orginal e uma completamente corrigida para comparação
    plt.figure()
    fig, eixos = plt.subplots(nrows=1, ncols=2, figsize=(15,10))
    original = eixos[0].imshow(imagem_original,vmin=np.mean(imagem_original)-2.5*np.std(imagem_original),
        vmax=np.mean(imagem_original)+2.5*np.std(imagem_original),cmap=plt.cm.gray,origin='lower')
    eixos[0].set_title("Imagem Antes de todas as correções")
    final = eixos[1].imshow(imagens_ciencia[0],vmin=np.mean(imagens_ciencia[0])-2.5*np.std(imagens_ciencia[0]),
        vmax=np.mean(imagens_ciencia[0])+2.5*np.std(imagens_ciencia[0]),cmap=plt.cm.gray,origin='lower')
    eixos[1].set_title("Após todas as correções")
    plt.show()
    print ("Todas as correções foram realizadas")  
    return imagens_ciencia

/home/brambila/UFRJ/TDA/projeto_1_tda/xo2b/