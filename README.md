	Esse é um projeto cuja a finalidade é realizar a redução padrão IRAF de imagens, foi desenvolvido para a diciplina de Tratamento de Dados ministrada no Observatório do Valongo pelo prof. Walter Martins Filho no segundo semestre de 2017. Ele tem como objetivo testar a compreenção do processo de redução padrão IRAF e sua automatização. A pipeline foi testada com um conjunto de imagens que possui 10 imagens de flat, 10 imagens de bias e 132 imagens de ciência. Ela foi escrita em python e esta dividida ao longo de 5 arquivo com multíplas funções.

1º) bias.py:
	
	Esse arquivo possui apenas uma função, bias_median(bcaminho, bnumro, filtro), onde baminho é o caminho dos diretórios das imagens 		bias, bnumero é a quantidade de imagens bias presentes nesse diretório e que serão usadas e filtro é o filtro em que as imagens bias 		foram produzidas. Essa função tem como retorno uma matriz onde seu elemento aij é o valor mediano de todos os elementos aij de todas 		as imagens bias.

2º) flat.py:
	
	Esse arquivo possui quatro funções, abrindo_flat(fcaminho, fnumero, filtro), correcao_flat_bias(bcaminho, fcaminho, bnumero, 		fnumero, filtro), norm_flat(bcaminho, fcaminho, bnumero, fnumero, filtro) e flat_field(bcaminho, fcaminho, bnumero, fnumero, 		filtro). Onde, bcaminho, bnumero e filtro forma explicados no item anterior, fcaminho é semelhante ao bcaminho mas agora para as 		imagens flat, fumero segue a mema lógica.
	A função abrindo_flat() irá abrir as imagens flat e salva-las em uma lista para poderem ser utilizadas. 

	A função correcao_flat_bias() irá usar a matriz fornecida por bias_median() para subtrair o bias das imagens de flat.

	A função norm_flat() irá normalizar as imagens de flat. Isso é feito imagem a imagem, isto é, divide-se cada uma das imagens pelo 		valor médio dos elementos das respectivas imagens.

	A função flat_field() utiliza essas matrizes normalizadas e retorna uma matriz de valores medianos seguindo o memso processo que 		explicado para a função bias_median()

3º) sky.py

	Esse arquivo possui duas funções, abrindo_imagens(icaminho,campo) e imagem_sky(bcaminho, fcaminho, icaminho, campo, bnumero, 		fnumero, filtro). Onde icaminho é o caminho do diretório das imagens de ciência e campo é o campo de observaçõ que nomeia as 		imagens	(ex: xo2b.0001.fits, neste casso xo2b é o campo).

	A função abrindo_imagens() irá abrir as imagens de ciência e salva-las em uma lista para poderem ser utilizadas.

	Já a função imagem_sky() possui duas funções, definir a região do céu (essa informação é fornecida pelo usuário com base numa imagem 		amostral fornecida) que não tem estrelas e utlizar essa informação para se produzir uma matriz rondomica e poissonica com 		dimensões iguais as imagens de ciência. Essa matriz será utlizada para subtrair a luz de fundo das imagens de 	ciência.

4º) correcoes.py

	Esse arquivo possui três funções que realizam todas as correções que a imagem de ciência precisa sofrer. bimagens(bcaminho, 		icaminho, campo, bnumero, filtro), fbimagens(bcaminho, fcaminho, icaminho, campo, bnumero, fnumero, filtro), sfbimagens(bcaminho, 		fcaminho, icaminho, campo, bnumero, fnumero, filtro), os parâmetros já foram explciado ao longo do texto em itens anteriores.

	A função bimagens() realiza a correção de bias para a imagem de ciência, e o faz chamando a função bias_mediam do arquivo bias.py e 		subtraindo a matriz fornecida por essa função das imagens de cinência retornando assim uma lista de imagens corrigidas para bias.

	A função fbimagens() realiza a correção do flat field das imagens de ciência, e o fáz chamando as funções flat_field() do arquivo 		flat.py e a funão bimagem() que esta no mesmo arquivo que a fbimagem(). A correção flat_field é feita dividindo-se todas as bimagens 		pela matriz fornecida pela função flat_field().
	
	Já a função sfbimagens() realiza a correção final das imagens. Ela é responsavel por remover a luz de fundo de todas as imagens de 		ciência. Ela o fáz chamando as funções imagem_sky() do arquivo sky.py e a fbimagem() presente no mesmo arquivo que a sfbimagens(). A 		correção do sky é feita subtraindo-se a matriz rondomica e poissonica fornecida pela função imagem_sky() das imagens de ciência que 		já fora tratadas para flat e bias fornecidas pela função fbimagens().

5º principal.py

	Esse arquivo possui apenas uma função, iniciando_correcoes(). Essa função é interativa com o usuário e será onde o usuário irá 		definir todos os parâmetros utilizados nas funções explicadas anteriormente. Portanto, para se dar início a redução de imagens é 		esse arquivo que deve ser executado. Ele irá perguntar o caminho do diretório em que as imagens de ciência, bias e flat estão, o 		campo de observação, a quantidade de bias e flat e o filtro de observação. Para que o programa funcione corretamente é improtante 		que os padrões de nomenclatura das iamgens sejam respeitados:
		
		ciência:
			campo.numero.fits, onde campo é o campo de observação e numero é o número da imagem
			(xo2b.0002.fits, ..., xo2b.0098.fits, ..., xo2b.0260.fits,...)

		bias:
			bias.filtro.numero.fits, onde filtro é o filtro da observação.
			(bias.B.0001.fits, ..., bias.B.0010.fits)

		flat:
			flat.filtro.numero.fits
			(flat.B.0001.fits, ..., flat.B.0010.fits)
	
	Após informar os parâmetros o código irá chamar as funções de correção e plotará imagens comparativas e informará da execução das 		correções. O retorno dessa função são as imagens completamente corrigidas.
			



















