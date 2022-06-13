# Analise-de-Dados-Acoes-Magalu

## Descrevendo o Código e os Gráficos:

A importação do Arquivo foi feita em excel do site da Kaggle, os dados já estavam limpos, só precisei fazer a Análise Financeira e plotagem.

### Gráfico de Serie Temporal
Para a criação do primeiro Gráfico eu coloquei a coluna [Data] como index para melhorar a visualização e inseri no eixo X, usei os dados da coluna [Fechamento] para utilizar no eixo Y. 
Estilizei o grafico de Serie Temporal com uma cor mais escura e inseri o Grid, ajustei o tamanho do grafico e coloquei os nomes nos eixos.

![Bilby Stampede](https://github.com/wesleymartins95/Analise-de-Dados-Acoes-Magalu/blob/main/Grafico%20Temporal.png)

Observando o Gráfico podemos ver que a Abertura das Ações foi entre R$:25,00 e R$:26,00 e quase no final de janeiro ele teve uma alta, mas a partir daí ele começou a fechar por vários dias em baixa, e então, na metade do mês de julho teve uma pequena alta por curto período, e logo em seguida começa a declinar até o final de dezembro, fechando a ação em R$:7,22. 

Podemos ver os 5 ultimos valores exatos de fechamentos neste arquivo em pdf:
![Bilby Stampede](https://github.com/wesleymartins95/Analise-de-Dados-Acoes-Magalu/blob/main/Ultimos%20dados%20A%C3%A7%C3%B5es.pdf)

### Gráfico Temporal de Médias Moveis

Para esse Gráfico criei uma variavel chamada MediaMovel e nela coloco a coluna [Fechamento] usando as funções rolling(15).mean() que é a seleção de 15 em 15 dos dados além de fazer a média desse periodo de dados.
Em seguida crio outra váriavel chamada MediaTendencia e uso a mesma coluna e as mesmas funções mas agora no periodo de 30 dias.
É feito a estilização e vou usar as 3 variaveis para fazer a plotagem, os Dados do fechamento, a MediaMovel e MediaTendencia.

![Bilby Stampede](https://github.com/wesleymartins95/Analise-de-Dados-Acoes-Magalu/blob/main/Grafico%20Media_Movel.png)

Linha Azul: São os dados do Fechamento diário.   
Linha Laranja: Média Móvel de 15 dias.
Linha Verde: Média de Tendencia.   
A MédiaMovel ela tira a oscilação, quanto mais você aumenta ela maior é a linha de Tendencia. Assim podemos ver a linha verde.  
Usar a Média Móvel é importante para Analisar os comportamentos de uma Serie Temporal.


### Gráfico Temporal em BloxPlot

Nessa plotagem inclui uma coluna [Mes] e usei o parametro dt.month para selecionar os meses, em seguido utilizei a função do Seaborn ( data=BaseDados, x='Mes', y='Fechamento'), que faz a leitura dos dados e passa os valores das colunas para os eixos.
![Bilby Stampede](https://github.com/wesleymartins95/Analise-de-Dados-Acoes-Magalu/blob/main/Grafico%20BoxPlot.png)

No Gráfico podemos ver os meses que tiveram mais ocilações, que mais variaram os valores que foram Março e teve maior média e Novembro com menor média. Os que obtiveram menos Ocilações Junho e Dezembro ou seja tiveram baixa variabilidade e desvio padrão. Porém o mês de Junho está posicionado na parte superior da tela, que significa que a média e o valor mediano são valores mais altos.   

### Gráfico Temporal em Candle 
É o grafico utlizado para Bolsa de valores
Para utilizar esse gráfico importei a biblioteca plotly.graph_objects as go  
Criei a variavel chamada Grafico e inseri os parametros = go.Figure( data=[go.Candlestick(x=Dados.index,open = Dados['Abertura'],high=Dados['Maior'],
low= Dados['Menor'],close= Dados['Fechamento'])])
Quando a plotagem for feita e você passar o mouse por cima das linhas aparecerá dentro de uma caixa a data, o valor da abertura da Ação, o valor maior, menor e quanto fechou. Se estiver vermelho fechou em baixa, se estiver verde fechou em alta.  
A linha de código a seguir foi só para remover a opção de zoom: Grafico.update_layout( xaxis_rangeslider_visible=False)

![Bilby Stampede](https://github.com/wesleymartins95/Analise-de-Dados-Acoes-Magalu/blob/main/Grafico%20Candle.png)

Podemos ver que a cor dominate é o vermelho, então chegamos a conclusão que as Ações da Magalu tiveram muitas baixas.
