#! /usr/bin/env python3 #
# -*- coding: utf-8 -*- #

import pandas as pd
import numpy  as np
import plotly.express as px
import plotly.graph_objects as go
import seaborn as sns
import matplotlib.pyplot as plt

import warnings
warnings.filterwarnings('ignore')

## pandas configuration
pd.set_option('display.max_rows', 200)
pd.set_option('display.max_columns', 100)

## matplot configuration
plt.rcParams['figure.figsize'] = (15, 6)
plt.style.use('ggplot')

## importing dataset
base_dados = pd.read_csv('../Data Set/clean_data.csv')

## basic dataset information
print(f"Dimensional of imported dataset: {base_dados.shape}\n")
print(f"First 5 lines of the dataset\n{base_dados.head()}\n")
print(f"Dataset summary\n{base_dados.info()}\n")
print(f"Show the number of null data for each column\n"
      f"{base_dados.isnull().sum()}\n")

print(f"Showing the number of unique values for each column\n"
      f"{base_dados.nunique()}")

## removing column Unnamed: 0 since it is only a record count for
## each line of the dataset
base_dados.drop(columns=['Unnamed: 0'], inplace=True)

## analyzing the data for mayors
query_prefeitos = base_dados[
    (base_dados['job'] == 'prefeito') &
    (base_dados['elector_count'] == 's')
]

## analyzing the number of mayors elected by main party
analise_01 = query_prefeitos.groupby(by=['main_party']).agg(
    quantidade=('candidate_vote_count', 'count')
)

number_elected_mayors = analise_01['quantidade'].sum()
analise_01['%'] = analise_01['quantidade'] / number_elected_mayors * 100
analise_01['%'] = round(analise_01['%'], 2)
analise_01.sort_values('quantidade', inplace=True, ascending=False)

## plotting the graphic with the analyzes analise_01
## creating a pallet of colors using seaborn
paleta_cores = sns.color_palette('magma', len(analise_01))

## configuring the size of the graph
plt.figure(figsize=(20,6))

## plotting the graph itself
plt.bar(analise_01.index,
        analise_01['quantidade'],
        width=0.9,
        color=paleta_cores)

## configuring the title
plt.title('Prefeitos eleitos no país',
          loc='left',
          fontsize=20,
          color='#404040',
          fontweight=600)

## configuring the labels
plt.ylabel('Quantidade de prefeitos')
plt.xlabel('Partidos')
plt.xticks(rotation=90)

## changing y axis limit value to add some space after the
## maximum value
plt.ylim(0, analise_01['quantidade'].max() * 1.1)

## adding labels for each bar of the graph
for posicao, valor in enumerate(analise_01['quantidade']):
    plt.text(
        ## position of the label
        posicao -0.3,
        valor +10,
        ## label text
        valor,
        ## label color
        color=paleta_cores[posicao],
        ## label size and font
        size=12,
        fontweight=700
    )

plt.annotate(
    f'Eleitos Brasil: {analise_01["quantidade"].sum()}',
    xy=(0.99,0.94),
    xycoords='axes fraction',
    ha='right',
    va='center',
    color='green',
    fontsize=14,
    bbox=dict(facecolor='#ffffff',
               edgecolor='green',
               boxstyle='round',
               pad=0.25)
)

plt.savefig('analise_prefeitos.png')
plt.clf()
plt.close()

## analyzing data for councilors
query_vereadores = base_dados[
    (base_dados['job'] == 'vereador') &
    (base_dados['elector_count'] == 's')
]

analise_02 = query_vereadores.groupby(by='main_party').agg(
    quantidade = ('candidate_vote_count', 'count')
)

number_elected_councilors = analise_02['quantidade'].sum()
analise_02['%'] = analise_02['quantidade'] / number_elected_councilors * 100
analise_02['%'] = round(analise_02['%'], 2)
analise_02.sort_values('quantidade', inplace=True, ascending=False)

plt.figure(figsize=(12,10))
plt.hlines(
    y=analise_02.index,
    xmin=0,
    xmax=analise_02['quantidade'],
    lw=5,
    color=paleta_cores,
    alpha=0.5
)

plt.scatter(
    analise_02['quantidade'],
    analise_02.index,
    s=100,
    color=paleta_cores,
    alpha=0.8
)

plt.title('Vereadores eleitos no país',
          loc='left',
          fontsize=20,
          color='#404040',
          fontweight=500)

plt.annotate(
    f'Eleitos Brasil: {analise_02["quantidade"].sum()}',
    xy=(0.99,0.94),
    xycoords='axes fraction',
    ha='right',
    va='center',
    color='green',
    fontsize=14,
    bbox=dict(facecolor='#ffffff',
               edgecolor='green',
               boxstyle='round',
               pad=0.25)
)

plt.savefig('analise_vereadores.png')
plt.clf()
plt.close()

## correlation analysis
## checking if there is any relationship between the number of mayors
## and councilors elected by party
correlation_table = analise_01['quantidade'].reset_index()
correlation_table = pd.merge(correlation_table,
                             analise_02.reset_index(),
                             on=['main_party'],
                             how='inner')
correlation_table.columns = ['Partido', 'Prefeitos', 'Vereadores', '%']
correlation_table.drop(columns=['%'], inplace=True)

sns.regplot(
    x=correlation_table['Prefeitos'],
    y=correlation_table['Vereadores'],
    ci=95,
    scatter_kws={
        'color': 'blue',
        's': 80,
        'alpha': 0.5},
    line_kws={
        'color': 'orange',
        'alpha': 0.2,
        'lw': 2
    }
)

plt.title('Prefeitos vs Vereadores eleitos')

## adding the party for mayors and councilors
for line in range(0, correlation_table.shape[0]):
    plt.text(
        correlation_table['Prefeitos'][line] + 0.8,
        correlation_table['Vereadores'][line],
        correlation_table['Partido'][line],
        size='medium',
        color='gray',
        weight='semibold'
    )

plt.savefig('analise_correlacao.png')
plt.clf()
plt.close()

## retrieves the amount of candidate by party, elected or not
candidate_party = base_dados.groupby(by=['main_party']).count().iloc[:,0:1].reset_index()
candidate_party.columns = ['Partido', 'Candidatos']

correlation_table = pd.merge(correlation_table,
                             candidate_party,
                             on=['Partido'],
                             how='inner')
print(correlation_table.head())

figure = plt.figure(figsize=(15,8))
eixo = figure.add_subplot(111, projection='3d')
eixo.scatter(
    correlation_table['Prefeitos'],
    correlation_table['Vereadores'],
    correlation_table['Candidatos'],
    c='black',
    s=100
)

eixo.view_init(30, 185)

eixo.set_xlabel('Prefeitos')
eixo.set_ylabel('Vereadores')
eixo.set_zlabel('Candidatos')

# plt.show()
plt.clf()
plt.close()

figura = px.scatter_3d(
    correlation_table,
    x='Prefeitos',
    y='Vereadores',
    z='Candidatos',
    color='Partido',
    opacity=0.7,
    symbol='Partido'
)

figura.show()
