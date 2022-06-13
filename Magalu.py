import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.graph_objects as go

BaseDados = pd.read_excel('Vase_004 - Magalu - Sem Resolução.xlsx')

#Series Temporais
Dados = BaseDados.set_index('Data')
plt.style.use('seaborn-darkgrid')
plt.figure(figsize=(10,5))
plt.plot(Dados.index,Dados['Fechamento'])
plt.title('Análise das Acões Magalu - Fechamento',fontsize=15,loc='left')
plt.xlabel('Período da Cotação')
plt.ylabel('Valor da Ação($)')
print(plt.show())
print(Dados.tail())

MediaMovel=Dados['Fechamento'].rolling(15).mean()
MediaTendencia=Dados['Fechamento'].rolling(30).mean()
plt.style.use('seaborn-darkgrid')
plt.figure(figsize=(10,5))
plt.plot(Dados.index,Dados['Fechamento'])
plt.plot(Dados.index,MediaMovel)
plt.plot(Dados.index,MediaTendencia)
plt.title('Análise das Acões Magalu - Fechamento',fontsize=15,loc='left')
plt.xlabel('Período da Cotação')
plt.ylabel('Valor da Ação($)')

print(plt.show())


BaseDados['Mes'] = BaseDados['Data'].dt.month
plt.title('Oscilações de valores por Mês',fontsize=14,loc='left')
sns.boxplot( data=BaseDados, x='Mes', y='Fechamento');
print(plt.show())

pd.set_option('display.max_columns',8)
pd.set_option('display.width',1000)
TabelaAnalitica=BaseDados.groupby(['Mes']).describe()['Fechamento']
print(TabelaAnalitica)

Grafico = go.Figure( data=[go.Candlestick(x=Dados.index,open = Dados['Abertura'],high=Dados['Maior'],
low= Dados['Menor'],close= Dados['Fechamento'])])
Grafico.update_layout( xaxis_rangeslider_visible=False)
print(Grafico.show())